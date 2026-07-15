"""
DealDesk Service

Main orchestration service.
"""

from __future__ import annotations

from .crm_service import CRMService
from .catalog_service import CatalogService
from .pricing_service import PricingService
from .approval_service import ApprovalService
from .drive_service import DriveService
from .rag_service import RAGService
from .gemini_service import GeminiService


class DealDeskService:

    def __init__(self):

        self.crm = CRMService()

        self.catalog = CatalogService()

        self.pricing = PricingService()

        self.approval = ApprovalService()

        self.drive = DriveService()

        self.rag = RAGService()

        self.gemini = GeminiService()

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------

    def execute(

        self,

        customer: str,

        product: str,

        quantity: int,

        discount_percent: float = 0,

        tax_percent: float = 18,

        corpus_name: str | None = None,

        customer_reason: str = "",

        negotiation_attempt: int = 1,

    ):

        # -------------------------------------------------
        # CRM
        # -------------------------------------------------

        crm_context = self.crm.customer_context(

            customer,

        )

        if not crm_context:

            return {

                "status": "failed",

                "reason": "Customer not found.",

            }

        # -------------------------------------------------
        # Catalog
        # -------------------------------------------------

        catalog = self.catalog.product(

            product,

        )

        if not catalog:

            return {

                "status": "failed",

                "reason": "Product not found.",

            }

        # -------------------------------------------------
        # Quantity Validation
        # -------------------------------------------------

        if not self.pricing.valid_quantity(

            quantity,

        ):

            return {

                "status": "failed",

                "reason": "Invalid quantity.",

            }

        # -------------------------------------------------
        # Discount Policy
        # -------------------------------------------------

        if discount_percent > 0:

            decision = self.approval.negotiate(

                attempts=negotiation_attempt,

                customer_reason=customer_reason,

            )

            if decision["status"] != "SEND_FOR_APPROVAL":

                return {

                    "status": "pending",

                    "negotiation": decision,

                }

        # -------------------------------------------------
        # Pricing
        # -------------------------------------------------

        quote = self.pricing.generate(

            customer=customer,

            product_name=product,

            quantity=quantity,

            discount_percent=discount_percent,

            tax_percent=tax_percent,

        )

        # -------------------------------------------------
        # Approval
        # -------------------------------------------------

        approval = self.approval.summary(

            customer=customer,

            deal_id=quote["quote_id"],

            discount_percent=discount_percent,

            amount=quote["final_price"],

            customer_reason=customer_reason,

        )

        # -------------------------------------------------
        # Drive Documents
        # -------------------------------------------------

        documents = self.drive.customer_documents(

            customer,

        )

        # -------------------------------------------------
        # Knowledge Base
        # -------------------------------------------------

        rag_context = None

        if corpus_name:

            rag_context = self.rag.knowledge_context(

                corpus_name,

                customer,

                product,

            )

        # -------------------------------------------------
        # Proposal
        # -------------------------------------------------

        proposal = self.gemini.generate_proposal(

            customer=customer,

            crm=crm_context,

            quote=quote,

            catalog=catalog,

            drive_documents=documents,

            rag_context=rag_context,

        )

        # -------------------------------------------------
        # Executive Summary
        # -------------------------------------------------

        executive_summary = self.gemini.executive_summary(

            customer,

            proposal,

        )

        # -------------------------------------------------
        # Approval Note
        # -------------------------------------------------

        approval_note = self.gemini.approval_note(

            quote,

            approval,

        )

        # -------------------------------------------------
        # Customer Email
        # -------------------------------------------------

        customer_email = self.gemini.customer_email(

            customer,

            proposal,

        )

        # -------------------------------------------------
        # Internal Note
        # -------------------------------------------------

        internal_note = self.gemini.internal_note(

            proposal,

        )

        # -------------------------------------------------
        # Deal Completion Message
        # -------------------------------------------------

        deal_completed_message = self.gemini.deal_completed_message(

            customer,

            proposal,

        )

        # -------------------------------------------------
        # CRM Updates
        # -------------------------------------------------

        self.crm.update_status(

            quote["quote_id"],

            "PROPOSAL_GENERATED",

        )

        self.crm.add_note(

            customer,

            f"Proposal {quote['quote_id']} generated.",

        )

        self.crm.update_activity(

            customer,

            "Proposal Generated",

        )

        # -------------------------------------------------
        # Follow-up Decision
        # -------------------------------------------------

        followup_required = False

        followup_reason = None

        if approval.get("status") == "PENDING":

            followup_required = True

            followup_reason = "Awaiting internal approval."

        elif approval.get("status") == "REJECTED":

            followup_required = True

            followup_reason = "Discount request rejected."

        elif approval.get("status") == "APPROVED":

            followup_required = True

            followup_reason = "Proposal approved. Send follow-up."

        elif approval.get("status") == "NO_APPROVAL_REQUIRED":

            followup_required = True

            followup_reason = "Deal completed under standard terms. Send next steps."

        # -------------------------------------------------
        # Result
        # -------------------------------------------------

        return {

            "status": "success",

            "customer": customer,

            "crm": crm_context,

            "catalog": catalog,

            "quote": quote,

            "approval": approval,

            "documents": documents,

            "knowledge": rag_context,

            "proposal": proposal,

            "executive_summary": executive_summary,

            "approval_note": approval_note,

            "customer_email": customer_email,

            "internal_note": internal_note,

            "deal_completed_message": deal_completed_message,

            "followup": {

                "required": followup_required,

                "reason": followup_reason,

            },

        }

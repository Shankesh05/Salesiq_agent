"""
Follow-up Service

Main orchestration service.
"""

from __future__ import annotations

from .gmail_service import GmailService
from .drive_service import DriveService
from .crm_service import CRMService
from .rag_service import RAGService
from .gemini_service import GeminiService
from tools.sales.firestore_service import FirestoreService


class FollowupService:

    def __init__(self):

        self.gmail = GmailService()
        self.drive = DriveService()
        self.crm = CRMService()
        self.rag = RAGService()
        self.gemini = GeminiService()

        self.firestore = FirestoreService()

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------

    def execute(

        self,

        customer: str,

        customer_email: str,

        corpus_name: str | None = None,

    ):

        # -------------------------------------------------
        # CRM
        # -------------------------------------------------

        crm_context = self.crm.customer_context(customer)

        # -------------------------------------------------
        # Gmail
        # -------------------------------------------------

        previous = self.gmail.get_latest_conversation(customer)

        previous_email = (
            previous["body"]
            if previous
            else "No previous email conversation found."
        )

        # -------------------------------------------------
        # Google Drive
        # -------------------------------------------------

        proposal = self.drive.find_document(customer)

        # -------------------------------------------------
        # Vertex AI RAG
        # -------------------------------------------------

        knowledge = None

        if corpus_name:

            try:

                knowledge = self.rag.customer_context(

                    corpus_name,

                    customer,

                )

            except Exception as exc:

                knowledge = {

                    "status": "error",

                    "message": str(exc),

                }

        # -------------------------------------------------
        # Gemini Draft
        # -------------------------------------------------

        draft = self.gemini.generate_followup(

            customer=customer,

            previous_email=previous_email,

        )

        subject = "Follow-up"

        body = draft

        lines = draft.splitlines()

        for i, line in enumerate(lines):

            if line.lower().startswith("subject:"):

                subject = line.replace(
                    "Subject:",
                    "",
                ).strip()

                body = "\n".join(

                    lines[i + 1:]

                ).strip()

                break

        # -------------------------------------------------
        # Gmail Send
        # -------------------------------------------------

        gmail = self.gmail.send(

            recipient=customer_email,

            subject=subject,

            message=body,

        )

        # -------------------------------------------------
        # Firestore Email Log
        # -------------------------------------------------

        self.firestore.log_email(

            deal_id="FOLLOWUP",

            recipient=customer_email,

            subject=subject,

            email_type="FOLLOWUP",

        )

        # -------------------------------------------------
        # CRM Update
        # -------------------------------------------------

        crm_update = self.crm.update_status(

            customer,

            "FOLLOWUP_SENT",

        )

        self.crm.update_activity(

            customer,

            "Follow-up email sent",

        )

        self.crm.add_note(

            customer,

            f"Follow-up email sent to {customer_email}",

        )

        # -------------------------------------------------
        # Result
        # -------------------------------------------------

        return {

            "status": "success",

            "customer": customer,

            "customer_email": customer_email,

            "crm": crm_context,

            "knowledge": knowledge,

            "proposal": proposal,

            "previous_email": previous_email,

            "subject": subject,

            "draft": body,

            "gmail": gmail,

            "crm_update": crm_update,

        }

"""
Gemini Service

Business layer for Gemini proposal generation.
"""

from __future__ import annotations

from tools.google.gemini_tool import generate_text

try:
    from agents.sales_iq.dealdesk_agent_v2.config import (
        GOOGLE_CLOUD_LOCATION,
        GOOGLE_CLOUD_PROJECT,
        GOOGLE_GENAI_USE_VERTEXAI,
        MODEL_NAME,
    )
    from agents.sales_iq.dealdesk_agent_v2.prompts import (
        APPROVAL_PROMPT,
        CUSTOMER_EMAIL_PROMPT,
        EXECUTIVE_SUMMARY_PROMPT,
        INTERNAL_NOTE_PROMPT,
        NO_NEGOTIATION_PROMPT,
        PROPOSAL_PROMPT,
        YES_DEAL_PROMPT,
    )
except ImportError:
    from config import (
        GOOGLE_CLOUD_LOCATION,
        GOOGLE_CLOUD_PROJECT,
        GOOGLE_GENAI_USE_VERTEXAI,
        MODEL_NAME,
    )
    from prompts import (
        APPROVAL_PROMPT,
        CUSTOMER_EMAIL_PROMPT,
        EXECUTIVE_SUMMARY_PROMPT,
        INTERNAL_NOTE_PROMPT,
        NO_NEGOTIATION_PROMPT,
        PROPOSAL_PROMPT,
        YES_DEAL_PROMPT,
    )


class GeminiService:
    def _generate(self, prompt: str) -> str:
        return generate_text(
            prompt,
            model=MODEL_NAME,
            project=GOOGLE_CLOUD_PROJECT,
            location=GOOGLE_CLOUD_LOCATION,
            vertexai=GOOGLE_GENAI_USE_VERTEXAI,
        )

    def generate_proposal(
        self,
        customer: str,
        crm: dict,
        quote: dict,
        catalog: dict,
        drive_documents: dict,
        rag_context: dict | None = None,
    ):
        prompt = PROPOSAL_PROMPT.format(
            customer=customer,
            crm=crm,
            catalog=catalog,
            quote=quote,
            documents=drive_documents,
            knowledge=rag_context,
        )
        return self._generate(prompt)

    def executive_summary(self, customer: str, proposal: str):
        prompt = EXECUTIVE_SUMMARY_PROMPT.format(
            customer=customer,
            proposal=proposal,
        )
        return self._generate(prompt)

    def approval_note(self, quote: dict, approval: dict):
        prompt = APPROVAL_PROMPT.format(
            quote=quote,
            approval=approval,
            customer_reason=approval.get("customer_reason", ""),
        )
        return self._generate(prompt)

    def customer_email(self, customer: str, proposal: str):
        prompt = CUSTOMER_EMAIL_PROMPT.format(
            customer=customer,
            proposal=proposal,
        )
        return self._generate(prompt)

    def internal_note(self, proposal: str):
        prompt = INTERNAL_NOTE_PROMPT.format(
            proposal=proposal,
        )
        return self._generate(prompt)

    def deal_completed_message(self, customer: str, proposal: str):
        prompt = YES_DEAL_PROMPT.format(
            customer=customer,
            proposal=proposal,
        )
        return self._generate(prompt)

    def negotiation_message(
        self,
        customer_message: str,
        attempts: int,
        customer_reason: str = "",
    ):
        prompt = NO_NEGOTIATION_PROMPT.format(
            customer_message=customer_message,
            attempts=attempts,
            customer_reason=customer_reason,
        )
        return self._generate(prompt)

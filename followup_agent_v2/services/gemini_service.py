"""
Gemini Service

Generates enterprise follow-up emails using Gemini.
"""

from __future__ import annotations

from tools.google.gemini_tool import generate_text

try:
    from agents.sales_iq.followup_agent_v2.config import (
        GEMINI_API_KEY,
        GOOGLE_CLOUD_LOCATION,
        GOOGLE_CLOUD_PROJECT,
        GOOGLE_GENAI_USE_VERTEXAI,
        MODEL_NAME,
    )
except ImportError:
    from config import (
        GEMINI_API_KEY,
        GOOGLE_CLOUD_LOCATION,
        GOOGLE_CLOUD_PROJECT,
        GOOGLE_GENAI_USE_VERTEXAI,
        MODEL_NAME,
    )


class GeminiService:
    def build_prompt(self, customer: str, previous_email: str) -> str:
        return f"""
You are an Enterprise Sales Follow-up Assistant.

Customer:
{customer}

Previous Conversation:
{previous_email}

Write a professional business follow-up email.

Requirements:
- Friendly and professional.
- Mention previous discussion naturally.
- Encourage the customer to respond.
- Keep it concise.
- End with a clear call-to-action.

Return ONLY in this format:

Subject:
<email subject>

Body:
<email body>
"""

    def generate_followup(self, customer: str, previous_email: str) -> str:
        return generate_text(
            self.build_prompt(customer, previous_email),
            model=MODEL_NAME,
            project=GOOGLE_CLOUD_PROJECT,
            location=GOOGLE_CLOUD_LOCATION,
            vertexai=GOOGLE_GENAI_USE_VERTEXAI,
            api_key=GEMINI_API_KEY,
        )

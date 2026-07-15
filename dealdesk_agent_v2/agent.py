"""
DealDesk Agent V2

Google ADK Agent
"""

from __future__ import annotations

from google.adk.agents import Agent

try:
    from .workflow import DealDeskWorkflow
except ImportError:
    from workflow import DealDeskWorkflow

workflow = DealDeskWorkflow()


# ---------------------------------------------------------
# Execute Tool
# ---------------------------------------------------------

def execute_dealdesk(

    customer: str,

    product: str,

    quantity: int,

    discount: float = 0,

    tax: float = 18,

    corpus_name: str | None = None,

    customer_reason: str = "",

    negotiation_attempt: int = 1,

):
    """
    Execute DealDesk Workflow.
    """

    return workflow.execute(

        customer=customer,

        product=product,

        quantity=quantity,

        discount=discount,

        tax=tax,

        corpus_name=corpus_name,

        customer_reason=customer_reason,

        negotiation_attempt=negotiation_attempt,

    )


# ---------------------------------------------------------
# Root Agent
# ---------------------------------------------------------

root_agent = Agent(

    name="dealdesk_agent_v2",

    model="gemini-2.5-flash",

    description=(

        "Enterprise DealDesk Agent for commercial approvals, "

        "proposal generation, pricing validation, "

        "and enterprise deal processing."

    ),

    instruction="""
You are Stratova's Enterprise DealDesk AI Agent.

Responsibilities:

• Retrieve customer information from Firestore.
• Retrieve product information from Firestore.
• Generate quotations.
• Generate enterprise proposals.
• Generate executive summaries.
• Retrieve enterprise documents.
• Retrieve enterprise knowledge from Vertex AI RAG.
• Prepare approval notes.
• Update CRM.
• Trigger Follow-up workflow when required.

Commercial Policy:

• Never offer discounts proactively.
• Do NOT negotiate pricing.
• If the customer requests a discount, politely decline initially.
• Only after repeated business justification should the request be forwarded for internal approval.
• Never approve more than 5%.
• Final approval is performed by the business approval workflow, not by the AI.

Always maintain a professional enterprise tone.

Never fabricate prices, customers, products or approvals.

Always use Firestore as the source of truth.

""",

    tools=[

        execute_dealdesk,

    ],

)

"""
Follow-up Agent Tool Registry
"""

from __future__ import annotations

from typing import Callable

try:
    from agents.sales_iq.followup_agent_v2.workflow import FollowupWorkflow
except ImportError:
    from workflow import FollowupWorkflow

# ---------------------------------------------------------
# Workflow
# ---------------------------------------------------------

workflow = FollowupWorkflow()


# ---------------------------------------------------------
# Tool
# ---------------------------------------------------------

def execute_followup(

    customer: str,

    customer_email: str,

    corpus_name: str = "",

):

    """
    Execute the complete Follow-up workflow.

    Args:
        customer: Customer name.
        customer_email: Customer email address.
        corpus_name: Optional Vertex AI RAG corpus.

    Returns:
        Complete workflow execution result.
    """

    return workflow.execute(

        customer=customer,

        customer_email=customer_email,

        corpus_name=corpus_name if corpus_name else None,

    )


# ---------------------------------------------------------
# Registry
# ---------------------------------------------------------

def get_all_tools() -> list[Callable]:

    return [

        execute_followup,

    ]

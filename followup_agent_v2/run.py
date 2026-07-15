"""
Run Follow-up Agent

Local test runner.
"""

from __future__ import annotations

from agents.sales_iq.followup_agent_v2.workflow import (
    FollowupWorkflow,
)


def main():

    workflow = FollowupWorkflow()

    customer = input("Customer Name : ").strip()

    customer_email = input("Customer Email: ").strip()

    corpus = input(
        "Vertex RAG Corpus (Optional): "
    ).strip()

    if corpus == "":
        corpus = None

    result = workflow.execute(

        customer=customer,

        customer_email=customer_email,

        corpus_name=corpus,

    )

    print()

    print("=" * 80)

    print("FINAL RESULT")

    print("=" * 80)

    print(result)


if __name__ == "__main__":

    main()
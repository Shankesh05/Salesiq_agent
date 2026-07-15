"""
Run DealDesk Agent
"""

from __future__ import annotations

from pprint import pprint

from .workflow import DealDeskWorkflow


def main():

    workflow = DealDeskWorkflow()

    print("=" * 70)
    print("STRATOVA DEALDESK AGENT")
    print("=" * 70)

    customer = input(

        "Customer ID : "

    ).strip()

    product = input(

        "Product : "

    ).strip()

    quantity = int(

        input(

            "Quantity : "

        )

    )

    discount = float(

        input(

            "Requested Discount (%) [Default 0] : "

        ) or "0"

    )

    tax = float(

        input(

            "Tax (%) [Default 18] : "

        ) or "18"

    )

    customer_reason = input(

        "Business Justification (Optional): "

    ).strip()

    negotiation_attempt = int(

        input(

            "Negotiation Attempt [Default 1] : "

        ) or "1"

    )

    corpus = input(

        "Vertex AI RAG Corpus (Optional): "

    ).strip()

    if corpus == "":

        corpus = None

    print()

    print("=" * 70)
    print("PROCESSING...")
    print("=" * 70)

    result = workflow.execute(

        customer=customer,

        product=product,

        quantity=quantity,

        discount=discount,

        tax=tax,

        corpus_name=corpus,

        customer_reason=customer_reason,

        negotiation_attempt=negotiation_attempt,

    )

    print()

    print("=" * 70)
    print("FINAL RESULT")
    print("=" * 70)

    pprint(result)

    print()

    followup = result.get(

        "followup",

    )

    if followup:

        print("=" * 70)
        print("FOLLOW-UP")
        print("=" * 70)

        print(

            "Required :", followup.get("required")

        )

        print(

            "Reason   :", followup.get("reason")

        )


if __name__ == "__main__":

    main()
"""
DealDesk Workflow

Coordinates DealDesk execution.
"""

from __future__ import annotations

try:
    from .services.dealdesk_service import (
        DealDeskService,
    )
except ImportError:
    from services.dealdesk_service import (
        DealDeskService,
    )


class DealDeskWorkflow:

    def __init__(self):

        self.dealdesk = DealDeskService()

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------

    def execute(

        self,

        customer: str,

        product: str,

        quantity: int,

        discount: float = 0,

        tax: float = 18,

        corpus_name: str | None = None,

        customer_reason: str = "",

        negotiation_attempt: int = 1,

    ):

        print("=" * 70)
        print("DEALDESK AUTOMATION WORKFLOW")
        print("=" * 70)

        try:

            result = self.dealdesk.execute(

                customer=customer,

                product=product,

                quantity=quantity,

                discount_percent=discount,

                tax_percent=tax,

                corpus_name=corpus_name,

                customer_reason=customer_reason,

                negotiation_attempt=negotiation_attempt,

            )

            status = {

                "status": "success",

                "reason": None,

                "data": result,

            }

        except Exception as exc:

            status = {

                "status": "failed",

                "reason": str(exc),

                "data": None,

            }

        print("\n" + "=" * 70)
        print("WORKFLOW SUMMARY")
        print("=" * 70)

        print(

            "DealDesk Status :",

            status["status"],

        )

        if status["reason"]:

            print(

                "Reason :",

                status["reason"],

            )

        followup = None

        if (

            status["status"] == "success"

            and status["data"]

        ):

            followup = status["data"].get(

                "followup",

                None,

            )

            if followup:

                print(

                    "Follow-up Required :",

                    followup["required"],

                )

                print(

                    "Reason :",

                    followup["reason"],

                )

        print("\nWorkflow Completed.")
        print("=" * 70)

        return {

            "customer": customer,

            "workflow": {

                "dealdesk": status,

            },

            "followup": followup,

            "result": status["data"],

        }

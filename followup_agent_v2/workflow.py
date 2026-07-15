"""
Follow-up Workflow

Enterprise Follow-up Automation Workflow.
"""

from __future__ import annotations

try:
    from agents.sales_iq.followup_agent_v2.services.followup_service import (
        FollowupService,
    )
except ImportError:
    from services.followup_service import (
        FollowupService,
    )


class FollowupWorkflow:

    def __init__(self):

        self.followup = FollowupService()

    # ---------------------------------------------------------
    # Safe Step Runner
    # ---------------------------------------------------------

    def _run_step(self, func, *args, **kwargs):

        try:

            result = func(*args, **kwargs)

            return {

                "status": "success",

                "reason": None,

                "data": result,

            }

        except Exception as exc:

            return {

                "status": "failed",

                "reason": str(exc),

                "data": None,

            }

    # ---------------------------------------------------------
    # Execute Workflow
    # ---------------------------------------------------------

    def execute(

        self,

        customer: str,

        customer_email: str,

        corpus_name: str | None = None,

    ):

        print("=" * 70)
        print("FOLLOW-UP AUTOMATION WORKFLOW")
        print("=" * 70)

        workflow = {}

        # -----------------------------------------------------
        # Step 1
        # -----------------------------------------------------

        print("\n[1/6] Customer Follow-up")

        workflow["followup"] = self._run_step(

            self.followup.execute,

            customer,

            customer_email,

            corpus_name,

        )

        print(

            "Status :",

            workflow["followup"]["status"],

        )

        # -----------------------------------------------------
        # Summary
        # -----------------------------------------------------

        print("\n" + "=" * 70)
        print("WORKFLOW SUMMARY")
        print("=" * 70)

        for step, info in workflow.items():

            print()

            print(step.upper())

            print(

                "Status :",

                info["status"],

            )

            if info["reason"]:

                print(

                    "Reason :",

                    info["reason"],

                )

        print("\nWorkflow Completed.")

        print("=" * 70)

        return {

            "customer": customer,

            "customer_email": customer_email,

            "workflow": workflow,

            "result": workflow["followup"]["data"],

        }

"""
Approval Service

Business layer for DealDesk approval workflow.
"""

from __future__ import annotations

from tools.sales.approval_tool import (
    approval_level,
    validate_discount,
    create_request,
    approve,
    reject,
    approval_history,
    approval_summary,
    negotiation_response,
)


class ApprovalService:

    # ---------------------------------------------------------
    # Approval Level
    # ---------------------------------------------------------

    def level(

        self,

        discount_percent: float,

    ):

        return approval_level(

            discount_percent,

        )

    # ---------------------------------------------------------
    # Validate Discount
    # ---------------------------------------------------------

    def validate(

        self,

        discount_percent: float,

    ):

        return validate_discount(

            discount_percent,

        )

    # ---------------------------------------------------------
    # Create Approval Request
    # ---------------------------------------------------------

    def create(

        self,

        customer: str,

        deal_id: str,

        discount_percent: float,

        amount: float,

        customer_reason: str = "",

    ):

        return create_request(

            customer,

            deal_id,

            discount_percent,

            amount,

            customer_reason,

        )

    # ---------------------------------------------------------
    # Approve
    # ---------------------------------------------------------

    def approve(

        self,

        approval_id: str,

        approver: str,

    ):

        return approve(

            approval_id,

            approver,

        )

    # ---------------------------------------------------------
    # Reject
    # ---------------------------------------------------------

    def reject(

        self,

        approval_id: str,

        approver: str,

        reason: str,

    ):

        return reject(

            approval_id,

            approver,

            reason,

        )

    # ---------------------------------------------------------
    # History
    # ---------------------------------------------------------

    def history(

        self,

        deal_id: str,

    ):

        return approval_history(

            deal_id,

        )

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(

        self,

        customer: str,

        deal_id: str,

        discount_percent: float,

        amount: float,

        customer_reason: str = "",

    ):

        return approval_summary(

            customer,

            deal_id,

            discount_percent,

            amount,

            customer_reason,

        )

    # ---------------------------------------------------------
    # Negotiation Response
    # ---------------------------------------------------------

    def negotiate(

        self,

        attempts: int,

        customer_reason: str = "",

    ):

        return negotiation_response(

            attempts,

            customer_reason,

        )
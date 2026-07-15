"""
CRM Service

Business layer for CRM operations.
"""

from __future__ import annotations

from tools.sales.crm_tool import (
    get_customer,
    get_contact,
    get_pipeline,
    get_deals,
    get_last_activity,
    update_followup_status,
    get_notes,
    get_customer_context,
    add_note,
    update_last_activity,
    update_pipeline,
)


class CRMService:

    # ---------------------------------------------------------
    # Customer
    # ---------------------------------------------------------

    def customer(
        self,
        customer: str,
    ):
        return get_customer(customer)

    # ---------------------------------------------------------
    # Contact
    # ---------------------------------------------------------

    def contact(
        self,
        customer: str,
    ):
        return get_contact(customer)

    # ---------------------------------------------------------
    # Pipeline
    # ---------------------------------------------------------

    def pipeline(
        self,
        customer: str,
    ):
        return get_pipeline(customer)

    # ---------------------------------------------------------
    # Deals
    # ---------------------------------------------------------

    def deals(
        self,
        customer: str,
    ):
        return get_deals(customer)

    # ---------------------------------------------------------
    # Last Activity
    # ---------------------------------------------------------

    def last_activity(
        self,
        customer: str,
    ):
        return get_last_activity(customer)

    # ---------------------------------------------------------
    # Notes
    # ---------------------------------------------------------

    def notes(
        self,
        customer: str,
    ):
        return get_notes(customer)

    # ---------------------------------------------------------
    # Add Note
    # ---------------------------------------------------------

    def add_note(
        self,
        customer: str,
        note: str,
    ):
        return add_note(
            customer,
            note,
        )

    # ---------------------------------------------------------
    # Update Activity
    # ---------------------------------------------------------

    def update_activity(
        self,
        customer: str,
        activity: str,
    ):
        return update_last_activity(
            customer,
            activity,
        )

    # ---------------------------------------------------------
    # Update Pipeline
    # ---------------------------------------------------------

    def update_pipeline(
        self,
        customer: str,
        pipeline: dict,
    ):
        return update_pipeline(
            customer,
            pipeline,
        )

    # ---------------------------------------------------------
    # Update Follow-up Status
    # ---------------------------------------------------------

    def update_status(
        self,
        customer: str,
        status: str,
    ):
        return update_followup_status(
            customer,
            status,
        )

    # ---------------------------------------------------------
    # Complete Customer Context
    # ---------------------------------------------------------

    def customer_context(
        self,
        customer: str,
    ):
        return get_customer_context(customer)
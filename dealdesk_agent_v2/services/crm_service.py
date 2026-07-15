"""
CRM Service

Business logic layer for DealDesk Agent.
"""

from __future__ import annotations

from tools.sales.crm_tool import (
    customer_context,
    get_customer,
    get_primary_contact,
    get_open_deals,
    get_opportunity,
    get_notes,
    get_last_activity,
    update_deal_status,
    add_note,
    update_last_activity,
    update_opportunity,
)


class CRMService:

    # ---------------------------------------------------------
    # Customer
    # ---------------------------------------------------------

    def customer(

        self,

        customer_id: str,

    ):

        return get_customer(

            customer_id,

        )

    # ---------------------------------------------------------
    # Contact
    # ---------------------------------------------------------

    def contact(

        self,

        customer_id: str,

    ):

        return get_primary_contact(

            customer_id,

        )

    # ---------------------------------------------------------
    # Deals
    # ---------------------------------------------------------

    def deals(

        self,

        customer_id: str,

    ):

        return get_open_deals(

            customer_id,

        )

    # ---------------------------------------------------------
    # Opportunity
    # ---------------------------------------------------------

    def opportunity(

        self,

        customer_id: str,

    ):

        return get_opportunity(

            customer_id,

        )

    # ---------------------------------------------------------
    # Notes
    # ---------------------------------------------------------

    def notes(

        self,

        customer_id: str,

    ):

        return get_notes(

            customer_id,

        )

    # ---------------------------------------------------------
    # Last Activity
    # ---------------------------------------------------------

    def last_activity(

        self,

        customer_id: str,

    ):

        return get_last_activity(

            customer_id,

        )

    # ---------------------------------------------------------
    # Complete CRM Context
    # ---------------------------------------------------------

    def customer_context(

        self,

        customer_id: str,

    ):

        return customer_context(

            customer_id,

        )

    # ---------------------------------------------------------
    # Update Deal Status
    # ---------------------------------------------------------

    def update_status(

        self,

        deal_id: str,

        status: str,

    ):

        return update_deal_status(

            deal_id,

            status,

        )

    # ---------------------------------------------------------
    # Add Note
    # ---------------------------------------------------------

    def add_note(

        self,

        customer_id: str,

        note: str,

    ):

        return add_note(

            customer_id,

            note,

        )

    # ---------------------------------------------------------
    # Update Activity
    # ---------------------------------------------------------

    def update_activity(

        self,

        customer_id: str,

        activity: str,

    ):

        return update_last_activity(

            customer_id,

            activity,

        )

    # ---------------------------------------------------------
    # Update Opportunity
    # ---------------------------------------------------------

    def update_pipeline(

        self,

        customer_id: str,

        opportunity: dict,

    ):

        return update_opportunity(

            customer_id,

            opportunity,

        )
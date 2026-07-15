"""
Outlook Service

Business layer for Outlook integration.
(Currently uses SMTP for sending.)
"""

from __future__ import annotations

from tools.sales.outlook_tool import (
    send_email,
)


class OutlookService:

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Search Latest Email
    # ---------------------------------------------------------

    def search_latest_email(
        self,
        customer: str,
    ):

        # SMTP cannot search inbox.
        return None

    # ---------------------------------------------------------
    # Read Email
    # ---------------------------------------------------------

    def read_email(
        self,
        message_id: str,
    ):

        # SMTP cannot read inbox.
        return None

    # ---------------------------------------------------------
    # Latest Conversation
    # ---------------------------------------------------------

    def get_latest_conversation(
        self,
        customer: str,
    ):

        message_id = self.search_latest_email(
            customer,
        )

        if not message_id:

            return None

        body = self.read_email(
            message_id,
        )

        return {
            "id": message_id,
            "body": body,
        }

    # ---------------------------------------------------------
    # Send Email
    # ---------------------------------------------------------

    def send(
        self,
        recipient: str,
        subject: str,
        message: str,
    ):

        return send_email(
            recipient=recipient,
            subject=subject,
            body=message,
        )

    # ---------------------------------------------------------
    # Health Check
    # ---------------------------------------------------------

    def health(self):

        return {
            "provider": "Outlook SMTP",
            "search": False,
            "read": False,
            "send": True,
            "status": "ready",
        }
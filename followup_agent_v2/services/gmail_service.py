"""
Gmail Service

Business layer for Gmail operations.
"""

from __future__ import annotations

from tools.google.gmail_tool import (
    search_latest_email,
    read_email,
    send_email,
)


class GmailService:

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Search latest customer conversation
    # ---------------------------------------------------------

    def get_latest_conversation(
        self,
        customer: str,
    ):

        message_id = search_latest_email(
            f"{customer} newer_than:365d"
        )

        if not message_id:

            return None

        return {

            "message_id": message_id,

            "body": read_email(message_id),

        }

    # ---------------------------------------------------------
    # Send Follow-up
    # ---------------------------------------------------------

    def send_followup(

        self,

        recipient: str,

        subject: str,

        body: str,

    ):

        return send_email(

            recipient,

            subject,

            body,

        )

    # ---------------------------------------------------------
    # Generic Send
    # ---------------------------------------------------------

    def send(

        self,

        recipient: str,

        subject: str,

        message: str,

    ):

        return send_email(

            recipient,

            subject,

            message,

        )

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(

        self,

        query: str,

    ):

        return search_latest_email(query)

    # ---------------------------------------------------------
    # Read
    # ---------------------------------------------------------

    def read(

        self,

        message_id: str,

    ):

        return read_email(message_id)
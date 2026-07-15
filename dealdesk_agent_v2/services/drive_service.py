"""
Drive Service

Business layer for Google Drive.
"""

from __future__ import annotations

from tools.google.gdrive_tool import (
    search_proposals,
    search_contracts,
    search_quotes,
    search,
)


class DriveService:

    # ---------------------------------------------------------
    # Proposal Documents
    # ---------------------------------------------------------

    def proposals(

        self,

        customer: str,

    ):

        return search_proposals(

            customer,

        )

    # ---------------------------------------------------------
    # Contracts
    # ---------------------------------------------------------

    def contracts(

        self,

        customer: str,

    ):

        return search_contracts(

            customer,

        )

    # ---------------------------------------------------------
    # Quotations
    # ---------------------------------------------------------

    def quotations(

        self,

        customer: str,

    ):

        return search_quotes(

            customer,

        )

    # ---------------------------------------------------------
    # Customer Documents
    # ---------------------------------------------------------

    def customer_documents(

        self,

        customer: str,

    ):

        return {

            "proposals": self.proposals(

                customer,

            ),

            "contracts": self.contracts(

                customer,

            ),

            "quotations": self.quotations(

                customer,

            ),

        }

    # ---------------------------------------------------------
    # Generic Search
    # ---------------------------------------------------------

    def search(

        self,

        keyword: str,

    ):

        return search(

            keyword,

        )
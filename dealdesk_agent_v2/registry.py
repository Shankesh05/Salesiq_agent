"""
Registry

Registers all services used by DealDesk Agent.
"""

from __future__ import annotations

from tools.sales.firestore_service import (
    FirestoreService,
)

from .services.crm_service import (
    CRMService,
)

from .services.catalog_service import (
    CatalogService,
)

from .services.pricing_service import (
    PricingService,
)

from .services.approval_service import (
    ApprovalService,
)

from .services.drive_service import (
    DriveService,
)

from .services.rag_service import (
    RAGService,
)

from .services.gemini_service import (
    GeminiService,
)

from .services.dealdesk_service import (
    DealDeskService,
)


class ServiceRegistry:

    def __init__(self):

        self.firestore = FirestoreService()

        self.crm = CRMService()

        self.catalog = CatalogService()

        self.pricing = PricingService()

        self.approval = ApprovalService()

        self.drive = DriveService()

        self.rag = RAGService()

        self.gemini = GeminiService()

        self.dealdesk = DealDeskService()

    # ---------------------------------------------------------
    # Dictionary
    # ---------------------------------------------------------

    def services(self):

        return {

            "firestore": self.firestore,

            "crm": self.crm,

            "catalog": self.catalog,

            "pricing": self.pricing,

            "approval": self.approval,

            "drive": self.drive,

            "rag": self.rag,

            "gemini": self.gemini,

            "dealdesk": self.dealdesk,

        }

    # ---------------------------------------------------------
    # Lookup
    # ---------------------------------------------------------

    def get(

        self,

        name: str,

    ):

        return self.services().get(

            name.lower(),

        )
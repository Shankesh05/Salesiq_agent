from __future__ import annotations

import importlib
import sys
import types
import unittest
from unittest.mock import Mock, patch


def _install_external_stubs() -> None:
    dotenv = types.ModuleType("dotenv")
    dotenv.load_dotenv = lambda *args, **kwargs: None
    dotenv.set_key = lambda *args, **kwargs: None
    sys.modules.setdefault("dotenv", dotenv)

    firestore = types.ModuleType("google.cloud.firestore")
    firestore.Client = lambda *args, **kwargs: object()

    google = sys.modules.setdefault("google", types.ModuleType("google"))
    google.__path__ = getattr(google, "__path__", [])

    cloud = sys.modules.setdefault("google.cloud", types.ModuleType("google.cloud"))
    cloud.__path__ = getattr(cloud, "__path__", [])
    cloud.firestore = firestore
    sys.modules["google.cloud.firestore"] = firestore


class TestSalesIQRefactor(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _install_external_stubs()

    def test_dealdesk_service_executes_all_mocked_steps(self) -> None:
        module = importlib.import_module(
            "agents.sales_iq.dealdesk_agent_v2.services.dealdesk_service"
        )

        crm = Mock()
        crm.customer_context.return_value = {"customer_id": "acme"}
        crm.update_status.return_value = {"updated": True}
        crm.add_note.return_value = ["note"]
        crm.update_activity.return_value = {"activity": "Proposal Generated"}

        catalog = Mock()
        catalog.product.return_value = {
            "sku": "SKU-1",
            "name": "Platform",
            "price": 100.0,
            "currency": "USD",
        }

        pricing = Mock()
        pricing.valid_quantity.return_value = True
        pricing.generate.return_value = {
            "quote_id": "QT-1",
            "final_price": 118.0,
            "product": "Platform",
        }

        approval = Mock()
        approval.summary.return_value = {"status": "NO_APPROVAL_REQUIRED"}

        drive = Mock()
        drive.customer_documents.return_value = {
            "proposals": [],
            "contracts": [],
            "quotations": [],
        }

        rag = Mock()
        rag.knowledge_context.return_value = {"customer": ["context"]}

        gemini = Mock()
        gemini.generate_proposal.return_value = "proposal"
        gemini.executive_summary.return_value = "summary"
        gemini.approval_note.return_value = "approval note"
        gemini.customer_email.return_value = "customer email"
        gemini.internal_note.return_value = "internal note"
        gemini.deal_completed_message.return_value = "deal completed"

        with (
            patch.object(module, "CRMService", return_value=crm),
            patch.object(module, "CatalogService", return_value=catalog),
            patch.object(module, "PricingService", return_value=pricing),
            patch.object(module, "ApprovalService", return_value=approval),
            patch.object(module, "DriveService", return_value=drive),
            patch.object(module, "RAGService", return_value=rag),
            patch.object(module, "GeminiService", return_value=gemini),
        ):
            result = module.DealDeskService().execute(
                customer="acme",
                product="Platform",
                quantity=2,
                corpus_name="corpus",
            )

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["quote"]["quote_id"], "QT-1")
        self.assertEqual(result["proposal"], "proposal")
        self.assertEqual(result["executive_summary"], "summary")
        self.assertEqual(result["customer_email"], "customer email")
        self.assertEqual(result["deal_completed_message"], "deal completed")
        self.assertTrue(result["followup"]["required"])
        crm.customer_context.assert_called_once_with("acme")
        catalog.product.assert_called_once_with("Platform")
        pricing.generate.assert_called_once()
        approval.summary.assert_called_once()
        drive.customer_documents.assert_called_once_with("acme")
        rag.knowledge_context.assert_called_once_with("corpus", "acme", "Platform")
        crm.update_status.assert_called_once_with("QT-1", "PROPOSAL_GENERATED")

    def test_followup_service_executes_all_mocked_steps(self) -> None:
        module = importlib.import_module(
            "agents.sales_iq.followup_agent_v2.services.followup_service"
        )

        gmail = Mock()
        gmail.get_latest_conversation.return_value = {
            "message_id": "msg-1",
            "body": "Previous discussion",
        }
        gmail.send.return_value = {"status": "sent"}

        drive = Mock()
        drive.find_document.return_value = {"id": "doc-1", "name": "Proposal"}

        crm = Mock()
        crm.customer_context.return_value = {"customer_id": "acme"}
        crm.update_status.return_value = {"status": "FOLLOWUP_SENT"}

        rag = Mock()
        rag.customer_context.return_value = {"history": ["context"]}

        gemini = Mock()
        gemini.generate_followup.return_value = "Subject: Next steps\nBody:\nHello"

        firestore = Mock()

        with (
            patch.object(module, "GmailService", return_value=gmail),
            patch.object(module, "DriveService", return_value=drive),
            patch.object(module, "CRMService", return_value=crm),
            patch.object(module, "RAGService", return_value=rag),
            patch.object(module, "GeminiService", return_value=gemini),
            patch.object(module, "FirestoreService", return_value=firestore),
        ):
            result = module.FollowupService().execute(
                customer="acme",
                customer_email="buyer@example.com",
                corpus_name="corpus",
            )

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["subject"], "Next steps")
        self.assertIn("Hello", result["draft"])
        crm.customer_context.assert_called_once_with("acme")
        gmail.get_latest_conversation.assert_called_once_with("acme")
        drive.find_document.assert_called_once_with("acme")
        rag.customer_context.assert_called_once_with("corpus", "acme")
        gemini.generate_followup.assert_called_once_with(
            customer="acme",
            previous_email="Previous discussion",
        )
        gmail.send.assert_called_once_with(
            recipient="buyer@example.com",
            subject="Next steps",
            message="Body:\nHello",
        )
        firestore.log_email.assert_called_once()
        crm.update_status.assert_called_once_with("acme", "FOLLOWUP_SENT")

    def test_pricing_calculation_uses_sales_catalog_tool(self) -> None:
        pricing_tool = importlib.import_module("tools.sales.pricing_tool")

        product = {
            "sku": "SKU-1",
            "name": "Platform",
            "price": 100.0,
            "currency": "USD",
        }

        with patch.object(pricing_tool, "get_product", return_value=product):
            quote = pricing_tool.generate_quote(
                customer="acme",
                product_name="Platform",
                quantity=2,
                discount_percent=5,
                tax_percent=10,
            )

        self.assertEqual(quote["base_price"], 200.0)
        self.assertEqual(quote["discount_amount"], 10.0)
        self.assertEqual(quote["final_price"], 209.0)

    def test_approval_workflow_uses_sales_firestore_layer(self) -> None:
        approval_tool = importlib.import_module("tools.sales.approval_tool")

        fake_firestore = Mock()
        fake_firestore._get.return_value = {"status": "APPROVED"}

        with patch.object(approval_tool, "firestore", fake_firestore):
            request = approval_tool.create_request(
                customer="acme",
                deal_id="deal-1",
                discount_percent=5,
                amount=100,
            )
            approved = approval_tool.approve("approval-1", "manager@example.com")

        self.assertEqual(request["approval_level"], "SALES_MANAGER")
        fake_firestore._set.assert_called_once()
        fake_firestore._update.assert_called_once()
        self.assertEqual(approved["status"], "APPROVED")

    def test_negotiation_story_declines_then_escalates_with_reason(self) -> None:
        approval_tool = importlib.import_module("tools.sales.approval_tool")

        first = approval_tool.negotiation_response(
            attempts=1,
            customer_reason="",
        )
        repeated = approval_tool.negotiation_response(
            attempts=2,
            customer_reason="Need a discount",
        )
        escalated = approval_tool.negotiation_response(
            attempts=4,
            customer_reason="Budget approval depends on a 5% concession.",
        )

        self.assertEqual(first["status"], "DECLINED")
        self.assertIn("unable to provide a discount", first["message"])
        self.assertEqual(repeated["status"], "DECLINED")
        self.assertIn("cannot bypass", repeated["message"])
        self.assertEqual(escalated["status"], "SEND_FOR_APPROVAL")
        self.assertIn("higher authorities", escalated["message"])
        self.assertIn("not guaranteed", escalated["message"])


if __name__ == "__main__":
    unittest.main()

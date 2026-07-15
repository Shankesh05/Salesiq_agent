DealDesk Agent V2

Overview

DealDesk Agent V2 is an enterprise sales automation agent built using Google Agent Development Kit (ADK). It automates the commercial proposal workflow by integrating CRM retrieval, product catalog lookup, pricing, quotation generation, approval workflow, Google Drive document retrieval, optional Vertex AI RAG knowledge retrieval, and Gemini-powered proposal generation.

«Note: This project is developed for demonstration and learning purposes. CRM records, product catalog, customer information, and proposal documents currently use sample/mock data.»

---

Features

- CRM customer lookup (sample CRM data)
- Enterprise product catalog
- Dynamic pricing engine
- Discount and tax calculation
- Professional quotation generation
- Approval workflow generation
- Google Drive proposal retrieval
- Optional Vertex AI RAG integration
- Gemini-generated commercial proposals
- Executive summary generation
- Approval justification generation
- Customer-ready proposal email generation
- Google ADK Web UI support

---

Tech Stack

- Python 3.12
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Google Drive API
- Vertex AI RAG (Optional)
- Google OAuth
- Google Cloud Platform

---

Project Structure

dealdesk_agent_v2/
│
├── agent.py
├── workflow.py
├── run.py
├── config.py
├── prompts.py
├── registry.py
│
├── services/
│   ├── pricing_service.py
│   ├── gemini_service.py
│   └── ...
│
├── tools/
│   ├── crm_tool.py
│   ├── catalog_tool.py
│   ├── pricing_tool.py
│   ├── approval_tool.py
│   ├── drive_tool.py
│   └── rag_tool.py
│
└── config/

---

Setup

Create a ".env" file inside the "dealdesk_agent_v2" directory.

Example:

GOOGLE_GENAI_USE_VERTEXAI=True
GOOGLE_CLOUD_PROJECT=<your-project-id>
GOOGLE_CLOUD_LOCATION=us-central1
MODEL_NAME=gemini-2.5-flash

Authentication is handled using Google OAuth credentials.

---

Running

Command Line

python -m agents.sales_iq.dealdesk_agent_v2.run

Google ADK Web

cd agents/sales_iq
adk web

---

Workflow

1. Retrieve CRM information
2. Retrieve product catalog
3. Calculate pricing
4. Apply discounts and taxes
5. Generate quotation
6. Retrieve proposal documents from Google Drive
7. Retrieve enterprise knowledge (optional)
8. Generate commercial proposal
9. Generate executive summary
10. Generate approval justification
11. Generate customer email

---

Notes

- CRM data is currently mocked for demonstration.
- Product catalog contains sample enterprise products.
- Customer information (e.g., John Doe) is sample data.
- Google Drive documents are demonstration files.
- Vertex AI RAG integration is optional.
- No production customer information is included.

---

Author

Shankesh Raja

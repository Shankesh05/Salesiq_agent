DEPLOYMENT.md

DealDesk Agent V2 Deployment Guide

Prerequisites

- Python 3.12+
- Google Cloud Project
- Google ADK
- Vertex AI Enabled
- Google Drive API Enabled
- Google OAuth Credentials
- Required Python packages installed

---

Project Structure

dealdesk_agent_v2/
│
├── agent.py
├── workflow.py
├── run.py
├── config.py
├── .env
├── services/
├── tools/
├── config/
    └── credentials.json



---

Environment Variables

Create a ".env" file inside the "dealdesk_agent_v2" directory.

Example:

GOOGLE_GENAI_USE_VERTEXAI=True
GOOGLE_CLOUD_PROJECT=<your-project-id>
GOOGLE_CLOUD_LOCATION=us-central1

MODEL_NAME=gemini-2.5-flash

DEFAULT_DISCOUNT=5
DEFAULT_TAX=18
DEFAULT_CURRENCY=USD

---

Google Cloud Setup

Enable the following APIs:

- Vertex AI API
- Google Drive API
- OAuth Consent Screen

Download the OAuth credentials and place them in:

config/credentials.json

During the first execution, OAuth authentication will open in the browser. After successful authorization, the access token will be stored locally for future executions.

---

Running from Terminal

python -m agents.sales_iq.dealdesk_agent_v2.run

The application will prompt for:

- Customer Name
- Product
- Quantity
- Discount
- Tax
- Vertex AI RAG Corpus (Optional)

---

Running with Google ADK

Navigate to:

cd agents/sales_iq

Launch ADK:

adk web

Open:

http://127.0.0.1:8000

Select dealdesk_agent_v2 and interact with the agent through the ADK Web interface.

---

Deployment Workflow

1. User submits deal request.
2. CRM data is retrieved.
3. Product information is fetched.
4. Pricing is calculated.
5. Approval workflow is generated.
6. Proposal documents are retrieved from Google Drive.
7. Enterprise knowledge is retrieved from Vertex AI RAG (optional).
8. Gemini generates:
   - Commercial Proposal
   - Executive Summary
   - Approval Note
   - Customer Email
9. CRM status is updated.

---

Security Notes

- Do not commit ".env".
- Do not commit "credentials.json".
- Do not commit OAuth token files.
- Store secrets securely using environment variables or a secret manager.
- Restrict Google Cloud IAM permissions following the principle of least privilege.

---

Production Recommendations

- Replace mock CRM data with Salesforce, HubSpot, Microsoft Dynamics 365, or Zoho CRM.
- Replace the sample product catalog with a database-backed catalog.
- Store documents in an enterprise document management system.
- Secure secrets using Google Secret Manager.
- Enable centralized logging and monitoring.
- Containerize the application using Docker for cloud deployment.

---

Current Status

- CRM: Sample implementation
- Product Catalog: Sample implementation
- Pricing Engine: Implemented
- Approval Workflow: Implemented
- Google Drive Integration: Implemented
- Vertex AI RAG: Optional
- Gemini Proposal Generation: Implemented
- Google ADK Integration: Implemented
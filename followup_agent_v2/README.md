Follow-up Agent V2

Overview

Follow-up Agent V2 is an autonomous enterprise sales assistant built using Google Agent Development Kit (ADK). The agent automates the complete follow-up process by gathering customer information, retrieving previous conversations, searching enterprise documents, generating personalized follow-up emails using Gemini, sending emails through Gmail, and updating CRM records.

The solution demonstrates how multiple enterprise services can be orchestrated into a single AI-powered workflow.

---

Features

- Customer CRM lookup
- Gmail conversation search
- Previous email retrieval
- Google Drive document search
- Vertex AI RAG integration (optional)
- Gemini-powered follow-up email generation
- Automatic Gmail email sending
- CRM status update
- Modular service-oriented architecture
- Extensible support for multiple email providers

---

Workflow

Customer Input
      │
      ▼
CRM Service
      │
      ▼
Retrieve Customer Information
      │
      ▼
Search Previous Gmail Conversation
      │
      ▼
Search Google Drive Documents
      │
      ▼
Retrieve Enterprise Knowledge (Vertex AI RAG)
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Generate Follow-up Email
      │
      ▼
Send Email via Gmail
      │
      ▼
Update CRM Status

---

Project Structure

followup_agent_v2/

├── agent.py
├── workflow.py
├── run.py
├── registry.py
├── prompts.py
├── config.py
├── models.py
├── README.md
├── DESIGN.md
├── ARCHITECTURE.md
├── DEPLOYMENT.md
├── requirements.txt
│
├── config/
│   ├── credentials.json
│   └── token.json
│
├── services/
│   ├── gmail_service.py
│   ├── drive_service.py
│   ├── crm_service.py
│   ├── rag_service.py
│   ├── gemini_service.py
│   ├── followup_service.py
│   └── outlook_service.py
│
├── tools/
│   ├── gmail_tool.py
│   ├── drive_tool.py
│   ├── crm_tool.py
│   ├── rag_tool.py
│   └── outlook_tool.py
│
└── templates/

---

Technologies Used

- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Google Gmail API
- Google Drive API
- Vertex AI RAG
- Google Cloud Platform
- Python 3.12
- OAuth 2.0 Authentication

---

Installation

Clone the repository.

git clone <repository-url>

Install dependencies.

pip install -r requirements.txt

Configure Google Cloud credentials.

credentials.json

Authenticate Gmail and Drive.

token.json

---

Running the Agent

python -m agents.sales_iq.followup_agent_v2.run

or launch the ADK interface

adk web

---

Example Execution

Input

Customer Name : Google

Customer Email : contact@company.com

The agent performs:

- Retrieves CRM information
- Reads previous Gmail conversations
- Searches Google Drive proposals
- Retrieves enterprise knowledge (optional)
- Generates a professional follow-up email
- Sends the email through Gmail
- Updates CRM status

---

Supported Integrations

Current

- Gmail API
- Google Drive API
- Gemini API
- Vertex AI RAG
- CRM Service

Planned

- Microsoft Outlook
- Salesforce CRM
- HubSpot CRM
- Slack
- Microsoft Teams

---

Security

- OAuth 2.0 Authentication
- Google Cloud Credentials
- Environment Variable Configuration
- Modular Authentication Design

---

Future Enhancements

- Outlook (Microsoft Graph) Integration
- Calendar Scheduling
- Meeting Summary Generation
- Automated Proposal Generation
- Multi-agent Sales Pipeline
- Customer Sentiment Analysis
- Follow-up Recommendation Engine
- Enterprise CRM Connectors

---

Author

Shankesh Raja V

B.Tech Computer Science Engineering (Big Data Analytics)

AI Engineer | Google ADK | Vertex AI | Gemini | Enterprise AI

---

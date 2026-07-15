Follow-up Agent V2 - System Architecture

Overview

Follow-up Agent V2 is an enterprise AI workflow built using Google Agent Development Kit (ADK). The agent integrates multiple enterprise services to automate customer follow-up activities, reducing manual effort while maintaining personalized communication.

---

High-Level Architecture

                           User
                             │
                             ▼
                  Follow-up Agent (ADK)
                             │
      ┌────────────┬──────────┬────────────|
      ▼            ▼          ▼            ▼
     CRM        Gmail      Drive      Vertex AI RAG
      │            │          │            │
      └────────────┴──────────┴────────────┘
                             │
                             ▼
                     Gemini 2.5 Flash
                             │
                             ▼
                  Follow-up Email Draft
                             │
                             ▼
                      Gmail Send API
                             │
                             ▼
                     CRM Status Update

---

Workflow

Step 1 – Customer Input

The user provides:

- Customer Name
- Customer Email
- Optional Vertex AI RAG Corpus

---

Step 2 – CRM Lookup

The CRM service retrieves:

- Customer profile
- Contact information
- Sales pipeline stage
- Previous deals
- Notes
- Last activity

---

Step 3 – Previous Conversation

The Gmail service:

- Searches previous conversations
- Reads the latest email thread
- Extracts context

---

Step 4 – Google Drive Search

The Drive service searches for:

- Proposals
- Quotations
- Technical documents
- Presentations

related to the customer.

---

Step 5 – Enterprise Knowledge

If a Vertex AI RAG corpus is provided, the RAG service retrieves organization-specific knowledge relevant to the customer.

---

Step 6 – AI Reasoning

Gemini 2.5 Flash receives the available context and generates a professional follow-up email.

Current inputs include:

- Customer name
- Previous email conversation

The architecture is designed to also incorporate:

- CRM details
- Drive documents
- RAG knowledge

for richer personalization.

---

Step 7 – Email Delivery

The generated email is sent using the Gmail API.

Future versions can support additional providers such as Microsoft Outlook.

---

Step 8 – CRM Update

After successful delivery, the CRM status is updated to indicate that the follow-up has been sent.

---

Core Components

Agent Layer

- agent.py
- workflow.py
- registry.py
- prompts.py

Responsible for orchestrating the workflow.

---

Service Layer

Provides business logic for:

- CRM
- Gmail
- Google Drive
- Vertex AI RAG
- Gemini
- Follow-up orchestration

---

Tool Layer

Handles API interactions with:

- Gmail API
- Google Drive API
- Vertex AI
- CRM
- Outlook (future-ready)

---

Configuration Layer

Manages:

- OAuth credentials
- Environment variables
- Google Cloud settings
- Runtime configuration

---

Design Principles

- Modular architecture
- Service-oriented design
- Separation of concerns
- Enterprise API integration
- Extensible provider model
- Reusable components

---

Current Integrations

Service| Status
Gmail API| ✅ Implemented
Google Drive API| ✅ Implemented
Gemini 2.5 Flash| ✅ Implemented
Vertex AI RAG| ✅ Implemented (Optional)
CRM Service| ✅ Implemented
Outlook| 🚧 Planned / Partial

---

Future Roadmap

- Microsoft Graph integration
- Salesforce CRM
- HubSpot CRM
- Google Calendar
- Microsoft Teams
- Slack
- Automated follow-up scheduling
- Multi-agent collaboration
- Customer sentiment analysis
- Enterprise dashboard

---

Summary

Follow-up Agent V2 demonstrates a modular enterprise AI architecture where CRM systems, communication channels, enterprise documents, and generative AI work together to automate sales follow-up activities. The design supports future expansion with minimal changes to the orchestration layer.
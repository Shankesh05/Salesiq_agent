Follow-up Agent V2 - Design Document

1. Introduction

Follow-up Agent V2 is an autonomous enterprise sales agent developed using the Google Agent Development Kit (ADK). The objective of the agent is to automate customer follow-up by integrating CRM data, email conversations, enterprise documents, and Large Language Models into a single workflow.

Instead of manually searching customer history and drafting emails, the agent performs these tasks automatically and sends a professional follow-up email.

---

2. Problem Statement

Sales teams spend considerable time:

- Looking up customer information
- Searching previous email conversations
- Finding proposals and documents
- Drafting follow-up emails
- Updating CRM systems

The goal of this project is to automate these repetitive tasks using AI while maintaining personalization and enterprise context.

---

3. Solution Overview

The Follow-up Agent orchestrates multiple enterprise services into one intelligent workflow.

The workflow consists of:

1. Customer identification
2. CRM data retrieval
3. Previous email retrieval
4. Proposal search from Google Drive
5. Enterprise knowledge retrieval using Vertex AI RAG (optional)
6. AI-powered follow-up generation using Gemini
7. Email delivery using Gmail
8. CRM status update

---

4. System Architecture

                     User Input
                          │
                          ▼
               Follow-up Agent (ADK)
                          │
      ┌──────────┬─────────┬─────────┬──────────┐
      ▼          ▼         ▼         ▼
    CRM      Gmail     Drive     Vertex RAG
      │          │         │         │
      └──────────┴─────────┴─────────┘
                    │
                    ▼
            Gemini 2.5 Flash
                    │
                    ▼
          Follow-up Email Draft
                    │
                    ▼
             Gmail Send Service
                    │
                    ▼
             CRM Status Update

---

5. Components

Follow-up Workflow

Coordinates the complete business process and orchestrates all services.

Responsibilities:

- Invoke services
- Aggregate context
- Generate email
- Send email
- Update CRM

---

CRM Service

Retrieves:

- Customer profile
- Contact information
- Pipeline stage
- Previous deals
- Sales notes

---

Gmail Service

Responsible for:

- Searching customer emails
- Reading latest conversation
- Sending follow-up emails

---

Google Drive Service

Searches enterprise documents including:

- Proposals
- Quotations
- Technical documents
- Sales presentations

---

Vertex AI RAG Service

Provides organization-specific knowledge using enterprise documents stored in Vertex AI RAG.

Current implementation supports optional retrieval.

---

Gemini Service

Uses Gemini 2.5 Flash to generate professional follow-up emails using the collected enterprise context.

---

6. Folder Structure

followup_agent_v2/
│
├── agent.py
├── workflow.py
├── run.py
├── prompts.py
├── registry.py
├── models.py
├── config.py
│
├── services/
├── tools/
├── config/
└── templates/

---

7. Authentication

The system uses OAuth 2.0 authentication.

Services include:

- Gmail API
- Google Drive API

Authentication artifacts:

- credentials.json
- token.json

---

8. Technologies

Programming Language

- Python 3.12

Frameworks

- Google ADK
- Vertex AI SDK

AI Models

- Gemini 2.5 Flash

Cloud Platform

- Google Cloud Platform

Google APIs

- Gmail API
- Google Drive API

Enterprise AI

- Vertex AI RAG

---

9. Scalability

The architecture is modular.

Additional services can be integrated without modifying the core workflow.

Examples:

- Outlook
- Salesforce
- HubSpot
- Slack
- Microsoft Teams
- Google Calendar

---

10. Future Improvements

- Microsoft Graph integration for Outlook
- Calendar scheduling
- Meeting summarization
- Proposal recommendation
- CRM synchronization
- Multi-agent collaboration
- Customer sentiment analysis
- Automatic follow-up scheduling
- Sales analytics dashboard

---

11. Conclusion

Follow-up Agent V2 demonstrates how enterprise AI can automate customer engagement by combining CRM systems, cloud storage, enterprise knowledge, and generative AI into a unified workflow.

The modular architecture enables easy extension to additional enterprise services while maintaining a clean separation of concerns.
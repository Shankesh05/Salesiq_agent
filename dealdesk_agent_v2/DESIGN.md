DESIGN.md

DealDesk Agent V2 – System Design

Overview

DealDesk Agent V2 is an enterprise AI sales automation system built using Google Agent Development Kit (ADK). The agent orchestrates CRM retrieval, pricing, quotation generation, approval workflow, Google Drive integration, Vertex AI RAG retrieval, and Gemini-powered commercial proposal generation.

The project follows a modular service-oriented architecture, allowing each enterprise component to be independently maintained and extended.

---

High-Level Architecture

User
   │
   ▼
Google ADK Agent
   │
   ▼
DealDesk Workflow
   │
   ├── CRM Service
   ├── Product Catalog Service
   ├── Pricing Service
   ├── Approval Service
   ├── Google Drive Service
   ├── Vertex AI RAG Service (Optional)
   └── Gemini Service
           │
           ▼
Commercial Proposal
Executive Summary
Approval Note
Customer Email

---

Workflow

1. User submits deal request.
2. CRM retrieves customer information.
3. Product catalog retrieves product details.
4. Pricing engine calculates quotation.
5. Approval workflow evaluates the deal.
6. Google Drive searches existing proposal documents.
7. Vertex AI RAG retrieves enterprise knowledge (optional).
8. Gemini generates:
   - Commercial proposal
   - Executive summary
   - Approval justification
   - Customer-ready email
9. Final response is returned to the user.

---

Architecture Layers

Agent Layer

- Google ADK Agent
- Tool orchestration
- Natural language interaction

---

Workflow Layer

Coordinates the complete DealDesk business process.

Responsibilities:

- Execute services in sequence
- Aggregate outputs
- Handle workflow failures
- Return final business response

---

Service Layer

Contains enterprise business logic.

Services include:

- CRM Service
- Catalog Service
- Pricing Service
- Approval Service
- Drive Service
- RAG Service
- Gemini Service

Each service encapsulates one business capability.

---

Tool Layer

Implements reusable utility functions.

Examples:

- crm_tool.py
- catalog_tool.py
- pricing_tool.py
- approval_tool.py
- drive_tool.py
- rag_tool.py

Tools remain independent of workflow logic.

---

Pricing Flow

Product
     │
     ▼
Base Price
     │
     ▼
Discount
     │
     ▼
Tax
     │
     ▼
Final Quote

---

Proposal Generation Flow

CRM
        │
Catalog │
Pricing │
Drive   │
RAG     │
        ▼
 Gemini
        │
        ▼
Commercial Proposal
        │
        ├── Executive Summary
        ├── Approval Note
        └── Customer Email

---

Technologies

- Python 3.12
- Google ADK
- Gemini 2.5 Flash
- Google Drive API
- Vertex AI RAG
- Google OAuth
- Google Cloud Platform

---

Design Principles

- Modular architecture
- Separation of concerns
- Service-oriented design
- Reusable tools
- Configurable through environment variables
- Easy integration with production CRM systems
- Extensible enterprise workflow

---

Current Limitations

- CRM data uses sample records.
- Product catalog contains sample products.
- Google Drive uses demonstration documents.
- Vertex AI RAG is optional.
- Outlook/Microsoft 365 integration is not included.

---

Future Enhancements

- Salesforce integration
- Microsoft Dynamics CRM integration
- SAP CPQ integration
- Outlook/Microsoft Graph support
- PDF proposal generation
- Digital approval workflows
- Electronic signatures
- Real-time pricing APIs
- Multi-currency support
- Database-backed product catalog
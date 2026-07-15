ARCHITECTURE.md

DealDesk Agent V2 Architecture

Overview

DealDesk Agent V2 follows a layered, modular architecture built on Google Agent Development Kit (ADK). The architecture separates orchestration, business logic, integrations, and reusable tools, making the system scalable and maintainable.

---

System Architecture

                              User
                                │
                                ▼
                     Google ADK Web / CLI
                                │
                                ▼
                         DealDesk Agent
                                │
                                ▼
                      execute_dealdesk()
                                │
                                ▼
                     DealDesk Workflow
                                │
     ┌──────────────┬──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
 CRM Service   Catalog Service  Pricing Service  Approval Service
     │              │              │              │
     └──────────────┴───────┬──────┴──────────────┘
                            ▼
                    Google Drive Service
                            │
                            ▼
                     Vertex AI RAG Service
                            │
                            ▼
                      Gemini AI Service
                            │
                            ▼
                 Proposal / Summary / Email
                            │
                            ▼
                    Final Workflow Response

---

Layered Architecture

1. Presentation Layer

Responsible for user interaction.

Components:

- Google ADK Web
- Python CLI ("run.py")

Responsibilities:

- Accept user input
- Invoke the workflow
- Display results

---

2. Agent Layer

Implemented using Google ADK.

Responsibilities:

- Natural language interaction
- Tool invocation
- Workflow execution

Main file:

agent.py

---

3. Workflow Layer

Coordinates the complete business process.

Main file:

workflow.py

Responsibilities:

- Call services in sequence
- Handle failures
- Aggregate responses
- Return final output

---

4. Service Layer

Implements business logic.

Services include:

- CRM Service
- Catalog Service
- Pricing Service
- Approval Service
- Drive Service
- RAG Service
- Gemini Service

Responsibilities:

- Business rules
- External integrations
- Data processing
- AI generation

---

5. Tool Layer

Contains reusable utility modules.

Examples:

- crm_tool.py
- catalog_tool.py
- pricing_tool.py
- approval_tool.py
- drive_tool.py
- rag_tool.py

Responsibilities:

- CRUD operations
- Pricing calculations
- Mock enterprise integrations
- Google API interactions

---

Data Flow

User Request
      │
      ▼
Agent
      │
      ▼
Workflow
      │
      ├── CRM Lookup
      ├── Product Lookup
      ├── Pricing Calculation
      ├── Approval Generation
      ├── Drive Document Search
      ├── Vertex AI RAG Retrieval
      └── Gemini Proposal Generation
      │
      ▼
Final Business Response

---

Component Responsibilities

CRM Service

- Retrieve customer profile
- Retrieve opportunities
- Retrieve deal history
- Update CRM status

Catalog Service

- Retrieve product details
- Search products
- Check availability

Pricing Service

- Base price calculation
- Discount application
- Tax calculation
- Quote generation

Approval Service

- Generate approval request
- Determine approver
- Maintain approval history

Drive Service

- Retrieve proposal documents
- Search customer files
- Search quotations

Vertex AI RAG Service

- Customer knowledge retrieval
- Pricing policies
- Product knowledge
- Discount policies

Gemini Service

- Commercial proposal generation
- Executive summary generation
- Approval justification
- Customer email generation

---

Design Principles

- Layered Architecture
- Separation of Concerns
- Modular Components
- Service-Oriented Design
- Reusable Tool Layer
- Configurable through Environment Variables
- Easy integration with enterprise systems

---

External Integrations

- Google ADK
- Gemini 2.5 Flash
- Vertex AI
- Google Drive API
- Google OAuth
- Google Cloud Platform

---

Current Implementation

- CRM: Sample implementation
- Product Catalog: Sample implementation
- Pricing Engine: Fully implemented
- Approval Workflow: Fully implemented
- Google Drive Integration: Implemented
- Vertex AI RAG: Optional integration
- Gemini AI: Implemented
- ADK Agent: Implemented

---

Future Architecture Enhancements

- Salesforce CRM Integration
- HubSpot Integration
- Microsoft Dynamics 365
- SAP CPQ Integration
- PostgreSQL Product Catalog
- Redis Caching Layer
- Docker & Kubernetes Deployment
- Cloud Run / GKE Deployment
- Monitoring with Cloud Logging
- Secret Manager Integration
- Multi-agent orchestration
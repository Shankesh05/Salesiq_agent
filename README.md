# 🚀 SalesIQ Agent

An enterprise-grade, AI-powered multi-agent sales automation system built during my AI Engineering & Solutions Architect Internship at Stratova AI.

This repository showcases the design and implementation of intelligent sales agents capable of handling proposal generation, commercial validation, customer follow-ups, enterprise knowledge retrieval, CRM integration, and automated sales workflows using modern Generative AI technologies.

> **Note:** This repository is intended for portfolio and demonstration purposes. Sensitive credentials, internal configurations, and proprietary business assets have been excluded.

---

# 📌 Project Overview

SalesIQ Agent is a modular multi-agent platform that streamlines enterprise sales operations through AI-driven automation.

The system leverages Retrieval-Augmented Generation (RAG), Google ADK, Gemini models, FastAPI services, and enterprise integrations to automate critical sales workflows while keeping human approval in the decision loop.

---

# ✨ Features

- 🤖 Multi-Agent Sales Orchestration
- 📄 Enterprise Proposal Generation
- 💼 DealDesk Automation
- 📧 Intelligent Customer Follow-up
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Gemini-powered Prompt Workflows
- 📂 Google Drive Integration
- 📧 Gmail Integration
- 🏢 CRM Integration
- 💰 Pricing Validation
- ✅ Commercial Approval Workflow
- 📊 Enterprise Knowledge Retrieval
- ⚙️ Modular Service Architecture
- ☁️ Google Cloud Ready

---

# 🏗️ Architecture

```
                    +----------------------+
                    |      User Request    |
                    +----------+-----------+
                               |
                               ▼
                  SalesIQ Multi-Agent System
                               |
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
 DealDesk Agent         Follow-up Agent        Knowledge/RAG
        │                      │                      │
        └──────────────┬───────┴──────────────────────┘
                       ▼
               Enterprise Services
                       │
     ┌─────────────────┼─────────────────┐
     ▼                 ▼                 ▼
   CRM            Google Drive         Gmail
     ▼                 ▼                 ▼
               Gemini + Vertex AI
                       │
                       ▼
                Business Response
```

---

# 🛠️ Tech Stack

## Programming

- Python

## AI & LLM

- Google Gemini
- Google ADK
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

## Backend

- FastAPI

## Cloud

- Google Cloud Platform
- Vertex AI

## Data

- Vector Search
- Document Processing
- Knowledge Retrieval

## Integrations

- Gmail
- Google Drive
- CRM Services

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
agents/
│
├── sales_iq/
│   ├── dealdesk_agent_v2/
│   ├── followup_agent_v2/
│   └── tests/
│
tools/
│
├── google/
├── rag/
├── sales/
│
deployment/
│
README.md
```

---

# 🤖 Major Components

## DealDesk Agent

Responsible for:

- Proposal generation
- Commercial validation
- Pricing verification
- Approval workflow
- Negotiation handling
- Customer proposal preparation

---

## Follow-up Agent

Responsible for:

- Customer communication
- Automated follow-ups
- Email generation
- CRM updates
- Deal progression

---

## RAG Services

- Knowledge retrieval
- Document search
- Enterprise context generation
- Semantic retrieval

---

## Google Integrations

- Gmail
- Google Drive
- Gemini APIs

---

# 📈 Key Contributions

- Designed enterprise multi-agent workflows
- Built DealDesk Agent V2
- Built Follow-up Agent V2
- Implemented enterprise RAG integration
- Integrated Google Gemini services
- Implemented CRM and pricing workflows
- Refactored shared Google utilities
- Improved modular architecture
- Resolved merge conflicts and production PRs
- Enhanced maintainability and scalability

---

# 📊 Highlights

- Enterprise-ready architecture
- Modular agent design
- Human-in-the-loop approval workflow
- AI-assisted proposal generation
- Retrieval-Augmented Generation
- Production-oriented project structure
- Scalable service-based architecture

---

# 📖 Learning Outcomes

During this project, I gained hands-on experience in:

- Multi-Agent AI Systems
- Enterprise Software Architecture
- Google ADK
- Vertex AI
- Prompt Engineering
- Retrieval-Augmented Generation
- Enterprise API Integration
- AI Workflow Orchestration
- Modular Backend Development
- Production Git Workflow

---

# 📌 Repository Status

✅ Active Portfolio Project

This repository represents the work completed during my internship and serves as a demonstration of enterprise AI engineering concepts and implementations.

---

# 👨‍💻 Author

**Shankesh Raja**

B.Tech Computer Science Engineering (Big Data Analytics)

AI Engineering & Solutions Architecture Enthusiast

GitHub: https://github.com/Shankesh05

LinkedIn: https://www.linkedin.com/in/shankesh-raja-028946319

Portfolio: https://shankesh05.github.io/Shankesh_Portfolio

---

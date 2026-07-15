Follow-up Agent V2 - Deployment Guide

Overview

This guide explains how to deploy and run the Follow-up Agent V2 locally using Google Agent Development Kit (ADK), Google Cloud Platform, Gmail API, Google Drive API, Gemini, and Vertex AI.

---

Prerequisites

- Python 3.11 or above
- Google Cloud Project
- Google ADK
- Gmail API Enabled
- Google Drive API Enabled
- Vertex AI API Enabled (Optional)
- OAuth Client Credentials

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
├── requirements.txt
│
├── config/
│   ├── credentials.json
│   └── token.json
│
├── services/
├── tools/
└── templates/

---

Step 1 – Clone Repository

git clone <repository-url>

cd followup_agent_v2

---

Step 2 – Create Virtual Environment

Windows

python -m venv .venv

.venv\Scripts\activate

Linux / macOS

python3 -m venv .venv

source .venv/bin/activate

---

Step 3 – Install Dependencies

pip install -r requirements.txt

---

Step 4 – Configure Google Cloud

Authenticate Google Cloud.

gcloud auth application-default login

Set project.

gcloud config set project YOUR_PROJECT_ID

Verify.

gcloud config get-value project

---

Step 5 – Enable Required APIs

Enable the following Google Cloud APIs:

- Gmail API
- Google Drive API
- Vertex AI API (Optional)
- Generative Language API

---

Step 6 – OAuth Configuration

Download OAuth Desktop Client credentials.

Copy

credentials.json

to

followup_agent_v2/config/

Delete any existing

token.json

before first execution.

The application will generate a new token during authentication.

---

Step 7 – Environment Variables

Create a ".env" file.

Example:

GOOGLE_CLOUD_PROJECT=your-project-id

GOOGLE_CLOUD_LOCATION=us-central1

MODEL_NAME=gemini-2.5-flash

DEBUG=False

---

Step 8 – Run the Agent

Command Line

python -m agents.sales_iq.followup_agent_v2.run

Example Input

Customer Name : Google

Customer Email : customer@example.com

Vertex RAG Corpus :

---

Step 9 – Run with Google ADK

Start the ADK web interface.

adk web

The agent will be available for interactive execution through the ADK interface.

---

Authentication

The first execution opens the Google OAuth consent screen.

Permissions requested:

- Gmail Read
- Gmail Modify
- Gmail Send
- Google Drive Read

After successful authentication, a "token.json" file is generated automatically.

---

Optional Vertex AI RAG

If a Vertex AI RAG corpus exists, provide the corpus name during execution.

Otherwise, leave the field blank.

The workflow will continue without RAG retrieval.

---

Expected Workflow

1. Customer information is entered.
2. CRM retrieves customer context.
3. Gmail searches previous conversations.
4. Google Drive searches related documents.
5. Vertex AI RAG retrieves enterprise knowledge (optional).
6. Gemini generates a personalized follow-up email.
7. Gmail sends the email.
8. CRM updates the customer status.

---

Troubleshooting

OAuth Error

Delete "config/token.json" and authenticate again.

---

Gmail Permission Error

Ensure the Gmail API is enabled and OAuth scopes include:

- Gmail Read
- Gmail Modify
- Gmail Send

---

Drive Permission Error

Enable Google Drive API and regenerate the OAuth token after adding the Drive scope.

---

Vertex AI Error

Verify:

- Vertex AI API is enabled.
- Google Cloud project is configured correctly.
- A valid RAG corpus is provided (if using RAG).

---

Deployment Checklist

- Python installed
- Dependencies installed
- Google Cloud configured
- Gmail API enabled
- Google Drive API enabled
- OAuth credentials added
- ".env" configured
- "credentials.json" available
- "token.json" generated
- Agent executes successfully

---

Deployment Status

Component| Status
Google ADK| ✅
Gemini 2.5 Flash| ✅
Gmail API| ✅
Google Drive API| ✅
Vertex AI RAG| ✅ (Optional)
CRM| ✅
Follow-up Workflow| ✅

---

Result

The Follow-up Agent V2 is ready for local execution and demonstration through both the command-line interface and the Google ADK web interface.
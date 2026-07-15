"""
Configuration for Follow-up Agent V2.

Loads all runtime configuration from environment variables.
Designed to be reusable across all Sales IQ agents.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------
# Base Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

# laabu-ai-app-main/
PROJECT_ROOT = BASE_DIR.parents[3]

CONFIG_DIR = BASE_DIR / "config"

# ---------------------------------------------------------
# Load Environment
# ---------------------------------------------------------

load_dotenv(PROJECT_ROOT / ".env")

# ---------------------------------------------------------
# Application
# ---------------------------------------------------------

APP_NAME = "Follow-up Agent V2"

VERSION = "1.0.0"

DEBUG = (
    os.getenv("DEBUG", "False").lower()
    == "true"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO",
)

# ---------------------------------------------------------
# Google Cloud
# ---------------------------------------------------------

GOOGLE_CLOUD_PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    "development-local-500411",
)

GOOGLE_CLOUD_LOCATION = os.getenv(
    "GOOGLE_CLOUD_LOCATION",
    "us-central1",
)

GOOGLE_GENAI_USE_VERTEXAI = (
    os.getenv(
        "GOOGLE_GENAI_USE_VERTEXAI",
        "True",
    ).lower()
    == "true"
)

# ---------------------------------------------------------
# Gemini
# ---------------------------------------------------------

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash",
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    "",
)

# ---------------------------------------------------------
# Gmail
# ---------------------------------------------------------

GMAIL_USER = os.getenv(
    "GMAIL_USER",
    "",
)

GMAIL_SCOPES = [

    "https://www.googleapis.com/auth/gmail.readonly",

    "https://www.googleapis.com/auth/gmail.send",

    "https://www.googleapis.com/auth/gmail.modify",

]

# ---------------------------------------------------------
# Google Drive
# ---------------------------------------------------------

DRIVE_SCOPES = [

    "https://www.googleapis.com/auth/drive",

]

# ---------------------------------------------------------
# OAuth Credentials
# ---------------------------------------------------------

CREDENTIALS_FILE = CONFIG_DIR / "tools_config.json"

TOKEN_FILE = CONFIG_DIR / "token.json"

# ---------------------------------------------------------
# Vertex AI RAG
# ---------------------------------------------------------

RAG_CORPUS = os.getenv(
    "VERTEX_RAG_CORPUS",
    "followup-agent-rag",
)

# ---------------------------------------------------------
# Defaults
# ---------------------------------------------------------

DEFAULT_TOP_K = 5

REQUEST_TIMEOUT = 300

MAX_RESULTS = 10

# ---------------------------------------------------------
# Helper
# ---------------------------------------------------------

def print_config():

    print("=" * 60)

    print(APP_NAME)

    print("=" * 60)

    print("Project :", GOOGLE_CLOUD_PROJECT)

    print("Location:", GOOGLE_CLOUD_LOCATION)

    print("Model   :", MODEL_NAME)

    print("RAG     :", RAG_CORPUS)

    print("Debug   :", DEBUG)

    print("=" * 60)
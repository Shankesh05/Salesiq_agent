"""
Configuration for DealDesk Agent V2.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------
# Base Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = BASE_DIR.parents[2]

load_dotenv(PROJECT_ROOT / ".env")

# ---------------------------------------------------------
# Application
# ---------------------------------------------------------

APP_NAME = "DealDesk Agent V2"

VERSION = "2.0.0"

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development",
)

# ---------------------------------------------------------
# Google Cloud
# ---------------------------------------------------------

GOOGLE_CLOUD_PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    "",
)

GOOGLE_CLOUD_LOCATION = os.getenv(
    "GOOGLE_CLOUD_LOCATION",
    "us-central1",
)

GOOGLE_GENAI_USE_VERTEXAI = (
    os.getenv(
        "GOOGLE_GENAI_USE_VERTEXAI",
        "true",
    ).lower()
    == "true"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash",
)

# ---------------------------------------------------------
# Firestore
# ---------------------------------------------------------

FIRESTORE_DATABASE = os.getenv(
    "FIRESTORE_DATABASE",
    "(default)",
)

CUSTOMER_COLLECTION = "customers"

PRODUCT_COLLECTION = "products"

DEAL_COLLECTION = "deals"

APPROVAL_COLLECTION = "approval_requests"

FOLLOWUP_COLLECTION = "followups"

# ---------------------------------------------------------
# Vertex AI RAG
# ---------------------------------------------------------

RAG_CORPUS = os.getenv(
    "VERTEX_RAG_CORPUS",
    "",
)

# ---------------------------------------------------------
# Google Drive
# ---------------------------------------------------------

DRIVE_FOLDER = os.getenv(
    "DRIVE_FOLDER",
    "",
)

# ---------------------------------------------------------
# Commercial Policy
# ---------------------------------------------------------

DEFAULT_TAX = float(
    os.getenv(
        "DEFAULT_TAX",
        "18",
    )
)

DEFAULT_CURRENCY = os.getenv(
    "DEFAULT_CURRENCY",
    "USD",
)

MAX_ALLOWED_DISCOUNT = float(
    os.getenv(
        "MAX_ALLOWED_DISCOUNT",
        "5",
    )
)

MAX_NEGOTIATION_ATTEMPTS = int(
    os.getenv(
        "MAX_NEGOTIATION_ATTEMPTS",
        "4",
    )
)

# ---------------------------------------------------------
# Follow-up
# ---------------------------------------------------------

ENABLE_FOLLOWUP = (
    os.getenv(
        "ENABLE_FOLLOWUP",
        "true",
    ).lower()
    == "true"
)

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO",
)

DEBUG = (
    os.getenv(
        "DEBUG",
        "false",
    ).lower()
    == "true"
)
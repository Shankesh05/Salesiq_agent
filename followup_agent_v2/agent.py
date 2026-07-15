"""
Follow-up Automation Agent V2
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# ------------------------------------------------------------------
# Add project root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------

from google.adk.agents import Agent
import google.auth
from dotenv import load_dotenv

try:
    from agents.sales_iq.followup_agent_v2.prompts import build_instruction
    from agents.sales_iq.followup_agent_v2.registry import get_all_tools
except ImportError:
    from prompts import build_instruction
    from registry import get_all_tools

# ------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------

load_dotenv()

try:
    _, project = google.auth.default()

    if project:
        os.environ.setdefault(
            "GOOGLE_CLOUD_PROJECT",
            project,
        )

except Exception:
    pass

os.environ.setdefault(
    "GOOGLE_CLOUD_LOCATION",
    "us-central1",
)

os.environ.setdefault(
    "GOOGLE_GENAI_USE_VERTEXAI",
    "True",
)

# ------------------------------------------------------------------
# Root Agent
# ------------------------------------------------------------------

root_agent = Agent(
    name="followup_agent_v2",
    model="gemini-2.5-flash",
    instruction=build_instruction,
    tools=get_all_tools(),
)

app = root_agent

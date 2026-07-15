"""
Deploy the DealDesk Agent to Vertex AI Agent Engine.

Run from inside the project environment:

    cd agents/sales_iq/dealdesk_agent_v2
    uv run python deploy/deploy.py
"""

from __future__ import annotations

import importlib as _importlib
import logging
import os
import shutil
import sys
import tempfile
from pathlib import Path

import cloudpickle as _cloudpickle
import vertexai
from dotenv import load_dotenv, set_key
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------

_SCRIPT_DIR = Path(__file__).parent.resolve()
_AGENT_DIR = _SCRIPT_DIR.parent.resolve()
_SALESIQ_DIR = _AGENT_DIR.parent.resolve()
_REPO_ROOT = _SALESIQ_DIR.parent.parent.resolve()

_ENV_FILE = _AGENT_DIR / ".env"

load_dotenv(_ENV_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
)

log = logging.getLogger(__name__)

PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    "",
)

LOCATION = os.getenv(
    "GOOGLE_CLOUD_LOCATION",
    "us-central1",
)

BUCKET = os.getenv(
    "STAGING_BUCKET",
    "",
)

RAG_CORPUS = os.getenv(
    "VERTEX_RAG_CORPUS",
    "",
)

REQUIREMENTS = [
    "google-cloud-aiplatform[adk,agent-engines]==1.153.1",
    "google-adk==1.34.3",
    "google-cloud-firestore",
    "google-cloud-storage>=2.0",
    "google-auth>=2.36.0",
    "google-genai>=1.0.0",
    "python-dotenv",
    "requests>=2.32.3",
]

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------


def main():

    vertexai.init(

        project=PROJECT,

        location=LOCATION,

        staging_bucket=BUCKET,

    )

    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "1"

    if RAG_CORPUS:
        os.environ["VERTEX_RAG_CORPUS"] = RAG_CORPUS

    sys.path.insert(0, str(_REPO_ROOT))
    sys.path.insert(0, str(_AGENT_DIR))

    log.info("Importing DealDesk Agent...")

    from agent import root_agent

    for module_name in [

        "agent",

        "config",

        "prompts",

    ]:

        try:

            module = _importlib.import_module(module_name)

            _cloudpickle.register_pickle_by_value(module)

            log.info(

                "Registered '%s' for pickling.",

                module_name,

            )

        except Exception as exc:

            log.warning(

                "Could not register '%s': %s",

                module_name,

                exc,

            )

    wrapped = AdkApp(

        agent=root_agent,

        enable_tracing=True,

    )

    env_vars = {

        "GOOGLE_GENAI_USE_VERTEXAI": "1",

        "GOOGLE_CLOUD_PROJECT": PROJECT,

        "GOOGLE_CLOUD_LOCATION": LOCATION,

        "VERTEX_RAG_CORPUS": RAG_CORPUS,

    }

    log.info("Deploying DealDesk Agent...")
    log.info("Project : %s", PROJECT)
    log.info("Location: %s", LOCATION)

    with tempfile.TemporaryDirectory(
        prefix="dealdesk_bundle_"
    ) as tmp:

        bundle = Path(tmp)

        # ------------------------------------------------------
        # Agent files
        # ------------------------------------------------------

        for file_name in [

            "agent.py",

            "config.py",

            "prompts.py",

            "workflow.py",

            "registry.py",

            "models.py",

        ]:

            src = _AGENT_DIR / file_name

            if src.exists():

                shutil.copy2(

                    src,

                    bundle / file_name,

                )

                log.info(

                    "Bundled %s",

                    file_name,

                )

        # ------------------------------------------------------
        # Services
        # ------------------------------------------------------

        shutil.copytree(

            _AGENT_DIR / "services",

            bundle / "services",

        )

        # ------------------------------------------------------
        # Shared tools
        # ------------------------------------------------------

        shutil.copytree(

            _REPO_ROOT / "tools",

            bundle / "tools",

        )

        log.info("Bundled tools/")

        os.chdir(bundle)

        remote_app = agent_engines.create(

            wrapped,

            display_name="SalesIQ - DealDesk Agent",

            requirements=REQUIREMENTS,

            extra_packages=["."],

            env_vars=env_vars,

        )

    resource_name = remote_app.resource_name

    log.info(

        "Deployment successful: %s",

        resource_name,

    )

    try:

        set_key(

            str(_ENV_FILE),

            "AGENT_ENGINE_ID",

            resource_name,

        )

    except Exception as exc:

        log.warning(

            "Unable to update .env: %s",

            exc,

        )

    print()

    print("=" * 70)

    print("DealDesk Agent deployed successfully!")

    print(resource_name)

    print("=" * 70)

    print()


if __name__ == "__main__":

    main()

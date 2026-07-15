"""
Models

Follow-up Agent data models.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Request
# ---------------------------------------------------------

class FollowupRequest(BaseModel):

    customer: str = Field(
        ...,
        description="Customer name",
    )

    customer_email: str = Field(
        ...,
        description="Customer email address",
    )

    corpus_name: str | None = Field(
        default=None,
        description="Optional Vertex AI RAG corpus",
    )


# ---------------------------------------------------------
# Response
# ---------------------------------------------------------

class FollowupResponse(BaseModel):

    status: str

    customer: str

    customer_email: str

    subject: str

    draft: str

    gmail: dict[str, Any] = Field(
        default_factory=dict,
    )

    crm: dict[str, Any] = Field(
        default_factory=dict,
    )

    crm_update: dict[str, Any] = Field(
        default_factory=dict,
    )

    proposal: Any = None

    knowledge: Any = None

    previous_email: str | None = None


# ---------------------------------------------------------
# Workflow Status
# ---------------------------------------------------------

class WorkflowStep(BaseModel):

    step: str

    status: str

    message: str = ""


class WorkflowReport(BaseModel):

    customer: str

    steps: list[WorkflowStep] = Field(
        default_factory=list,
    )

    completed: bool = False
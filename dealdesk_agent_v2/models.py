"""
Models

Data models for DealDesk Agent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------
# Customer
# ---------------------------------------------------------

@dataclass
class Customer:

    customer_id: str

    customer_name: str

    industry: str

    account_type: str

    region: str

    status: str

    primary_contact: dict[str, Any] = field(default_factory=dict)

    notes: list[str] = field(default_factory=list)


# ---------------------------------------------------------
# Product
# ---------------------------------------------------------

@dataclass
class Product:

    sku: str

    name: str

    category: str

    description: str

    price: float

    currency: str

    availability: str

    support: str = ""

    license: str = ""


# ---------------------------------------------------------
# Quote
# ---------------------------------------------------------

@dataclass
class Quote:

    quote_id: str

    customer: str

    product: str

    sku: str

    quantity: int

    unit_price: float

    base_price: float

    discount_percent: float

    discount_amount: float

    subtotal: float

    tax_percent: float

    tax_amount: float

    final_price: float

    currency: str

    generated_at: str

    status: str


# ---------------------------------------------------------
# Approval
# ---------------------------------------------------------

@dataclass
class Approval:

    approval_id: str

    deal_id: str

    approval_level: str

    status: str

    discount_percent: float

    amount: float

    customer_reason: str = ""


# ---------------------------------------------------------
# Proposal
# ---------------------------------------------------------

@dataclass
class Proposal:

    proposal: str

    executive_summary: str

    approval_note: str

    customer_email: str

    internal_note: str


# ---------------------------------------------------------
# Follow-up
# ---------------------------------------------------------

@dataclass
class FollowUp:

    required: bool

    reason: str | None = None


# ---------------------------------------------------------
# Workflow Result
# ---------------------------------------------------------

@dataclass
class WorkflowResult:

    status: str

    customer: str

    crm: dict[str, Any]

    catalog: dict[str, Any]

    quote: dict[str, Any]

    approval: dict[str, Any]

    documents: dict[str, Any]

    knowledge: Any

    proposal: str

    executive_summary: str

    approval_note: str

    customer_email: str

    internal_note: str

    followup: dict[str, Any]


# ---------------------------------------------------------
# Agent Response
# ---------------------------------------------------------

@dataclass
class AgentResponse:

    success: bool

    message: str

    data: dict[str, Any] = field(default_factory=dict)
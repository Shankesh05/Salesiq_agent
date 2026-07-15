"""
Pricing Service

Business layer for Pricing Engine.
"""

from __future__ import annotations

from tools.sales.pricing_tool import (
    calculate_base_price,
    apply_discount,
    apply_tax,
    generate_quote,
    quote_summary,
    validate_quantity,
    validate_discount,
)


class PricingService:

    # ---------------------------------------------------------
    # Base Price
    # ---------------------------------------------------------

    def base_price(

        self,

        product_name: str,

        quantity: int = 1,

    ):

        return calculate_base_price(

            product_name,

            quantity,

        )

    # ---------------------------------------------------------
    # Discount
    # ---------------------------------------------------------

    def discount(

        self,

        amount: float,

        discount_percent: float,

    ):

        return apply_discount(

            amount,

            discount_percent,

        )

    # ---------------------------------------------------------
    # Tax
    # ---------------------------------------------------------

    def tax(

        self,

        amount: float,

        tax_percent: float,

    ):

        return apply_tax(

            amount,

            tax_percent,

        )

    # ---------------------------------------------------------
    # Generate Quote
    # ---------------------------------------------------------

    def generate(

        self,

        customer: str,

        product_name: str,

        quantity: int,

        discount_percent: float = 0,

        tax_percent: float = 18,

    ):

        return generate_quote(

            customer=customer,

            product_name=product_name,

            quantity=quantity,

            discount_percent=discount_percent,

            tax_percent=tax_percent,

        )

    # ---------------------------------------------------------
    # Quote Summary
    # ---------------------------------------------------------

    def summary(

        self,

        quote: dict,

    ):

        return quote_summary(

            quote,

        )

    # ---------------------------------------------------------
    # Validate Quantity
    # ---------------------------------------------------------

    def valid_quantity(

        self,

        quantity: int,

    ):

        return validate_quantity(

            quantity,

        )

    # ---------------------------------------------------------
    # Validate Discount
    # ---------------------------------------------------------

    def valid_discount(

        self,

        discount_percent: float,

    ):

        return validate_discount(

            discount_percent,

        )
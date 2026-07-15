"""
RAG Service

Business layer for Vertex AI RAG.
"""

from __future__ import annotations

from tools.rag.rag_tool import (
    retrieve_customer_context,
    retrieve_product_context,
    retrieve_pricing_policy,
    retrieve_discount_policy,
    semantic_search,
)


class RAGService:

    # ---------------------------------------------------------
    # Customer Context
    # ---------------------------------------------------------

    def customer_context(

        self,

        corpus_name: str,

        customer: str,

    ):

        return retrieve_customer_context(

            corpus_name,

            customer,

        )

    # ---------------------------------------------------------
    # Product Context
    # ---------------------------------------------------------

    def product_context(

        self,

        corpus_name: str,

        product: str,

    ):

        return retrieve_product_context(

            corpus_name,

            product,

        )

    # ---------------------------------------------------------
    # Pricing Policy
    # ---------------------------------------------------------

    def pricing_policy(

        self,

        corpus_name: str,

        product: str,

    ):

        return retrieve_pricing_policy(

            corpus_name,

            product,

        )

    # ---------------------------------------------------------
    # Discount Policy
    # ---------------------------------------------------------

    def discount_policy(

        self,

        corpus_name: str,

        product: str,

    ):

        return retrieve_discount_policy(

            corpus_name,

            product,

        )

    # ---------------------------------------------------------
    # Generic Search
    # ---------------------------------------------------------

    def search(

        self,

        corpus_name: str,

        query: str,

    ):

        return semantic_search(

            corpus_name,

            query,

        )

    # ---------------------------------------------------------
    # Complete Knowledge Context
    # ---------------------------------------------------------

    def knowledge_context(

        self,

        corpus_name: str,

        customer: str,

        product: str,

    ):

        return {

            "customer": self.customer_context(

                corpus_name,

                customer,

            ),

            "product": self.product_context(

                corpus_name,

                product,

            ),

            "pricing": self.pricing_policy(

                corpus_name,

                product,

            ),

            "discount": self.discount_policy(

                corpus_name,

                product,

            ),

        }
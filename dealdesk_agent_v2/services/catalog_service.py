"""
Catalog Service

Business layer for Product Catalog.
"""

from __future__ import annotations

from tools.sales.catalog_tool import (
    list_products,
    get_product,
    get_product_by_sku,
    products_by_category,
    check_availability,
    search_products,
    create_product,
    update_product,
    delete_product,
)


class CatalogService:

    # ---------------------------------------------------------
    # Get All Products
    # ---------------------------------------------------------

    def products(self):

        return list_products()

    # ---------------------------------------------------------
    # Get Product By Name
    # ---------------------------------------------------------

    def product(

        self,

        product_name: str,

    ):

        return get_product(

            product_name,

        )

    # ---------------------------------------------------------
    # Get Product By SKU
    # ---------------------------------------------------------

    def sku(

        self,

        sku: str,

    ):

        return get_product_by_sku(

            sku,

        )

    # ---------------------------------------------------------
    # Products By Category
    # ---------------------------------------------------------

    def category(

        self,

        category: str,

    ):

        return products_by_category(

            category,

        )

    # ---------------------------------------------------------
    # Availability
    # ---------------------------------------------------------

    def availability(

        self,

        product_name: str,

    ):

        return check_availability(

            product_name,

        )

    # ---------------------------------------------------------
    # Search Products
    # ---------------------------------------------------------

    def search(

        self,

        keyword: str,

    ):

        return search_products(

            keyword,

        )

    # ---------------------------------------------------------
    # Create Product
    # ---------------------------------------------------------

    def create(

        self,

        product: dict,

    ):

        return create_product(

            product,

        )

    # ---------------------------------------------------------
    # Update Product
    # ---------------------------------------------------------

    def update(

        self,

        sku: str,

        data: dict,

    ):

        return update_product(

            sku,

            data,

        )

    # ---------------------------------------------------------
    # Delete Product
    # ---------------------------------------------------------

    def delete(

        self,

        sku: str,

    ):

        return delete_product(

            sku,

        )
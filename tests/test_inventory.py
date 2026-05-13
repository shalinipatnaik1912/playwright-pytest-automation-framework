# Test Cases for Product Inventory

import pytest
from pages.login_page import LoginPage

#TC007: Verify all products are displayed

def test_inventory_display(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Verify 6 products are displayed   
    products = page.query_selector_all(".inventory_item")
    assert len(products) == 6, f"Expected 6 products, but found {len(products)}"

    # Verify each product has: image, name, description, price, "Add to cart" button
    for product in products:    
        assert product.query_selector(".inventory_item_img") is not None, "Product image is missing"
        assert product.query_selector(".inventory_item_name") is not None, "Product name is missing"
        assert product.query_selector(".inventory_item_desc") is not None, "Product description is missing"
        assert product.query_selector(".inventory_item_price") is not None, "Product price is missing"
        assert product.query_selector("button[id^='add-to-cart']") is not None, "Add to cart button is missing"
 
#  TC008: Add single product to cart
def test_add_single_product_to_cart(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce") 

    # Add "Sauce Labs Backpack" to cart
    backpack = page.query_selector(".inventory_item:has-text('Sauce Labs Backpack')")
    backpack.query_selector("button[id^='add-to-cart']").click()

    # Verify button text changes to "Remove"
    assert backpack.query_selector("button[id^='remove']").is_visible()

    # Verify cart badge shows "1"
    assert page.query_selector(".shopping_cart_badge").text_content() == "1"

# TC009: Add multiple products to cart

def test_add_multiple_products_to_cart(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Add products to cart
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
    for product_name in products:
        product = page.query_selector(f".inventory_item:has-text('{product_name}')")
        product.query_selector("button[id^='add-to-cart']").click()

    # Verify cart badge shows "3"
    assert page.query_selector(".shopping_cart_badge").text_content() == "3"

# TC010: Remove product from inventory page

def test_remove_product_from_inventory(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")


# TC011: Sort products by price (low to high)

def test_sort_products_by_price_low_to_high(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Select "Price (low to high)" from sort dropdown
    page.select_option(".product_sort_container", "lohi")

    # Verify products are sorted correctly by price ascending
    product_prices = page.query_selector_all(".inventory_item_price")
    prices = [float(price.text_content().strip('$')) for price in product_prices]
    assert prices == sorted(prices), "Products are not sorted by price ascending"
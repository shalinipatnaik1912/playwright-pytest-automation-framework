# Test Cases for Shopping Cart

import pytest
from pages import cart_page
from pages.cart_page import CartPage
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage 

# TC012: View cart with added items

def test_view_cart_with_added_items(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()

    # Verify cart page displays the added product
    # Verify product name, price, and quantity are correct
    cart_item = page.locator(".cart_item").first
    assert cart_item.count() == 1, "Cart item is not displayed"  
    assert cart_item.locator(".inventory_item_name").text_content() == "Sauce Labs Backpack", "Product name is incorrect in cart"
    assert cart_item.locator(".inventory_item_price").text_content() == "$29.99", "Product price is incorrect in cart"
    assert cart_page.get_cart_item_count() == 1, "Cart item count is incorrect"

# TC013: Remove item from cart

def test_remove_item_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    page.locator(".btn_small").click()
    assert page.locator(".cart_item").count() == 0, "Cart item is still displayed"


# TC014: Continue shopping from cart

def test_continue_shopping_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.continue_shopping()
    assert page.url.endswith("/inventory.html"), "User is not redirected back to inventory page after clicking Continue Shopping"

# TC015: Cart persists across pages

def test_cart_persistence_across_pages(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce") 

    # Add multiple products to cart
    inventory_page.add_product_to_cart("Sauce Labs Backpack")       
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.click_cart()
    assert cart_page.get_cart_item_count() == 2, "Cart item count is incorrect after adding multiple items"

# TC016: Multiple items in cart calculation

def test_multiple_items_cart_calculation(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    page.goto("https://www.saucedemo.com/") 
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light") 
    inventory_page.click_cart()
    assert cart_page.get_cart_item_count() == 2, "Cart item count is incorrect for multiple items"
    assert page.query_selector_all(".cart_item")[0].query_selector(".inventory_item_name").text_content() == "Sauce Labs Backpack", "First product name is incorrect in cart"
    assert page.query_selector_all(".cart_item")[1].query_selector(".inventory_item_name").text_content() == "Sauce Labs Bike Light", "Second product name is incorrect in cart"
    assert page.query_selector_all(".cart_item")[0].query_selector(".inventory_item_price").text_content() == "$29.99", "First product price is incorrect in cart"
    assert page.query_selector_all(".cart_item")[1].query_selector(".inventory_item_price").text_content() == "$9.99", "Second product price is incorrect in cart"
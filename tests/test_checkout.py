# Test Cases for Checkout Process

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

# TC017: Complete checkout with valid information

def test_complete_checkout_with_valid_information(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.continue_checkout()
    assert overview_page.is_displayed(), "Checkout overview page is not displayed"  
    assert overview_page.get_item_total() == 29.99, "Item total is incorrect"
    assert overview_page.get_tax() == 2.40, "Tax is calculated incorrectly"
    assert overview_page.get_total() == 32.39, "Total is calculated incorrectly"
    overview_page.click_finish()
    assert overview_page.get_success_message() == "Thank you for your order!", "Success message is incorrect"

# TC018: Checkout with empty first name

def test_checkout_with_empty_first_name(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("", "Doe", "12345")
    checkout_page.continue_checkout()
    error_message = page.locator(".error-message-container").text_content()
    assert error_message == "Error: First Name is required", "Error message for empty first name is incorrect"

# TC019: Checkout with empty last name

def test_checkout_with_empty_last_name(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "", "12345")
    checkout_page.continue_checkout()
    error_message = page.locator(".error-message-container").text_content()
    assert error_message == "Error: Last Name is required", "Error message for empty last name is incorrect"

# TC020: Checkout with empty postal code

def test_checkout_with_empty_postal_code(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "")
    checkout_page.continue_checkout()
    error_message = page.locator(".error-message-container").text_content()
    assert error_message == "Error: Postal Code is required", "Error message for empty postal code is incorrect"

# TC021: Cancel checkout process

def test_cancel_checkout_process(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.cancel_checkout()
    assert page.url.endswith("/cart.html"), "User is not redirected back to cart page after clicking Cancel"
    assert page.locator(".cart_item").count() == 1, "Cart item is not displayed after canceling checkout"

# TC022: Verify price calculation on checkout overview

def test_verify_price_calculation_on_checkout_overview(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.click_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.continue_checkout()
    assert overview_page.is_displayed(), "Checkout overview page is not displayed"  
    assert overview_page.get_item_total() == 29.99, "Item total is incorrect"
    assert overview_page.get_tax() == 2.40, "Tax is calculated incorrectly"
    assert overview_page.get_total() == 32.39
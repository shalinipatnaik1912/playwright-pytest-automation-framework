# Complete User Journey Tests

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage

# TC023: Happy path - Complete purchase flow

def test_complete_purchase_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.click_cart()

    # Verify all 3 items are in cart
    assert page.locator(".cart_item").count() == 3, "Not all added items are displayed in cart"
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")  
    checkout_page.continue_checkout()
    assert overview_page.is_displayed(), "Checkout overview page is not displayed"  
    assert overview_page.get_item_total() == 29.99 + 9.99 + 15.99, "Item total is incorrect"
    checkout_page.finish_button()
    assert overview_page.get_success_message() == "Thank you for your order!", "Success message is incorrect"
    checkout_page.back_home_button()
    assert page.url.endswith("/inventory.html"), "User is not redirected back to inventory page after clicking Back Home"

# TC024: Full shopping experience with modifications

def test_full_shopping_experience_with_modifications(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    
    page.goto("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")
    inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product_to_cart("Sauce Labs Fleece Jacket")
    inventory_page.click_cart()

    # Verify all 4 items are in cart
    assert page.locator(".cart_item").count() == 4, "Not all added items are displayed in cart"
    page.locator(".btn_small").first.click()
    cart_page.continue_shopping()
    inventory_page.add_product_to_cart("Sauce Labs Onesie")
    inventory_page.click_cart()
    assert page.locator(".cart_item").count() == 4, "Modified cart item count is incorrect" 
    cart_page.proceed_to_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")  
    checkout_page.continue_checkout()
    checkout_page.finish_button()
    assert overview_page.get_success_message() == "Thank you for your order!", "Success message is incorrect"
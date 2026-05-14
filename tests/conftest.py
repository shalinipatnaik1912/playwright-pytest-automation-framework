import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page_instance = context.new_page()
        yield page_instance
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    from pages.login_page import LoginPage
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    return page
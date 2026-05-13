import pytest
from pages.login_page import LoginPage
from utils.test_data import VALID_USERS, INVALID_USERS

# Test Cases for Login Functionality

# TC001: Successful login with valid credentials
    
def test_valid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(VALID_USERS["standard"]["username"], VALID_USERS["standard"]["password"])
    assert "inventory" in page.url

# TC002: Login with invalid username

def test_invalid_username(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(INVALID_USERS["invalid"]["username"], VALID_USERS["standard"]["password"])
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg # type: ignore

# TC003: Login with invalid password

def test_invalid_password(page): 
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(VALID_USERS["standard"]["username"], INVALID_USERS["invalid"]["password"])
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg # type: ignore

# TC004: Login with empty username

def test_empty_username(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login("", VALID_USERS["standard"]["password"])
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Username is required" in error_msg # type: ignore

# TC005: Login with empty password

def test_empty_password(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(VALID_USERS["standard"]["username"], "")
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Password is required" in error_msg # type: ignore

# TC006: Login with locked out user

def test_locked_out_user(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    login_page.login(INVALID_USERS["locked"]["username"], INVALID_USERS["locked"]["password"])
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out." in error_msg # type: ignore
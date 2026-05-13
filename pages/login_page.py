from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.saucedemo.com/"
    
    def navigate(self):
        super().navigate(self.url)
    
    def enter_username(self, username):
        self.fill(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)
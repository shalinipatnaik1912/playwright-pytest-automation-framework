from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        self._finish_button = page.locator("#finish")
        self._back_home_button = page.locator("#back-to-products")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):    
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    def finish_button(self):
        self._finish_button.click()

    def back_home_button(self):
        self._back_home_button.click()
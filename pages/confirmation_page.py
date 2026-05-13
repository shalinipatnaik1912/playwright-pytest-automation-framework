from .base_page import BasePage


class ConfirmationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.confirmation_message = page.locator(".complete-header")
        self.finish_button = page.locator("#finish")

    def get_confirmation_message(self):
        return self.confirmation_message.text_content()

    def finish_order(self):
        self.finish_button.click()
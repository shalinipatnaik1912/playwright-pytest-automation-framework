from .base_page import BasePage


class OverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.overview_container = page.locator(".summary_info")
        self.item_total_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def is_displayed(self):
        return self.overview_container.is_visible()

    def _parse_currency(self, label_text: str) -> float:
        if not label_text:
            return 0.0
        digits = "".join(ch for ch in label_text if ch.isdigit() or ch == '.')
        return float(digits) if digits else 0.0

    def get_item_total(self) -> float:
        return self._parse_currency(self.item_total_label.text_content())

    def get_tax(self) -> float:
        return self._parse_currency(self.tax_label.text_content())

    def get_total(self) -> float:
        return self._parse_currency(self.total_label.text_content())

    def click_finish(self):
        self.finish_button.click()

    def get_success_message(self) -> str:
        return self.success_message.text_content()

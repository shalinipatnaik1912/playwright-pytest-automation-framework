from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    INVENTORY_ITEMS = ".inventory_item"
    PRODUCT_NAME = ".inventory_item_name"
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    REMOVE_BUTTON = "button[id^='remove']"
    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    SORT_DROPDOWN = ".product_sort_container"
    
    def get_product_count(self):
        return self.get_element_count(self.INVENTORY_ITEMS)
    
    def add_product_to_cart(self, product_name):
        # Example: "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack"
        button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.click(f"#{button_id}")
    
    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"
    
    def click_cart(self):
        self.click(self.CART_ICON)
    
    def sort_products(self, option):
        self.page.select_option(self.SORT_DROPDOWN, option)
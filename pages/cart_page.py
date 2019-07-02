from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS), \
            "Items in cart is presented, but should not be"

    def should_be_cart_empty_text(self):
        assert self.browser.find_element(*CartPageLocators.CART_EMPTY_TEXT).text == 'Your basket is empty. Continue shopping', \
            "Empty cart is not presented, bot should be"

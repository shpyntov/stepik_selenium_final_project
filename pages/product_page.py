from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.solve_quiz_and_get_code()

    def item_added_message_check(self):
        MESSAGE = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_MESSAGE).text
        ITEM_NAME = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert MESSAGE == ITEM_NAME + ' has been added to your basket.'

    def basket_price_message_check(self):
        MESSAGE = self.browser.find_element(*ProductPageLocators.CART_PRICE_MESSAGE).text
        ITEM_PRICE = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert 'Your basket total is now ' + ITEM_PRICE == MESSAGE

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

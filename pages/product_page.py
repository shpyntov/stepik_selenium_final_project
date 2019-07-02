from .base_page import BasePage
from selenium.webdriver.common.by import By
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

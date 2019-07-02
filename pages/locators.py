from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner')
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner > p')


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group .btn")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    ITEMS = (By.CSS_SELECTOR, '.basket-items')
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')

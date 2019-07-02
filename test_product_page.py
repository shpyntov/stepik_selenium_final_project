from .pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.item_added_message_check()
    page.basket_price_message_check()

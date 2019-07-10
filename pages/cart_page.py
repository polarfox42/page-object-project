from .base_page import BasePage
from .locators import BasePageLocators, CartPageLocators


class CartPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def empty_cart_check(self):
        self.should_not_be_products_in_basket()
        self.should_be_empty_basket_message()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.CART_IS_NOT_EMPTY), "Cart is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY_MESSAGE), "Message is not present"
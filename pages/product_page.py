from .base_page import BasePage
from .locators import ProductPageLocators, AlertLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_to_cart(self):
        self.should_be_add_to_cart_button()
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def add_to_cart_check(self):
        self.should_be_added_to_cart_message()
        self.should_be_cart_price_message()


    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to basket button is not presented"

    def should_be_added_to_cart_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        verification_message = self.browser.find_element(*AlertLocators.ADD_PRODUCT_TO_CART_ALERT).text
        assert product_name == verification_message, "Wrong product name in message"

    def should_be_cart_price_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*AlertLocators.PRICE_ALERT).text
        assert product_price == message_price, "Wrong price in message"
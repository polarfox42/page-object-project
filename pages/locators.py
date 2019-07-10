from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, '.btn-group>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")


class AlertLocators(object):
    PRICE_ALERT = (By.CSS_SELECTOR, ".alertinner >p strong")
    ADD_PRODUCT_TO_CART_ALERT = (By.CSS_SELECTOR, ".alertinner>strong:nth-child(1)")

class CartPageLocators(object):
    CART_IS_NOT_EMPTY = (By.CSS_SELECTOR, '.basket-title')
    CART_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
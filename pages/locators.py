from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success:first-child")
    SUCCESS_PRODUCT_TITLE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    BASKET_INFO_MSG = (By.CSS_SELECTOR, ".alert-info")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")





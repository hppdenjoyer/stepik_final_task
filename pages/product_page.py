from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
   
    def add_product_to_basket(self):
        self.click_add_to_basket_button()
        # self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.is_success_product_title_correct()
        self.should_be_basket_price_message()
        self.is_basket_price_correct()

    def click_add_to_basket_button(self):
        assert self.click_on_button(*ProductPageLocators.ADD_TO_BASKET_BTN), \
            "Add to basket button is not present"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def is_success_product_title_correct(self):
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        ).text
        success_product_title = self.browser.find_element(
            *ProductPageLocators.SUCCESS_PRODUCT_TITLE
        ).text
        assert success_product_title == product_title, \
            "Success product title is not correct"

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            "Basket price info message is not present"

    def is_basket_price_correct(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text
        assert basket_price == product_price, "Basket price is not correct"



    




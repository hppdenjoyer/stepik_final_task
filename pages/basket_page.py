from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE
        ), "Basket empty message is not presented"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Products in basket is presented, but not should be"


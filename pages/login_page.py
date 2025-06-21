from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL
        )
        email_field.send_keys(email)
        password_1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_1
        )
        password_1.send_keys(password)
        password_2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_2
        )
        password_2.send_keys(password)
        submit_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_SUBMIT_BTN
        )
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not present"



from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Login not in url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login pass input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Registration pass input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Registration pass confirmation input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Registration button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

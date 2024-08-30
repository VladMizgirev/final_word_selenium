from .base_page import BasePage
from selenium import webdriver
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, 'login is not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.email_enter), "Element email_enter is not found"
        assert self.is_element_present(*LoginPageLocators.password_enter), "Element password_enter is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.email_register), "Element email_register is not found"
        assert self.is_element_present(*LoginPageLocators.password_register), "Element password_register is not found"
        assert self.is_element_present(*LoginPageLocators.password_enter_replay), "Element password_enter_replay is not found"
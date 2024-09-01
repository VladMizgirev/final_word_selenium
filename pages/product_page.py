from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from .base_page import BasePage
from .locators import ProductPageLocators



class CartPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.add_button)
        cart.click()
        time.sleep(1)
        
    def should_not_be_success_message_is_not(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_not_be_success_message_is_d(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
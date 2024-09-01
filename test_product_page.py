from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.product_page import CartPage



def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = CartPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message_is_not()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = CartPage(browser, link)
    page.open()
    page.should_not_be_success_message_is_not()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = CartPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message_is_d()
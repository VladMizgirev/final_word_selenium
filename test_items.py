from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest
import time
import math



def test_3_6_10(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
   
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button is not None, 'Такой элемент не найден!'

if __name__ == "__main__":
    pytest.main()
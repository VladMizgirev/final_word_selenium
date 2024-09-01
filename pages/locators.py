from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



class ProductPageLocators():
    add_button = (By.CLASS_NAME, 'btn-add-to-basket') 
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner') 

    
    
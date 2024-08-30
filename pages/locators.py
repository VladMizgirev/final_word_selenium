from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    email_enter = (By.ID, "id_login-username")
    password_enter = (By.ID, "id_login-password")
    email_register = (By.ID, "id_registration-email")
    password_register = (By.ID, "id_registration-password1") 
    password_enter_replay = (By.ID, "id_registration-password2") 
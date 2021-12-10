import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
import time
from types import SimpleNamespace


from webdriver_helpers import *

class Test_client_login_creation:

    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @pytest.fixture
    def account(self):
        account = SimpleNamespace()
        account.username = "Mallick"
        account.password = "qwerty123"
        self.account = account
        return account    

#-------------TESTS------------------#
# test for successful logging
    def test_client_login(self, account):
        self.homepage_site()
        self.client_login()
        self.login(account.username, account.password)
        self.logout()
        assert self.logged_in() == "Login"

#---------NAVIGATING TO SITE AND LOGIN PAGE-------------#	
    def homepage_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")        

    def client_login(self):
        login_locator = By.PARTIAL_LINK_TEXT, "Login"
        self.driver.find_element(*login_locator).click()

        client_login_locator = By.XPATH, "/html/body/div/div[3]/div/div[2]/button"
        self.driver.find_element(*client_login_locator).click()
        time.sleep(3)

        f_send_button = By.XPATH, "//button"
        self.driver.find_element(*f_send_button).click()
        time.sleep(3)

    def login(self, username, password):
        name_locator = By.XPATH, "/html/body/div/form/div[1]/input"
        self.driver.find_element(*name_locator).send_keys(username)

        password_locator = By.XPATH, "/html/body/div/form/div[2]/input"
        self.driver.find_element(*password_locator).send_keys(password)

        submit_locator = By.XPATH, "/html/body/div/form/button"
        self.driver.find_element(*submit_locator).click()

    def logout(self):
        dropdown_locator=By.XPATH,"/html/body/div/div[2]/nav/div/div[2]/ul/li/a/i" 
        self.driver.find_element(*dropdown_locator).click()
        time.sleep(4)  

        logout_locator=By.XPATH,"/html/body/div/div[2]/nav/div/div[2]/ul/li/div/a[2]"
        self.driver.find_element(*logout_locator).click()
        time.sleep(4)

        
    def logged_in(self):
        return self.driver.title




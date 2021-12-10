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

class Test_event_manager_login_creation:

    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @pytest.fixture
    def account(self):
        account = SimpleNamespace()
        account.username = "Swamy"
        account.password = "qwerty123"
        self.account = account
        return account    

#-------------TESTS------------------#
# test for successful logging
    def test_event_manager_login(self, account):
        self.homepage_site()
        self.event_manager_login()
        self.login(account.username, account.password)
        self.logout()
        assert self.logged_in() == "Login"

#---------NAVIGATING TO SITE AND LOGIN PAGE-------------#	
    def homepage_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")    

    def event_manager_login(self):
        login_locator = By.PARTIAL_LINK_TEXT, "Login"
        self.driver.find_element(*login_locator).click()

        client_login_locator = By.XPATH, "/html/body/div/div[2]/form/button"
        self.driver.find_element(*client_login_locator).click()
        time.sleep(3)


    def login(self, username, password):
        name_locator = By.XPATH, "/html/body/div/form/div[1]/input"
        self.driver.find_element(*name_locator).send_keys(username)
        time.sleep(3)

        password_locator = By.XPATH, "/html/body/div/form/div[2]/input"
        self.driver.find_element(*password_locator).send_keys(password)
        time.sleep(3)

        submit_locator = By.XPATH, "/html/body/div/form/button"
        self.driver.find_element(*submit_locator).click()
        time.sleep(3)

    def logout(self):
        logout_locator=By.XPATH,"/html/body/nav/div/div/form/button/a"  
        self.driver.find_element(*logout_locator).click()
        time.sleep(3)


    def logged_in(self):
        return self.driver.title    

    





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

class Test_event_manager_bid_creation:

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
    def test_event_manager_bid_create(self, account):
        self.homepage_site()
        self.event_manager_login()
        self.login(account.username, account.password)
        self.bid_create()
        #assert self.logged_in() == "managerdash"

#---------NAVIGATING TO SITE AND LOGIN PAGE-------------#	
    def homepage_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")    

    def event_manager_login(self):
        login_locator = By.PARTIAL_LINK_TEXT, "Login"
        self.driver.find_element(*login_locator).click()

        client_login_locator = By.XPATH, "/html/body/div/div[2]/form/button"
        self.driver.find_element(*client_login_locator).click()
        time.sleep(3)

        # f_send_button = By.XPATH, "//button"
        # self.driver.find_element(*f_send_button).click()
        # time.sleep(3)

    def login(self, username, password):
        name_locator = By.XPATH, "/html/body/div/form/div[1]/input"
        self.driver.find_element(*name_locator).send_keys(username)

        password_locator = By.XPATH, "/html/body/div/form/div[2]/input"
        self.driver.find_element(*password_locator).send_keys(password)
        time.sleep(3)

        submit_locator = By.XPATH, "/html/body/div/form/button"
        self.driver.find_element(*submit_locator).click()
        time.sleep(5)

    def bid_create(self):    
        # Bid Form
        # enter click on bid
        bid_locator= By.XPATH, "/html/body/div/div/div/table/tbody/tr/td[10]/button"
        self.driver.find_element(*bid_locator).click()
        time.sleep(4)

        # Price
        price_locator= By.XPATH, "/html/body/div/form/div[1]/input"
        self.driver.find_element(*price_locator).send_keys("11000")
        time.sleep(3)

        # comment
        comment_locator= By.XPATH, "/html/body/div/form/div[2]/textarea"
        self.driver.find_element(*comment_locator).send_keys("please check bid amount and please confirm with us")
        time.sleep(2)

        # File attach
        file_attach_locator= By.XPATH, "/html/body/div/form/div[3]/input"
        self.driver.find_element(*file_attach_locator).send_keys("C:\\Users\\Jigne\\OneDrive\\Desktop\\PAN CARD\\pan60kb.jpeg")
        time.sleep(3)

        #final submit 
        sub_button = By.XPATH, "/html/body/div/form/input"
        self.driver.find_element(*sub_button).click()
        time.sleep(5)

        #and then Logout
        logout_locator = By.LINK_TEXT, "Logout"
        self.driver.find_element(*logout_locator).click()
        time.sleep(5)

        #driver.quit()


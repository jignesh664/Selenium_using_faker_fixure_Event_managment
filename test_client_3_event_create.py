import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
    def test_client_event_creation(self, account):
        self.homepage_site()
        self.client_login()
        self.login(account.username, account.password)
        self.event_cerate()
        #assert self.logged_in() == "managerdash"

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
        time.sleep(3)

        submit_locator = By.XPATH, "/html/body/div/form/button"
        self.driver.find_element(*submit_locator).click()

    def event_cerate(self):
        #Go to dashbord
        event_locator = By.XPATH, "/html/body/div/div[2]/div[1]/div/div[1]/div[1]/a/div/div[1]/div/i"
        self.driver.find_element(*event_locator).click()
        time.sleep(2)

        #event_form:
        #username
        username_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[1]/input"
        self.driver.find_element(*username_locator).send_keys("Mallick")
        time.sleep(2)

        #location
        location_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[2]/select"
        self.driver.find_element(*location_locator).send_keys("Ahmedabad")
        time.sleep(2)

        #Attendence
        Attendence_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[3]/div[1]/div/input"
        self.driver.find_element(*Attendence_locator).send_keys("100")
        time.sleep(2)

        #Budget
        budget_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[3]/div[2]/div/input"
        self.driver.find_element(*budget_locator).send_keys("12000")
        time.sleep(2)


        #for scrolldown one step
        self.driver.execute_script("window.scrollTo(0,300);")
        time.sleep(2)

        #venue_type
        venue_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/input[1]"
        self.driver.find_element(*venue_locator).click()
        time.sleep(2)

        # Event Duration
        ed_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[4]/div[1]/div/input"
        self.driver.find_element(*ed_locator).send_keys("1")
        time.sleep(2)

        # Event Time
        et_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[4]/div[2]/div/input"
        date=self.driver.find_element(*et_locator)
        action:ActionChains=ActionChains(self.driver)
        action.click(date)
        action.send_keys("10112021")
        action.send_keys(Keys.TAB)
        action.send_keys("0330")
        action.send_keys("P")
        action.perform()
        time.sleep(3)

        #for scrolldown one step
        self.driver.execute_script("window.scrollTo(300,600);")
        time.sleep(3)

        # choose event type
        cet_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/input[5]"
        self.driver.find_element(*cet_locator).click()
        time.sleep(2)

        # Description
        dn_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[5]/textarea"
        self.driver.find_element(*dn_locator).send_keys("I went to require event manager for my son wedding")
        time.sleep(2)

        #for scrolldown one step
        self.driver.execute_script("window.scrollTo(600,900);")
        time.sleep(2)

        #final submit 
        sub_button = By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[6]/input"
        self.driver.find_element(*sub_button).click()
        time.sleep(2)

    #driver.quit()


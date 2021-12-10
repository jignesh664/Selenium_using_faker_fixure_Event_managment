import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
import time
from types import SimpleNamespace

from faker import Faker

from webdriver_helpers import *

class Test_signup_creation:

    @pytest.fixture(autouse=True)
    def setup(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fake = Faker(locale="en_IN")

    @pytest.fixture
    def account(self):
        self.name =self.fake.first_name()
        self.username =self.fake.last_name()
        self.email =self.fake.email()
        self.password = "qwerty123"
        self.c_password = "qwerty123"
        self.mobile =self.fake.phone_number()

#----------TESTS--------#
# test for successful signup 
    def test_client_signup_creation(self, account):
        self.homepage_site()
        self.client_signup()
        self.signup(self.name,self.username,self.email,self.password,self.c_password,self.mobile)
        assert self.signed_in() == "Login"

#-----NAVIGATING TO SITE AND SIGNUP PAGE------#       

    def homepage_site(self):
        self.driver.get("http://localhost/AD-event-management-main/HomePage/rishabh/")

      
    def client_signup(self):
        signup_locator = By.LINK_TEXT, "SignUp"
        self.driver.find_element(*signup_locator).click()
        time.sleep(3)

        send_button = By.XPATH, "/html/body/div/div[3]/div/div[2]/button"
        self.driver.find_element(*send_button).click()
        time.sleep(3)

        f_send_button = By.XPATH, "//button"
        self.driver.find_element(*f_send_button).click()
        time.sleep(3)  

    def signup(self, name,username,email,password,c_password,mobile):
        name_locator = By.XPATH,"/html/body/form/div[1]/input"
        self.driver.find_element(*name_locator).send_keys(name)

        user_name_locator= By.XPATH, "/html/body/form/div[2]/input"
        self.driver.find_element(*user_name_locator).send_keys(username)

        email_locator= By.XPATH, "/html/body/form/div[3]/input"
        self.driver.find_element(*email_locator).send_keys(email)

        password_locator = By.XPATH, "/html/body/form/div[4]/input"
        self.driver.find_element(*password_locator).send_keys(password)

        c_password_locator= By.XPATH, "/html/body/form/div[5]/input"
        self.driver.find_element(*c_password_locator).send_keys(c_password)

        mobile_locator= By.XPATH, "/html/body/form/div[6]/input"
        self.driver.find_element(*mobile_locator).send_keys(mobile)

        #for scrolldown
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        submit_locator = By.XPATH, "/html/body/form/button[1]"
        self.driver.find_element(*submit_locator).click()

    def signed_in(self):
        return self.driver.title

          
    

    












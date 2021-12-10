import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



from webdriver_helpers import get_chrome_options 

@pytest.fixture
def driver():
    options=get_chrome_options()  
    print(options) 
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    sleep(10)
    driver.quit()
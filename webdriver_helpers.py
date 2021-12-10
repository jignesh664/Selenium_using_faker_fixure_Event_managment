import os
from socket import gethostname
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver


def running_on_pythonanywhere():
    if "console" in gethostname():
        return True
    return False

def get_chrome_options():
    chrome_options=webdriver.ChromeOptions()

    if running_on_pythonanywhere():
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

    return chrome_options

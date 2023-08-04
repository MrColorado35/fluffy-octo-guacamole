from time import sleep
from selenium.webdriver.common.by import By
import pymongo
from pymongo import MongoClient
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver
from random import randrange
from selenium import webdriver
# from selenium_proxy import SeleniumProxy 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Yes, I know how to correctly spell "Clear", but if I did, then it would not short to my initials

class Selenium_Clear:
    def __init_(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.params = ({'in_progress': 0, 'failed': 0, 'complete': 0})
        # self.driver = self.start_driver(proxy=False)

     # Create and start the driver  
    @staticmethod
    def start_driver():
        # if proxy == True:
        #     SP = SeleniumProxy()
        #     self.driver = SP.get_ip_via_chrome()
        # else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version="114.0.5735.16").install()))
        return driver


    """Call the driver and open required page. In case if we won't provide any url, it will go to the deafault one"""
    def open_page(self, website=""):
        # Variable "website" should be specified every time before running it, but in case if it was left blank we need a page that will do no harm to our program
        if website == "":
            website = "https://www.sportinglife.com/racing/fast-results"
        else:
            website == website
        self.main_url = website
        self.driver.get(self.main_url)
        # Depending on the URL, some delay is required for program to wait until the website is fully loaded. That part will be replaced with WebDriverWait when I can spent some time poilishing this program
        sleep(4)

    """This function will take care of clicking any button.
    At the moment it only can search by ID or CSS selector, extend 'except' in case if you need Xpath/ Name etc.
    Just pass the string with search criteria for the driver and call it in your code
    """
    @staticmethod
    def click_btn(driver, btn):
        try:
            click_me = driver.find_element(By.ID, btn)
            print("GOT THE ID")
        except:
            click_me = driver.find_element(By.CSS_SELECTOR, btn)
            print("GOT THE CSS SELECTOR")
            
        click_me.click()
        sleep(3)


if __name__ == '__main__':
    Selenium_Clear()
    app = Selenium_Clear()
    driver = app.start_driver()
    website = "https://www.sportinglife.com/racing/fast-results#"
    app.open_page(website)
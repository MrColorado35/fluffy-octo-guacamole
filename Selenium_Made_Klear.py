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
from selenium_proxy import SeleniumProxy 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Yes, I know how to correctly spell "Clear", but if I did, then it would not short to my initials

class Selenium_Clear:
    def __init_(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.params = ({'in_progress': 0, 'failed': 0, 'complete': 0})

     # Create and start the driver  
    def start_driver(self, proxy=""):
        if proxy != "":
            SP = SeleniumProxy()
            self.driver = SP.get_ip_via_chrome()
        else:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return self.driver






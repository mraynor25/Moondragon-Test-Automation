#How to check broken links
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_find_Broken_Links():

    def listALLBrokenLinks(self):
        Links = self.driver.find_elements_by_tag_name("a")
        for link in Links:
            r = requests.head(link.get_attribute('href'))
            print(link.get_attribute('href'), r.status_code)
            if r.status_code>= 400:
                print("This link is broken link= ",link.get_attribute('href'))
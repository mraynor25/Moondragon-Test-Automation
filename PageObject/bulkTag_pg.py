import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class bulkQueryPage():
    # Locators of all the elements
    addBulk_xpath = "//span[contains(text(),'Bulk Add Tag')]"
    bulkAddTagHeader_xpath = "//h1[contains(text(),'Bulk Add Tag')]"
    createTag_xpath = "//button[contains(text(),'Create Tag')]"



    def __init__(self,driver):
        self.driver = driver

    def click_addBulkMenu(self):
        click_addbulk = self.driver.find_elements(By.XPATH, self.addBulk_xpath)
        click_addbulk[0].click()


    def wait4bulkTagPagetoLoad(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.bulkAddTagHeader_xpath))
                   )


    def click_createTag(self):
        click_createTag = self.driver.find_elements(By.XPATH, self.createTag_xpath)
        click_createTag[0].click()

















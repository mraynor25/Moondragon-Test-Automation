import time


class securityPage():
    # Locators of all the elements
    rulesMenu_xpath = "//span[contains(text(),'Rules')]"



    def __init__(self,driver):
        self.driver = driver


    def clickRulesMenu(self):
        rules = self.driver.find_elements_by_xpath(self.rulesMenu_xpath)
        rules[0].click()
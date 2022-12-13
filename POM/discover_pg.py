from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DiscoverPage():
        # Locators of all the elements
        open_indexDropdown_xpath = "//*/section[1]/div[1]/div[1]/div[1]/button[1]/span[1]/*[1]"
        selectECS_xpath = "//span[contains(text(),'ecs-*')]"
        openDate_xpath = "//*[@id='QuickSelectPopover']/div[1]/button[1]/span[1]/*[1]"
        selectLastOption_xpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
        EnterNumOfYear_xpath = "//*/fieldset[1]/div[3]/div[2]/div[1]/div[1]/input[1]"
        SelectYear_xpath = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
        clickApply_xpath = "//span[contains(text(),'Apply')]"
        enterKQL_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
        clickUpdate_xpath = "//span[contains(text(),'Update')]"
        clickArrow_xpath = "//tbody/tr[1]/td[1]/button[1]/icon[1]/*[1]"




        def __init__(self, driver):
               self.driver = driver

        def OpenIndexDropdown(self):
                OpenIndexDropdown = self.driver.find_elements_by_xpath(self.open_indexDropdown_xpath)
                OpenIndexDropdown[0].click()

        def selectECSdropdown(self):
                ecs_option2 = self.driver.find_elements_by_xpath(self.selectECS_xpath)
                ecs_option2[0].click()

        def openDate(self):
                OpenDate2 = self.driver.find_elements_by_xpath(self.openDate_xpath)
                OpenDate2[0].click()

        def selectDropdownLast(self):
                dropdownLast = self.driver.find_element_by_xpath(self.selectLastOption_xpath)
                select2 = Select(dropdownLast)
                select2.select_by_value("last")

        def EnterNumberYear(self, numOfyear):
                enterNumber = self.driver.find_elements_by_xpath(self.EnterNumOfYear_xpath)
                if enterNumber[0].get_attribute('value') != "3":
                        enterNumber[0].send_keys(Keys.CONTROL + "a")
                        enterNumber[0].send_keys(Keys.DELETE)
                        enterNumber[0].send_keys(numOfyear)

        def selectYear(self):
                selectYear = self.driver.find_element_by_xpath(self.SelectYear_xpath)
                select3 = Select(selectYear)
                select3.select_by_value("y")

        def clickApply(self):
                clickApply = self.driver.find_elements_by_xpath(self.clickApply_xpath)
                clickApply[0].click()

        def enterKQLInput(self, KQLInput):
                enterKQL = self.driver.find_elements_by_xpath(self.enterKQL_xpath)
                enterKQL[0].send_keys(Keys.CONTROL + "a")
                enterKQL[0].send_keys(Keys.DELETE)
                enterKQL[0].send_keys(KQLInput)

        def clickUpdate(self):
                PressUpdate = self.driver.find_elements_by_xpath(self.clickUpdate_xpath)
                PressUpdate[0].click()

        def scrollDownResult(self):
                self.driver.execute_script("window.scrollBy(0,400)", "")

        def clickArrowToExpand(self):
                clickArrow = self.driver.find_elements_by_xpath(self.clickArrow_xpath)
                clickArrow[0].click()

        def scrollDownExpandedResult(self):
                self.driver.execute_script("window.scrollBy(0,200)", "")






from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import glob

class ArkimePage():
        # Locators of all the elements
        clickDropArrow_xpath = "//button[contains(@class, 'dropdown-toggle')]"
        clickExportPCAPButton_xpath = "//a[@class='dropdown-item']"
        clickPlusIcon_xpath = "//a[contains(@class, 'collapsed btn-theme-tertiary')]"
        clickDownloadPCAP_xpath = "//*/td[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]"



        def __init__(self, driver):
               self.driver = driver

        def clickDropArrow(self):
                clickdropArrow = self.driver.find_elements_by_xpath(self.clickDropArrow_xpath)
                clickdropArrow[0].click()

        def clickExportPCAP(self):
                clickExportPCAP = self.driver.find_elements_by_xpath(self.clickExportPCAPButton_xpath)
                clickExportPCAP[0].click()

        def clickPlusIcon(self):
                clickPlusicon = self.driver.find_elements_by_xpath(self.clickPlusIcon_xpath)
                clickPlusicon[0].click()

        def downloadPCAPTime(self):
                list_of_files_before_download = glob.glob('C:/Users/Desktop/*.pcap')

                # Get the loop start time ( current time)
                start = time.time()
                # this is the time in seconds , we set to zero initially
                elapsed = 0

                # get file list before download
                list_of_files_before_download = glob.glob('C:/Users/mraynor/*.pcap')
                start = time.time()

                clickDownloadPCAP = self.driver.find_elements_by_xpath(self.clickDownloadPCAP_xpath)
                clickDownloadPCAP[0].click()

                list_of_files_after_download = glob.glob('C:/Users/mraynor/*.pcap')
                done = time.time()
                elapsed = done - start
                return (elapsed)

                # get new file list
                list_of_files_after_download = glob.glob('C:/Users/mraynor/*.pcap')
                newfile = \
                        list(set(list_of_files_after_download).difference(list_of_files_before_download))



        #_____________-----------

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
                KQL = "KQLInput"
                enterKQL[0].send_keys(KQL)

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



# -------------------------

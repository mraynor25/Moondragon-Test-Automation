from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class saveQueryDashboardPage():
        # Locators of all the elements
        button_openDate_xpath = "//*[@id='QuickSelectPopover']/div[1]/button[1]/span[1]/*[1]"
        click_1year_xpath = "//button[contains(text(),'Last 1 year')]"
        textbox_enterQuery_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
        button_update_xpath = "//span[contains(text(),'Update')]"
        click_openSaveQuery_xpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
        button_saveQuery_xpath = "//span[contains(text(),'Save current query')]"
        VerifySavedQuery_xpath = "//*/div[6]/div[3]/div[1]/div[1]/div[1]/div[1]"
        textbox_QueryName_name = "title"
        Toggle_TimeOn_name = "shouldIncludeTimefilter"
        button_save_xpath = "//span[contains(text(),'Save')]"
        alertMessage_xpath = "//span[contains(text(),'Your query \"IP_Trojan_Query\" was saved')]"
        clickShare_xpath = "//span[contains(text(),'Share')]"
        click_permalink_xpath = "//span[contains(text(),'Permalinks')]"
        check_radioButton_snapshot = "//label[@class='euiRadio__label']"
        click_copylink_xpath = "//span[contains(text(),'Copy link')]"
        click_logout_xpath = "//*/div[1]/button[1]/div[1]/span[1]"
        click_logoutlink_linktext = "Log out"
        get_savedquerytext_xpath = "//span[contains(text(),'IP_Trojan_Query')]"
        click_savedquery_xpath = "//span[contains(text(),'IP_Trojan_Query')]"
        get_querytextTextbox_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
        get_lastValue_xpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
        get_drop_down_xpath = "//div[@class='euiFlexItem']/div[1]/div[1]/input[1]"
        get_year_xpath = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
        openSavedIcon_xpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
        clickDeleteIcon_xpath = "//button[contains(@class, 'ButtonIcon--danger euiListGroupItem__extraAction')]"
        deleteButton_xpath = "//span[contains(text(),'Delete')]"

        def __init__(self, driver):
               self.driver = driver

        def scrollUp(self):
               self.driver.execute_script("scroll(0, 0);")

        def openCalenderDate(self):
                OpenDate2 = self.driver.find_elements_by_xpath(self.button_openDate_xpath)
                OpenDate2[0].click()

        def selectYear(self):
                SelectYear = self.driver.find_elements_by_xpath(self.click_1year_xpath)
                SelectYear[0].click()


        def EnterQuery(self, Query):
                Enterquery = self.driver.find_elements_by_xpath(self.textbox_enterQuery_xpath)

                Enterquery[0].send_keys(Keys.CONTROL + "a")
                Enterquery[0].send_keys(Keys.DELETE)
                Enterquery[0].send_keys(Query)

        def clickUpdate(self):
                PressUpdate = self.driver.find_elements_by_xpath(self.button_update_xpath)
                PressUpdate[0].click()
        def clickSavedQuery(self):
                OpenSaveQuery1 = self.driver.find_elements_by_xpath(self.click_openSaveQuery_xpath)
                OpenSaveQuery1[0].click()

        def clickSaveCurrentQuery(self):
                SaveCurrentQuery = self.driver.find_elements_by_xpath(self.button_saveQuery_xpath)
                SaveCurrentQuery[0].click()

        def SavedQueryText(self):
                myquery = self.driver.find_elements_by_xpath(self.VerifySavedQuery_xpath)[0].text
                return (myquery)


        def EnterName(self, IPtitleName):
                self.driver.find_element_by_name(self.textbox_QueryName_name).send_keys(IPtitleName)

        def clickToggleOnTimeFilter(self):
                ToggleOn = self.driver.find_elements_by_name(self.Toggle_TimeOn_name)
                ToggleOn[0].click()

        def clickSave(self):
                press_save = self.driver.find_elements_by_xpath(self.button_save_xpath)
                press_save[0].click()

        def capture_alert_msg(self):
                getAlertMsg = self.driver.find_elements_by_xpath(self.alertMessage_xpath)[0].text
                return (getAlertMsg)


        def clickShare(self):
                clickshare = self.driver.find_elements_by_xpath(self.clickShare_xpath)
                clickshare[0].click()

        def clickPermalink(self):
                Permalinks = self.driver.find_elements_by_xpath(self.click_permalink_xpath)
                Permalinks[0].click()

        def checkRadioButton(self):
                radio_button_snapshot = self.driver.find_elements_by_xpath(self.check_radioButton_snapshot)
                radio_button_snapshot[0].click()

        def clickCopylink(self):
                copylink = self.driver.find_elements_by_xpath(self.click_copylink_xpath)
                copylink[0].click()

        def logOut(self):
                Logoutmenu = self.driver.find_elements_by_xpath(self.click_logout_xpath)
                Logoutmenu[0].click()

        def logoutMenu(self):
                self.driver.find_element_by_link_text(self.click_logoutlink_linktext).click()


        def gettosavedquerylink(self):
                gettosavequery = self.driver.find_elements_by_xpath(self.get_savedquerytext_xpath)[0].text
                return (gettosavequery)

        def clicksavedquery(self):
                Savedquery = self.driver.find_elements_by_xpath(self.click_savedquery_xpath)
                Savedquery[0].click()


# Verify that KQL is pre-populated for the saved query
        def getQuerytext(self):
                Verifyquery = self.driver.find_elements_by_xpath(self.get_querytextTextbox_xpath)[0].text
                return (Verifyquery)

        # Verify year matches for the saved query
        def checkLastvalue(self):
                CheckLast = self.driver.find_elements_by_xpath(self.get_lastValue_xpath)
                return CheckLast[0].get_attribute('value')


        def checknumberYear(self):
                Date_dropdownmenu1 = self.driver.find_elements_by_xpath(self.get_drop_down_xpath)
                return Date_dropdownmenu1[0].get_attribute('value')

        def getYear(self):
                CheckDate2 = self.driver.find_elements_by_xpath(self.get_year_xpath)
                return CheckDate2[0].get_attribute('value')


        def closeCalenderpicker(self):
                OpenDate2 = self.driver.find_elements_by_xpath(self.button_openDate_xpath)
                OpenDate2[0].click()

        def openSavedQuery(self):
                OpenSaveIcon = self.driver.find_elements_by_xpath(self.openSavedIcon_xpath)
                OpenSaveIcon[0].click()

        def deleteQuery(self):
                clickdeleteIcon = self.driver.find_elements_by_xpath(self.clickDeleteIcon_xpath)
                if clickdeleteIcon[0].get_attribute('title') == "Delete saved query IP_Trojan_Query":
                    clickdeleteIcon[0].click()

        def clickDeleteButton(self):
                deleteButton = self.driver.find_elements_by_xpath(self.deleteButton_xpath)
                deleteButton[0].click()



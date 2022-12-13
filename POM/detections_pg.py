from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class detectionsPage():
    # Locators of all the elements

    button_manageDetection_xpath = "//span[contains(text(),'Manage detection rules')]"
    button_createNewRule_xpath = "//span[contains(text(),'Create new rule')]"
    getText_customQuery_xpath = "//span[contains(text(),'Selected')]"
    selectCustomQuery_xpath = "//span[contains(text(),'Selected')]"
    IndexPatternField_xpath = "//button[@class='euiFormControlLayoutClearButton']/*[1]"
    enterIndex_xpath = "//div[@class='euiComboBox__input']/input[1]"
    QueryTextbox_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/*[1]"
    QueryPreview_xpath = "//*[@id='queryPreviewSelect']/option[1]"
    continueButton_xpath = "//span[contains(text(),'Continue')]"
    nameField_xpath = "//input[contains(@class, 'euiFieldText--fullWidth')]"
    descriptionField_xpath = "//*[contains(@class, 'euiTextArea--compressed')]"
    severityDropdown_xpath = "//button[contains(@class, 'euiSuperSelectControl')]"
    selectHigh_xpath = "//div[contains(text(),'High')]"
    tagTextbox_xpath = "//*[@class='euiComboBox__input']/input[1]"
    runsEveryField_xpath = "//input[contains(@class, 'euiFieldNumber')]"
    runsEveryDropdown_xpath = "//select[contains(@class, 'MyEuiSelect-d3i8n6-2')]"
    additionalLookback_xpath = "//*/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    additionalLookbackDropdown_xpath = "//*//div[2]/div[2]/div[1]/div[2]/div[1]/select[1]"
    actionFreqDropdown_xpath = "//select[contains(@class,'euiSelect')]"



    def __init__(self, driver):
        self.driver = driver


    def clickManageDetections(self):
        Manage_detection = self.driver.find_elements_by_xpath(self.button_manageDetection_xpath)
        Manage_detection[0].click()

    def clickCreateRule(self):
        CreateNewrule = self.driver.find_elements_by_xpath(self.button_createNewRule_xpath)
        CreateNewrule[0].click()

    def selectCustomQuery(self):
        SelectCustom = self.driver.find_elements_by_xpath(self.getText_customQuery_xpath)[0].text
        SelectCustomClick = self.driver.find_elements_by_xpath(self.selectCustomQuery_xpath)
        if SelectCustom != "Selected":
            SelectCustomClick[0].click()

    def scrollDownpg(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")

    def ClearIndexPattern(self):
        Remove_IndexPatten = self.driver.find_elements_by_xpath(self.IndexPatternField_xpath)
        Remove_IndexPatten[0].click()

    def enterIndexPattern_zeek(self, index1):
        EnterIndex2 = self.driver.find_elements_by_xpath(self.enterIndex_xpath)
        EnterIndex2[0].send_keys(index1)
        EnterIndex2[0].send_keys(Keys.ENTER)

    def enterIndexPattern_ecs(self, index2):
        EnterIndex3 = self.driver.find_elements_by_xpath(self.enterIndex_xpath)
        EnterIndex3[0].send_keys(index2)
        EnterIndex3[0].send_keys(Keys.ENTER)

    def enterQuery(self, KQL):
        QueryTextbox = self.driver.find_elements_by_xpath(self.QueryTextbox_xpath)
        QueryTextbox[0].send_keys(KQL)

    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0,100)", "")

    def clickQueryPreview(self):
        Query_preview = self.driver.find_elements_by_xpath(self.QueryPreview_xpath)
        Query_preview[0].click()

    def clickContinue(self):
        Continue = self.driver.find_elements_by_xpath(self.continueButton_xpath)
        Continue[0].click()

    def scrolluptoView(self):
        self.driver.execute_script("window.scrollBy(0,-150)", "")

    def enterName(self, name):
        EnterName = self.driver.find_elements_by_xpath(self.nameField_xpath)
        EnterName[0].send_keys(name)

    def enterDescription(self, desc):
        EnterDesc = self.driver.find_elements_by_xpath(self.descriptionField_xpath)
        EnterDesc[0].send_keys(desc)

    def selectSeverityDropdown(self):
        Severity_dropdown = self.driver.find_elements_by_xpath(self.severityDropdown_xpath)
        Severity_dropdown[0].click()
        Select_high = self.driver.find_elements_by_xpath(self.selectHigh_xpath)
        Select_high[0].click()

    def scrollDownslightly(self):
        self.driver.execute_script("window.scrollBy(0,200)", "")

    def TypefirstTag(self, tag1):
        Tag = self.driver.find_elements_by_xpath(self.tagTextbox_xpath)
        Tag[0].send_keys(tag1)
        Tag[0].send_keys(Keys.ENTER)

    def TypesecondTag(self, tag2):
        Tag = self.driver.find_elements_by_xpath(self.tagTextbox_xpath)
        Tag[0].send_keys(tag2)
        Tag[0].send_keys(Keys.ENTER)

    def scrollDown(self):
        self.driver.execute_script("window.scrollBy(0,100)", "")

    def enterRunsEvery(self, RunsEveryValue):

        Runs_every = self.driver.find_elements_by_xpath(self.runsEveryField_xpath)
        if Runs_every[0].get_attribute('value') != "5":
            Runs_every[0].clear()
            Runs_every[0].send_keys(RunsEveryValue)

    def selectRunsEveryDropdown(self, min):
        Select_Runevery_dropdown = self.driver.find_element_by_xpath(self.runsEveryDropdown_xpath)
        select = Select(Select_Runevery_dropdown)
        select.select_by_value(min)

    def enterAdditionalLookback(self, time):
        Additional_Lookback_time = self.driver.find_elements_by_xpath(self.additionalLookback_xpath)
        if Additional_Lookback_time[0].get_attribute('value') != "720":
            Additional_Lookback_time[0].clear()
            Additional_Lookback_time[0].send_keys(time)

    def selectAdditionalLookback(self):
        Select_Additional_Lookback_time = self.driver.find_element_by_xpath(self.additionalLookbackDropdown_xpath)
        select = Select(Select_Additional_Lookback_time)
        select.select_by_value("h")

    def selectActionFreq(self):
        Select_Actions_Freq = self.driver.find_element_by_xpath(self.actionFreqDropdown_xpath)
        select = Select(Select_Actions_Freq)
        select.select_by_value("rule")









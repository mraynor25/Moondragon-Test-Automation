import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import json


class rulesPage():
    # Locators of all the elements
    createNewrule_xpath = "//span[contains(text(),'Create new rule')]"
    QueryOption_xpath = "//span[contains(text(),'Selected')]"
    threshold_xpath = "//*/div[2]/div[1]/div[3]/div[1]/button[1]/span[1]"
    removeIndexPatten_xpath = "//button[@class='euiFormControlLayoutClearButton']/*[1]"
    indexfield_xpath = "//div[@class='euiComboBox__input']/input[1]"
    queryTextbox_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/*[1]"
    thresholdValue_xpath = "//input[contains(@class, 'euiFieldNumber--fullWidth')]"
    continueButton_xpath = "//span[contains(text(),'Continue')]"
    nameTextbox_xpath = "//input[contains(@class, 'euiFieldText--fullWidth')]"
    descTextbox_xpath = "//*[contains(@class, 'euiTextArea--compressed')]"
    severityDropdown_xpath = "//button[contains(@class, 'euiSuperSelectControl')]"
    mediumSeverity_xpath = "//div[contains(text(),'Medium')]"
    highSeverity_xpath = "//div[contains(text(),'High')]"
    tagsField_xpath = "//*[@class='euiComboBox__input']/input[1]"
    runEvery_xpath = "//input[contains(@class, 'euiFieldNumber')]"
    runEveryMin_xpath = "//select[contains(@class, 'MyEuiSelect-sc-d3i8n6-2')]"
    additional_lookback_xpath = "//*/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    additional_lookback2_xpath = "//*//div[2]/div[2]/div[1]/div[2]/div[1]/select[1]"
    action_freq_xpath = "//select[contains(@class,'euiSelect')]"
    webhook_option_xpath = "//span[contains(text(),'Webhook')]"
    jsonBody_xpath = "//textarea[contains(@class, 'monaco-mouse-cursor-text')]"
    actionRule_xpath = "//span[contains(text(),'Create & activate rule')]"
    capture_createdMsg_xpath = "//*/body[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]"



    def __init__(self,driver):
        self.driver = driver


    def clickCreateNewRule(self):
        CreateNewrule = self.driver.find_elements_by_xpath(self.createNewrule_xpath)
        CreateNewrule[0].click()


    def clickCustomQuery(self):
        SelectCustom2 = self.driver.find_elements_by_xpath(self.QueryOption_xpath)[0].text
        SelectCustomClick = self.driver.find_elements_by_xpath(self.QueryOption_xpath)
        if SelectCustom2 != "Selected":
            SelectCustomClick[0].click()


    def select_Threshold(self):
        SelectThreshold = self.driver.find_elements_by_xpath(self.threshold_xpath)
        SelectThreshold[0].click()


    def removeIndexPatten(self):
        Remove_IndexPatten2 = self.driver.find_elements_by_xpath(self.removeIndexPatten_xpath)
        Remove_IndexPatten2[0].click()


    def enter_index(self, index1, index2, index3):
        EnterIndex3 = self.driver.find_elements_by_xpath(self.indexfield_xpath)
        EnterIndex3[0].send_keys(index1)
        EnterIndex3[0].send_keys(Keys.ENTER)
        EnterIndex3[0].send_keys(index2)
        EnterIndex3[0].send_keys(Keys.ENTER)
        EnterIndex3[0].send_keys(index3)
        EnterIndex3[0].send_keys(Keys.ENTER)

    def enter_QueryTextbox(self, Query):
        QueryTextbox = self.driver.find_elements_by_xpath(self.queryTextbox_xpath)
        # QueryTextbox[0].send_keys("related.ip: \"144.121.162.12\" or related.ip: \"79.124.62.82\"")
        # QueryTextbox[0].send_keys("target_index: \"wildfire\" AND wildfire.CakeStatic.extracted_urls.url_2: \"http://www.microsoft.com/pki/certs/MicRooCerAut_2010-06-23.crt0\"")
        # QueryTextbox[0].send_keys("observer.filename: \"DD-03-210830.cap\" AND NOT event.category: \"network\"")
        QueryTextbox[0].send_keys(Query)

    def enter_threshold(self, threshold_value):
        EnterThreshold = self.driver.find_elements_by_xpath(self.thresholdValue_xpath)
        if EnterThreshold[0].get_attribute('value') != threshold_value:
            EnterThreshold[0].send_keys(Keys.CONTROL + "a")
            EnterThreshold[0].send_keys(Keys.DELETE)
            EnterThreshold[0].send_keys(threshold_value)

    def clickContinue(self):
        Continue = self.driver.find_elements_by_xpath(self.continueButton_xpath)
        Continue[0].click()

    def enter_name(self, name):
        EnterName = self.driver.find_elements_by_xpath(self.nameTextbox_xpath)
        EnterName[0].send_keys(name)

    def enter_desc(self, desc):
        EnterDesc = self.driver.find_elements_by_xpath(self.descTextbox_xpath)
        EnterDesc[0].send_keys(desc)

    def clickSeverity_dropdown(self):
        Severity_dropdown = self.driver.find_elements_by_xpath(self.severityDropdown_xpath)
        Severity_dropdown[0].click()

    def selectMedium(self):
        Select_Medium = self.driver.find_elements_by_xpath(self.mediumSeverity_xpath)
        Select_Medium[0].click()


    def selectHigh(self):
        Select_high = self.driver.find_elements_by_xpath(self.highSeverity_xpath)
        Select_high[0].click()

    def enter_tags(self, tag1, tag2, tag3):
        Tag = self.driver.find_elements_by_xpath(self.tagsField_xpath)
        time.sleep(5)
        Tag[0].send_keys(tag1)
        time.sleep(2)
        Tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Tag[0].send_keys(tag2)
        time.sleep(2)
        Tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Tag[0].send_keys(tag3)
        time.sleep(2)
        Tag[0].send_keys(Keys.ENTER)


    def RunEvery(self, run_num):
        Runs_every = self.driver.find_elements_by_xpath(self.runEvery_xpath)
        if Runs_every[0].get_attribute('value') != run_num:
            Runs_every[0].clear()
            Runs_every[0].send_keys(run_num)


    def runEvery_min(self, min):
        Select_Runevery_dropdown = self.driver.find_element_by_xpath(self.runEveryMin_xpath)
        select = Select(Select_Runevery_dropdown)
        select.select_by_value(min)


    def select_additional_lookback(self, time):
        Additional_Lookback_time = self.driver.find_elements_by_xpath(self.additional_lookback_xpath)
        if Additional_Lookback_time[0].get_attribute('value') != time:
            Additional_Lookback_time[0].clear()
            Additional_Lookback_time[0].send_keys(time)


    def select_additional_lookback2(self, hour):
        Select_Additional_Lookback_time = self.driver.find_element_by_xpath(self.additional_lookback2_xpath)
        select = Select(Select_Additional_Lookback_time)
        select.select_by_value(hour)

    def selectRuleAction_freq(self):
        Select_Actions_Freq = self.driver.find_element_by_xpath(self.action_freq_xpath)
        select = Select(Select_Actions_Freq)
        select.select_by_value("rule")



    def select_webhook(self):
        select_webhook = self.driver.find_elements_by_xpath(self.webhook_option_xpath)
        select_webhook[0].click()

    def enter_json(self, json_text):

        jsonToEnter = {
            "text": json_text
        }

        EnterBody = self.driver.find_elements_by_xpath(self.jsonBody_xpath)
        EnterBody[0].send_keys(json.dumps(jsonToEnter))

    def clickActionRule(self):
        ActionRule = self.driver.find_elements_by_xpath(self.actionRule_xpath)
        ActionRule[0].click()

    def capture_createdMsg(self):
        captureCreated_Msg = self.driver.find_element_by_xpath(self.capture_createdMsg_xpath).text
        return captureCreated_Msg


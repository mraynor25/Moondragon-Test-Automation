from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class createNewRulePage():
    # Locators of all the elements

    select_customOption_xpath = "//span[contains(text(),'Selected')]"
    clear_indexPattern_xpath = "//button[@class='euiFormControlLayoutClearButton']/*[1]"
    enter_indexPattern_xpath = "//div[@class='euiComboBox__input']/input[1]"
    textbox_query_xpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/*[1]"
    query_preview_xpath = "//*[@id='queryPreviewSelect']/option[1]"
    click_continue_xpath = "//span[contains(text(),'Continue')]"
    enter_name_xpath = "//input[contains(@class, 'euiFieldText--fullWidth')]"
    enter_desc_xpath = "//*[contains(@class, 'euiTextArea--compressed')]"
    severity_dropdown_xpath = "//button[contains(@class, 'euiSuperSelectControl')]"
    selectSeverity_high_xpath = "//div[contains(text(),'High')]"
    textbox_tag_xpath = "//*[@class='euiComboBox__input']/input[1]"
    input_runsEvery_xpath = "//input[contains(@class, 'euiFieldNumber')]"
    select_runsEvery_xpath = "//select[contains(@class, 'MyEuiSelect-d3i8n6-2')]"
    additionalLookback_xpath = "//*/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    select_additionalHour_xpath = "//*//div[2]/div[2]/div[1]/div[2]/div[1]/select[1]"
    select_actionFreq_xpath = "//select[contains(@class,'euiSelect')]"
    select_actionType_xpath = "//*/div[6]/div[7]/button[1]/div[1]"
    webhook_option_xpath = "//button[contains(@class, 'LayoutCustomIcon--click')]/*[1]"
    select_mattermost = "//span[contains(text(),'Mattermost-ElasticAlert')]"
    button_activateRule = "//span[contains(text(),'Create & activate rule')]"



    def __init__(self, driver):
        self.driver = driver


    def clickManageDetections(self):
        SelectCustom2 = self.driver.find_elements_by_xpath(self.select_customOption_xpath)[0].text
        SelectCustomClick = self.driver.find_elements_by_xpath(self.select_customOption_xpath)
        if SelectCustom2 != "Selected":
            SelectCustomClick[0].click()

    def scrollDownPage(self):
        self.driver.execute_script("window.scrollBy(0,500)", "")

    def clearIndex(self):
        Remove_IndexPatten = self.driver.find_elements_by_xpath(self.clear_indexPattern_xpath)
        Remove_IndexPatten[0].click()

    def EnterIndexZeek(self, zeekIndex):
        EnterIndex2 = self.driver.find_elements_by_xpath(self.enter_indexPattern_xpath)
        EnterIndex2[0].send_keys(zeekIndex)
        EnterIndex2[0].send_keys(Keys.ENTER)

    def EnterIndexECS(self, ecsIndex):
        EnterIndex3 = self.driver.find_elements_by_xpath(self.enter_indexPattern_xpath)
        EnterIndex3[0].send_keys(ecsIndex)
        EnterIndex3[0].send_keys(Keys.ENTER)

    def TypeQuery(self, KQLinput):
        QueryTextbox = self.driver.find_elements_by_xpath(self.textbox_query_xpath)
        QueryTextbox[0].send_keys(KQLinput)

    def scrolldownpage2(self):
        self.driver.execute_script("window.scrollBy(0,100)", "")

    def clickQueryPreview(self):
        Query_preview = self.driver.find_elements_by_xpath(self.query_preview_xpath)
        Query_preview[0].click()

    def clickContinue(self):
        Continue = self.driver.find_elements_by_xpath(self.click_continue_xpath)
        Continue[0].click()

    def scrollUp(self):
        self.driver.execute_script("window.scrollBy(0,-150)", "")

    def enterName(self, ruleName):
        EnterName = self.driver.find_elements_by_xpath(self.enter_name_xpath)
        EnterName[0].send_keys(ruleName)

    def enterDesc(self, description):
        EnterDesc = self.driver.find_elements_by_xpath(self.enter_desc_xpath)
        EnterDesc[0].send_keys(description)

    def clickSeverity_dropdown(self):
        Severity_dropdown = self.driver.find_elements_by_xpath(self.severity_dropdown_xpath)
        Severity_dropdown[0].click()

    def select_high_severity(self):
        Select_high = self.driver.find_elements_by_xpath(self.selectSeverity_high_xpath)
        Select_high[0].click()

    def scrollDown(self):
        self.driver.execute_script("window.scrollBy(0,200)", "")

    def inputFirstTag(self, tag1):
        Tag = self.driver.find_elements_by_xpath(self.textbox_tag_xpath)
        Tag[0].send_keys(tag1)
        Tag[0].send_keys(Keys.ENTER)

    def inputSecondTag(self, tag2):
        Tag = self.driver.find_elements_by_xpath(self.textbox_tag_xpath)
        Tag[0].send_keys(tag2)
        Tag[0].send_keys(Keys.ENTER)

    #scrolldown page function scrolldownpage2
    #click continue functiion clickContinue

    def enterRunsEvery(self, valueRunEvery):
        Runs_every = self.driver.find_elements_by_xpath(self.input_runsEvery_xpath)
        if Runs_every[0].get_attribute('value') != "5":
            Runs_every[0].clear()
            Runs_every[0].send_keys(valueRunEvery)

    def selectRunsEvery(self):
        Select_Runevery_dropdown = self.driver.find_element_by_xpath(self.select_runsEvery_xpath)
        select = Select(Select_Runevery_dropdown)
        select.select_by_value("m")


    def enterAdditionalLookback(self, lookbackValue):
        Additional_Lookback_time = self.driver.find_elements_by_xpath(self.additionalLookback_xpath)
        if Additional_Lookback_time[0].get_attribute('value') != "720":
            Additional_Lookback_time[0].clear()
            Additional_Lookback_time[0].send_keys(lookbackValue)


    def selectAdditionalLookback(self):
        Select_Additional_Lookback_time = self.driver.find_element_by_xpath(self.select_additionalHour_xpath)
        select = Select(Select_Additional_Lookback_time)
        select.select_by_value("h")

        #clickContinue

    def selectActionFreq(self):
        Select_Actions_Freq = self.driver.find_element_by_xpath(self.select_actionFreq_xpath)
        select = Select(Select_Actions_Freq)
        select.select_by_value("rule")
        self.driver.execute_script("window.scrollBy(0,180)", "")

    def selectActionType(self):
        Select_Action_Type = self.driver.find_elements_by_xpath(self.select_actionType_xpath)
        Select_Action_Type[0].click()
        self.driver.execute_script("window.scrollBy(0,100)", "")

    def clickWebhook(self):
        webhook_conn = self.driver.find_elements_by_xpath(self.webhook_option_xpath)
        webhook_conn[0].click()

    def selectMattermost(self):
        mattermost = self.driver.find_elements_by_xpath(self.select_mattermost)
        mattermost[0].click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400)", "")

    def clickActivateRule(self):
        clickActionRule = self.driver.find_elements_by_xpath(self.button_activateRule)
        clickActionRule[0].click()
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class dashboardPage():
    # Locators of all the elements
    opendateXpath = "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    selectYearXpath = "//button[@data-test-subj='superDatePickerCommonlyUsed_Last_1 year']"
    selectYearXpath2 = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
    enterQueryXpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
    pressUpdateXpath = "//span[contains(text(),'Update')]"
    refreshXpath = "//span[contains(text(),'Refresh')]"
    #openSaveQueryXpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
    openSaveQueryXpath = "//button[@data-test-subj='saved-query-management-popover-button']/span[1]/span[1]/*[2]"
    saveCurrentqueryXpath = "//span[contains(text(),'Save current query')]"
    enterNameName = "title"
    toggleOnName = "shouldIncludeTimefilter"
    saveXpath = "//*/div[1]/div[3]/button[2]/span[1]/span[1]"
    saveCurrentQueryXpath = "//span[contains(text(),'Save current query')]"
    toastMsgXpath = "//span[contains(text(),'Your query \"IP_Trojan_Query\" was saved')]"
    toastMsg1Xpath = "//span[contains(text(),'Your query \"sensor_query\" was saved')]"
    shareButtonXpath = "//span[contains(text(),'Share')]"
    permalinkXpath = "//span[contains(text(),'Permalinks')]"
    radioButtonSnapshotXpath = "//label[@class='euiRadio__label']"
    copyLinkXpath = "//span[contains(text(),'Copy link')]"
    openSaveQueryXpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
    enterQueryName_Name = "title"
    toggleOn_Name = "shouldIncludeTimefilter"
    saveQueryTextXpath = "//span[contains(text(),'IP_Trojan_Query')]"
    checkLastXpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
    DateDropdownMenuXpath = "//div[@class='euiFlexItem']/div[1]/div[1]/input[1]"
    checkDateXpath = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
    deleteIconXpath = "//button[contains(@class, 'euiListGroupItem__extraAction')]"
    deleteButtonXpath = "//span[contains(text(),'Delete')]"
    session_deleteButtonXpath = "//tbody/tr[1]/td[2]/div[1]/div[1]/button[2]"
    getTimeframeClassName = "euiSuperDatePicker__prettyFormat"
    applyButtonXpath = "//span[contains(text(),'Apply')]"
    addToWorkspaceXpath = "//span[contains(text(),'Add to My Workspace')]"
    checkboxID = "show-time-filter"
    submitXpath = "//span[contains(text(),'Submit')]"
    toastMsg_addToworkspaceXpath = "//span[@class='euiToastHeader__title']"
    dropdown_lastXpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
    enterNumberXpath = "//*/fieldset[1]/div[3]/div[2]/div[1]/div[1]/input[1]"
    selectYearXpath = "//button[contains(text(),'Last 1 year')]"
    select_oneyearXpath = "//button[text()='Last 1 year']"
    addedFilterFieldXpath = "//*//div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    addFilterLinkXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    count_removeFilter1Xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[2]/*[1]"
    removeFilter1Xpath = "//*/div[1]/span[1]/span[1]/button[2]/*[1]"
    count_removeFilter2Xpath = "//*/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]"
    addArrow_dropdownXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    typeFieldXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    applyfilter_fieldXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    enterButtonClassName = "euiComboBoxOption__content"
    operatorArrowXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    selectOperatorXpath = "//*/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]"
    typeValueXpath = "//*/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    saveButtonXpath = "//span[contains(text(),'Save')]"
    savedToastMsg_IpruleQuery = "//span[contains(text(),'Your query \"dest_IP_rule_query\" was saved')]"
    getTitleXpath = "//*/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/ul[1]/li/div[2]"
    selectExistXpath = "//mark[contains(text(),'exists')]"
    savebutton_addfilterXpath = "//*/nav[1]/div[1]/button[5]/span[1]/span[1]"
    total_pgXpath = "//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button"
    del1Xpath = "//*/div[3]/div[1]/div[2]/div[1]/div[3]/ul[1]/li/button[2]"
    delete_ButtonXpath = "//*/div[2]/button[2]/span[1]/span[1]"
    dashboard_menuXpath = "//button[contains(text(),'Dashboard')]"
    analyst_notesXpath = "//span[contains(text(),'Analyst Notes')]"
    expand_dataTagXpath = "//*/table[1]/tbody[1]/tr[1]/td[2]/div[1]/button[1]"
    id_linkXpath = "//*/tr[2]/td[1]/div[1]/dl[1]/dt[1]/button[1]"
    getTItleXpath = "//span[contains(text(),'Editing Suricata [MOONDRAGON]')]"
    dataTagaTabXpath = "//span[text()='Data Tags']"
    notes_tabXpath = "//span[text()='Notes']"
    close_deepdiveXpath = "//body[1]/div[8]/div[3]/div[1]/button[1]"
    close_analystNotesXpath = "//body[1]/div[6]/div[3]/div[1]/button[1]"
    addNewTagXpath = "//strong[text()='Add a New Data Tag']"
    timeValueXpath = "//*/figure[1]/figcaption[1]/div[1]/div[3]/time[1]"
    fieldToRefArrowXpath = "//button[@class='euiSuperSelectControl']"
    getRefMenuXpath = "//div[contains(text(),'related.ip')]"
    getVisualIPXpath = "//button[contains(text(),'suricata related IP chart')]"
    search_deletedTag1Xpath = "//*/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    noitemfoundXpath = "//*/tbody[1]/tr[1]/td[1]/div[1]/span[1]"
    firstTitleXpath = "//*/figcaption[1]/h2[1]/span[2]/span[1]"
    secondTItleXpath = "//*/span[1]/figcaption[1]/h2[1]/span[2]/span[1]/span[1]"
    thirdTitleXpath = "//*/div[4]/div[1]/div[1]/span[1]/figcaption[1]/h2[1]/span[2]/span[1]"
    forthTitleXpath = "//*/div[3]/div[1]/div[1]/span[1]/figcaption[1]/h2[1]/span[2]/span[1]"
    checkoccuranceXpath = "//label[contains(text(),'C​h​e​c​k​ ​t​o​ ​A​p​p​l​y​ ​t​o​ ​A​L​L​ ​O​c​c​')]"
    enterTagXpath = "//div[@class='euiComboBox__input']/input[1]"
    enter_tagXpath = "//*//div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    lookgoodXpath = "//span[contains(text(),'Looks Good')]"
    entered_TagXpath = "//*//div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    sessionfieldXpath = "//*/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    ipruleXpath = "//mark[text()='dest_IP_rule_query']"
    select_addfilterFieldXpath = "//*/button[1]/span[1]/span[1]/span[1]/span[1]/mark[1]"
    addDash2Xpath = "//*/tr[1]/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    addDashNotes2Xpath = "//*/tr[1]/td[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]"
    addnotesXpath = "//span[contains(text(),'Add Note')]"
    sessionNotesXpath = "//*/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/textarea[1]"
    sessionNotesfieldXpath = "//span[text()='Submit']"
    addedDash1Xpath = "//*/tr[1]/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    #addedDashNotes1Xpath = "//div[contains(text(),'This is a destination IP rule query notes.')]"
    addedDashNotes1Xpath = "//*/tr[1]/td[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]"
    toastMsg_anaylstNotesXpath = "//span[ @class ='euiToastHeader__title']/div[1]/div[1]"
    session_notesXpath = "//span[contains(text(),'Session Notes')]"
    notesaddedXpath = "//div[contains(text(),'Note Added Successfully')]"
    deleteIcon_sessionNotesXpath = "//*/tr[1]/td[2]/div[1]/div[1]/button[1]"
    delete_toastMsgXpath = "//div[@data-test-subj='globalToastList']"
    delete_savedQueryButton = "//*/div[2]/button[2]/span[1]/span[1]"
    dashboard_notesXpath = "//span[contains(text(),'Dashboard Notes')]"
    dashboardCommentXpath = "//h1[contains(text(),'Add Dashboard Comment')]"
    dashCommentNotFoundXpath = "//span[contains(text(),'No items found')]"
    usernameTimeValueXpath = "//*/tr/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    ip_savedQueryXpath = "//span[contains(text(),'IP_Trojan_Query')]"
    deleteicon1Xpath = "//*/div[3]/div[1]/div[2]/div[1]/div[3]/ul[1]/li[1]/button[2]"
    deleteicon2Xpath = "//button[@data-test-subj='delete-saved-query-sensor_query-button']"
    findDashXpath = "//*/tr[1]/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
    deleteToastMsgXpath = "//span[@class='euiToastHeader__title']/div[1]/div[1]"
    get_destinIPXpath = "//*/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr/td[1]/div[2]/div[1]/div[1]"
    ruleQuery_alertMsgXpath = "//span[contains(text(),'Your query \"Rule_Query\" was saved')]"
    ruleQueryXpath = "//span[contains(text(),'Rule_Query')]"
    SensorQueryXpath = "//span[contains(text(),'sensor_query')]"
    delete_ruleQueryXpath = "//*[@title='Delete saved query Rule_Query']"
    delete_sensorQueryXpath = "//*[@title='Delete saved query sensor_query']"
    table_colXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/kbn-agg-table-group[1]/table[1]/tbody[1]/tr[1]/td[1]/kbn-agg-table[1]/paginated-table[1]/paginate[1]/div[1]/table[1]/tbody[1]/tr/td[1]/div[1]/span[1]"
    table_col2Xpath = "//*/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/kbn-agg-table-group[1]/table[1]/tbody[1]/tr[1]/td[1]/kbn-agg-table[1]/paginated-table[1]/paginate[1]/div[1]/table[1]/tbody[1]/tr/td[1]/div[1]/span[1]"
    sourcePortXpath = "//*/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr/td[2]/div[2]/div[1]/div[1]"





    def __init__(self,driver):
        self.driver = driver

    def dashboard_menu(self):
        clickDashboard_pg = self.driver.find_elements(By.XPATH, self.dashboard_menuXpath)
        clickDashboard_pg[0].click()


    def opendate(self):
        OpenDate2 = self.driver.find_elements(By.XPATH, self.opendateXpath)
        OpenDate2[0].click()

    def selectLastOneyear(self):
        select_oneyear = self.driver.find_elements(By.XPATH, self.select_oneyearXpath)
        select_oneyear[0].click()


    def clickdecoderlin(self):
        DecoderLink = self.driver.find_elements(By.LINK_TEXT, "Decoder")
        DecoderLink[0].click()
        time.sleep(2)



    def select_Year(self):
        SelectYear = self.driver.find_elements(By.XPATH, self.selectYearXpath)
        SelectYear[0].click()

    def dropdown_last(self, value_dropdown):
        dropdownLast = self.driver.find_element(By.XPATH, self.dropdown_lastXpath)
        select2 = Select(dropdownLast)
        select2.select_by_value(value_dropdown)

    def enterNumberofYear(self, num):
        enterNumber = self.driver.find_elements(By.XPATH, self.enterNumberXpath)
        if enterNumber[0].get_attribute('value') != "1":
            enterNumber[0].send_keys(Keys.CONTROL + "a")
            enterNumber[0].send_keys(Keys.DELETE)
            enterNumber[0].send_keys(num)
            time.sleep(1)


    def openSavedQuery(self):
        OpenSaveQuery1 = self.driver.find_elements(By.XPATH, self.openSaveQueryXpath)
        OpenSaveQuery1[0].click()
        time.sleep(2)



    def save_currentQuery(self):
        SaveCurrentQuery = self.driver.find_elements(By.XPATH, self.saveCurrentQueryXpath)
        SaveCurrentQuery[0].click()
        time.sleep(3)

    def enterQueryName(self, Query_name):
        EnterName = self.driver.find_element(By.NAME, self.enterQueryName_Name).send_keys(Query_name)

    def toggleON_saveQuery(self):
        ToggleOn = self.driver.find_elements(By.NAME, self.toggleOn_Name)
        ToggleOn[0].click()

    def enternumof2ndYear(self):
        enterNumber = self.driver.find_elements(By.XPATH, self.enterNumberXpath)
        if enterNumber[0].get_attribute('value') != "2":
            enterNumber[0].send_keys(Keys.CONTROL + "a")
            enterNumber[0].send_keys(Keys.DELETE)
            enterNumber[0].send_keys("2")

    def selectYear(self, value_y):
        selectYear = self.driver.find_element(By.XPATH, self.selectYearXpath2)
        select3 = Select(selectYear)
        select3.select_by_value(value_y)

    def clickApply(self):
        clickApply = self.driver.find_elements(By.XPATH, self.applyButtonXpath)
        clickApply[0].click()

    def enterKQL_query(self, Query_1):
        Enterquery = self.driver.find_elements(By.XPATH, self.enterQueryXpath)

        Enterquery[0].send_keys(Keys.CONTROL + "a")
        Enterquery[0].send_keys(Keys.DELETE)
        time.sleep(3)
        Enterquery[0].send_keys(Query_1)

    def pressUpdate(self):
        PressUpdate = self.driver.find_elements(By.XPATH, self.pressUpdateXpath)
        PressUpdate[0].click()


    def clickRefresh(self):
        if self.driver.find_elements(By.XPATH, self.refreshXpath)[0].is_displayed():
            clickRefresh = self.driver.find_element(By.XPATH, self.refreshXpath)
            clickRefresh.click()
            time.sleep(4)

    def openSaveQuery(self):
        OpenSaveQuery1 = self.driver.find_elements(By.XPATH, self.openSaveQueryXpath)
        OpenSaveQuery1[0].click()


    def saveCurrentquery(self):
        SaveCurrentQuery = self.driver.find_elements(By.XPATH, self.saveCurrentqueryXpath)
        SaveCurrentQuery[0].click()

    def enterQueryName(self, query_name):
        EnterName = self.driver.find_element(By.NAME, self.enterNameName).send_keys(query_name)
        ToggleOn = self.driver.find_elements(By.NAME, self.toggleOnName)
        ToggleOn[0].click()

    def SaveQuery(self):
        saveQ_button = self.driver.find_elements(By.XPATH, self.saveXpath)
        saveQ_button[0].click()

    def toastMsg(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.toastMsgXpath))
                   )

        toast_message = self.driver.find_elements(By.XPATH, self.toastMsgXpath)[0].text
        assert toast_message == "Your query \"IP_Trojan_Query\" was saved"

    def toastMsg2(self, toast_msg):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, self.toastMsg1Xpath))
                   )
        toast_message2 = self.driver.find_elements(By.XPATH, self.toastMsg1Xpath)[0].text
        assert toast_message2 == toast_msg

    def shareButton(self):
        clickshare = self.driver.find_elements(By.XPATH, self.shareButtonXpath)
        clickshare[0].click()

    def permalink(self):
        Permalinks = self.driver.find_elements(By.XPATH, self.permalinkXpath)
        Permalinks[0].click()

    def radioButton_snapshot(self):
        radio_button_snapshot = self.driver.find_elements(By.XPATH, self.radioButtonSnapshotXpath)
        radio_button_snapshot[0].click()

    def copyLink(self):
        copylink = self.driver.find_elements(By.XPATH, self.copyLinkXpath)
        copylink[0].click()

    def openSave_query(self):
        OpenSaveQuery1 = self.driver.find_elements(By.XPATH, self.openSaveQueryXpath)
        OpenSaveQuery1[0].click()


    def verifySavedQuery(self):
        total_pg = len(self.driver.find_elements(By.XPATH, self.total_pgXpath))

        if total_pg > 1:
            nextpg = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button[" + str(total_pg) + "]")
            nextpg[0].click()
            time.sleep(3)
            Savedquerytext = self.driver.find_elements(By.XPATH, self.saveQueryTextXpath)[0].text
            assert "IP_Trojan_Query" == Savedquerytext
            Savedquery = self.driver.find_elements(By.XPATH, self.ip_savedQueryXpath)
            Savedquery[0].click()
            time.sleep(3)
        else:
            Savedquerytext = self.driver.find_elements(By.XPATH, self.ip_savedQueryXpath)[0].text
            assert "IP_Trojan_Query" == Savedquerytext
            Savedquery = self.driver.find_elements(By.XPATH, self.ip_savedQueryXpath)
            Savedquery[0].click()
            time.sleep(3)

    def verifySavedQuery2(self):
        total_pg = len(self.driver.find_elements(By.XPATH, self.total_pgXpath))

        if total_pg > 1:
            nextpg = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button[" + str(total_pg) + "]")
            nextpg[0].click()
            time.sleep(3)
            clickRunquery = self.driver.find_elements(By.XPATH, self.SensorQueryXpath)
            clickRunquery[0].click()
        else:
            clickRunquery = self.driver.find_elements(By.XPATH, self.SensorQueryXpath)
            clickRunquery[0].click()


    def verifyQuery(self):
        Verifyquery = self.driver.find_elements(By.XPATH, self.enterQueryXpath)[0].text
        assert "destination.ip: 194.5.249.157 or rule.category: A Network Trojan was detected" == Verifyquery

    def verify_alertRuleQuery(self):
        alert_message = self.driver.find_elements(By.XPATH, self.ruleQuery_alertMsgXpath)[0].text
        assert "Your query \"Rule_Query\" was saved" == alert_message

    def checkLastDate(self):
        CheckLast = self.driver.find_elements(By.XPATH, self.checkLastXpath)
        assert CheckLast[0].get_attribute('value') == "last"


    def dateDropdown(self):
        Date_dropdownmenu1 = self.driver.find_elements(By.XPATH, self.DateDropdownMenuXpath)
        assert Date_dropdownmenu1[0].get_attribute('value') == "1"

    def checkDate(self):
        CheckDate = self.driver.find_elements(By.XPATH, self.checkDateXpath)
        assert CheckDate[0].get_attribute('value') == "y"


    def deleteIcon(self):
        clickdeleteIcon1 = self.driver.find_elements(By.XPATH, self.deleteicon1Xpath)
        if clickdeleteIcon1[0].get_attribute('title') == "Delete saved query IP_Trojan_Query":
            clickdeleteIcon1[0].click()
            time.sleep(3)
            deleteButton = self.driver.find_elements(By.XPATH, self.delete_savedQueryButton)
            deleteButton[0].click()

    def deleteIcon2(self):
        clickdeleteIcon1 = self.driver.find_elements(By.XPATH, self.deleteicon2Xpath)
        if clickdeleteIcon1[0].get_attribute('title') == "Delete saved query sensor_query":
            clickdeleteIcon1[0].click()
            time.sleep(2)
            deleteButton = self.driver.find_elements(By.XPATH, self.deleteButtonXpath)
            deleteButton[0].click()


    def getTimeFrame(self):
        GetTimeFrame = self.driver.find_element(By.CLASS_NAME, self.getTimeframeClassName).text
        return GetTimeFrame


    def addToWorkspace(self):
        clickAddToMyWorkspace = self.driver.find_elements(By.XPATH, self.addToWorkspaceXpath)
        clickAddToMyWorkspace[0].click()

    def checkbox_addToworkspaceMenu(self):
        checkbox = self.driver.find_elements(By.ID, self.checkboxID)

        if checkbox[0].is_selected():
            submit = self.driver.find_elements(By.XPATH, self.submitXpath)
            submit[0].click()
            time.sleep(2)
        else:
            checkbox[0].click()
            submit = self.driver.find_elements(By.XPATH, self.submitXpath)
            submit[0].click()
            time.sleep(2)

    def submit_workspace(self):
        submit = self.driver.find_elements(By.XPATH, self.submitXpath)
        submit[0].click()

    def toastMsg_addworkspace(self):
        ToasterAddWorkspace = self.driver.find_elements(By.XPATH, self.toastMsg_addToworkspaceXpath)[0].text
        assert "Dashboard has been added to your Workspace" == ToasterAddWorkspace


    def addFilter(self):
        clickAddFilter = self.driver.find_element(By.XPATH, self.addFilterLinkXpath)
        clickAddFilter.click()

    def remove_addedFilters(self):
        if len(self.driver.find_elements(By.XPATH, self.count_removeFilter1Xpath)) > 0:
            Remove_filter1 = self.driver.find_elements(By.XPATH, self.removeFilter1Xpath)
            Remove_filter1[0].click()
            time.sleep(2)

        if len(self.driver.find_elements(By.XPATH, self.count_removeFilter2Xpath)) > 0:
            Remove_filter2 = self.driver.find_elements(By.XPATH, self.removeFilter1Xpath)
            Remove_filter2[0].click()
            time.sleep(15)

        if len(self.driver.find_elements(By.XPATH, self.count_removeFilter2Xpath)) > 0:
            Remove_filter3 = self.driver.find_elements(By.XPATH, self.removeFilter1Xpath)
            Remove_filter3[0].click()
            time.sleep(2)

    def selectOperator_menu(self, operator_name):
        SelectOperator = self.driver.find_elements(By.XPATH, self.applyfilter_fieldXpath)
        SelectOperator[0].send_keys(operator_name)


    def selectExist(self):
        pressMenuOption = self.driver.find_elements(By.XPATH, self.selectExistXpath)
        pressMenuOption[0].click

    def click_save_addfilter(self):
        clickSave = self.driver.find_elements(By.XPATH, self.savebutton_addfilterXpath)
        clickSave[0].click()


    def addArrow_dropdown(self):
        clickArrow_dropdown = self.driver.find_elements(By.XPATH, self.addArrow_dropdownXpath)
        clickArrow_dropdown[0].click()

    def enteraddedfilter_field(self, filterField):
        enter_field = self.driver.find_elements(By.XPATH, self.addedFilterFieldXpath)
        enter_field[0].send_keys(filterField)


    def typeFilter_field(self, filter_value):
        TypeField = self.driver.find_elements(By.XPATH, self.typeFieldXpath)
        TypeField[0].send_keys(filter_value)

    def select_sourceip(self):
        select_sip = self.driver.find_elements(By.XPATH, self.select_addfilterFieldXpath)
        select_sip[0].click()

    def pressEnter(self):
        pressEnter_option = self.driver.find_elements(By.CLASS_NAME, self.enterButtonClassName)
        pressEnter_option[0].click()

    def operator_arrow(self):
        clickOperatorArrow = self.driver.find_elements(By.XPATH, self.operatorArrowXpath)
        clickOperatorArrow[0].click()

    def selectOperator(self):
        SelectOperator = self.driver.find_elements(By.XPATH, self.selectOperatorXpath)
        SelectOperator[0].click()

    def TypeValue(self, filter_value):
        TypeValue = self.driver.find_element(By.XPATH, self.typeValueXpath)
        TypeValue.send_keys(filter_value)

    def saveButton(self):
        clickSave = self.driver.find_element(By.XPATH, self.saveButtonXpath)
        clickSave.click()

    def saveToastMsg(self):
        toast_message = \
        self.driver.find_elements(By.XPATH, self.savedToastMsg_IpruleQuery)[0].text
        assert "Your query \"dest_IP_rule_query\" was saved" == toast_message

    def verifyTitle_table(self, data_query):
        getTitle = self.driver.find_elements(By.XPATH, self.getTitleXpath)

        for data in getTitle:
            assert data.text == data_query


    def get_Title(self):
        confirm_Title = self.driver.find_elements(By.XPATH, self.getTItleXpath)
        return confirm_Title

    def get_visual_relIP(self):
        confirm_visual_rel_ip = self.driver.find_elements(By.XPATH, self.getVisualIPXpath)[0].text
        return confirm_visual_rel_ip


    def get_toastMsg(self):
        confirm_toast_msg = self.driver.find_elements(By.XPATH, self.toastMsg_addToworkspaceXpath)[0].text
        return confirm_toast_msg

    def clickAnalystNotes(self):
        analystsNotes = self.driver.find_elements(By.XPATH, self.analyst_notesXpath)
        analystsNotes[0].click()

    def wait_dashboardSessionName(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located("//*/tr[1]/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]"))



    def expand_dataTag(self):
        expand_dataTags = self.driver.find_elements(By.XPATH, self.expand_dataTagXpath)
        expand_dataTags[0].click()


    def click_idlink(self):
        id_link = self.driver.find_elements(By.XPATH, self.id_linkXpath)
        id_link[0].click()


    def click_notesTab(self):
        note_tab = self.driver.find_elements(By.XPATH, self.notes_tabXpath)
        note_tab[0].click()


    def add_NewTag(self):
        addNewTag = self.driver.find_elements(By.XPATH, self.addNewTagXpath)
        addNewTag[0].click()


    def click_fieldtoRefArrow(self):
        FieldToRef_arrow = self.driver.find_elements(By.XPATH, self.fieldToRefArrowXpath)
        FieldToRef_arrow[0].click()


    def getRefMenu(self):
        ref_menu = self.driver.find_elements(By.XPATH, self.getRefMenuXpath)[0].text
        return ref_menu


    def selectMenu(self):
        select_menu = self.driver.find_elements(By.XPATH, self.getRefMenuXpath)
        select_menu[0].click()

    def check4occurance(self):
        checkbox_occurance = self.driver.find_elements(By.XPATH, self.checkoccuranceXpath)
        if checkbox_occurance[0].is_selected():
            print("Checkbox all occurance already selected")
        else:
            checkbox_occurance[0].click()

    def enterTags(self, tag_1, tag_2):
        Enter_tag = self.driver.find_elements(By.XPATH, self.enterTagXpath)
        Enter_tag[0].send_keys(tag_1)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Enter_tag[0].send_keys(tag_2)
        time.sleep(1)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)

#add this in the lab wait until
    def findDashNotes(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, self.findDashXpath))
                   )
        find_dash_notes = self.driver.find_elements(By.XPATH, self.findDashXpath)[0].text
        return find_dash_notes


    def findDashNotes1(self):
        find_dash_notes1 = self.driver.find_elements(By.XPATH, self.findDashXpath)[0].text
        return find_dash_notes1


    #submit tag

    def submit_tags(self):
        Submit = self.driver.find_elements(By.XPATH, self.submitXpath)
        Submit[0].click()

    def verify_enteredTags(self, tag_1, tag_2):
        entered_tag = len(self.driver.find_elements(By.XPATH, self.enter_tagXpath))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements(By.XPATH, "//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert tag_1 == Tag_value
            else:
                assert tag_2 == Tag_value

    def store_timevalue(self):
        time_value = self.driver.find_elements(By.XPATH, self.timeValueXpath)[0].text
        return time_value


    def click_lookgood(self):
        lookgood_button = self.driver.find_elements(By.XPATH, self.lookgoodXpath)
        lookgood_button[0].click()


    def verify_enteredTags2(self, tag_1, tag_2):
        entered_tag = len(self.driver.find_elements(By.XPATH, self.entered_TagXpath))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements(By.XPATH, "//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert True
            elif tag_2 == Tag_value:
                assert True
            else:
                assert False


    def close_deepdive(self):
        close_deepdive1 = self.driver.find_elements(By.XPATH, self.close_deepdiveXpath)
        close_deepdive1[0].click()


    def close_analystNotes(self):
        close_analystNotes = self.driver.find_elements(By.XPATH, self.close_analystNotesXpath)
        close_analystNotes[0].click()
        time.sleep(2)

    def click_dataTagsTab(self):
        data_tags_tab = self.driver.find_elements(By.XPATH, self.dataTagaTabXpath)
        data_tags_tab[0].click()


    def search_deletedTags1(self, tag_1):
        search_datatag = self.driver.find_elements(By.XPATH, self.search_deletedTag1Xpath)
        search_datatag[0].send_keys(tag_1)

    def search_deletedTags2(self, tag_2):
        search_datatag = self.driver.find_elements(By.XPATH, self.search_deletedTag1Xpath)
        search_datatag[0].clear()
        search_datatag[0].send_keys(tag_2)




    def noItemFound_analystResults(self):
        noitemfound = self.driver.find_elements(By.XPATH, self.noitemfoundXpath)[0].text
        assert noitemfound == "No items found"


    def verify_decorder_title(self):
        first_title = self.driver.find_elements(By.XPATH, self.firstTitleXpath)

        assert "Decoder Content command over time" in first_title[0].text

        second_title = self.driver.find_elements(By.XPATH, self.secondTItleXpath)

        assert "Decoder command vs connect" in second_title[0].text

        third_title = self.driver.find_element(By.XPATH, self.thirdTitleXpath).text

        assert "Decoder Command Content" in third_title

        forth_title = self.driver.find_element(By.XPATH, self.forthTitleXpath).text

        assert "Decoder CommandLine Chart" in forth_title


    def click_SessionNotesTab(self):

        SessionNotes_tab = self.driver.find_elements(By.XPATH, self.session_notesXpath)
        SessionNotes_tab[0].click()
        time.sleep(2)


    def sessionField(self, session_name):
        Session_textbox = self.driver.find_elements(By.XPATH, self.sessionfieldXpath)
        Session_textbox[0].send_keys(session_name)


    def select_query(self):
        select_query = self.driver.find_elements(By.XPATH, self.ipruleXpath)
        select_query[0].click()
        time.sleep(2)

    def add_dash2(self):
        added_dash2 = self.driver.find_elements(By.XPATH, self.addDash2Xpath)[0].text
        return added_dash2

    def add_dashNotes2(self):
        added_dashNotes2 = self.driver.find_elements(By.XPATH, self.addDashNotes2Xpath)[0].text
        return added_dashNotes2

    def delete_icon_sessionNotes(self):
        delete_icon = self.driver.find_elements(By.XPATH, self.deleteIcon_sessionNotesXpath)
        delete_icon[0].click()
        time.sleep(2)
        delete_button = self.driver.find_elements(By.XPATH, self.session_deleteButtonXpath)
        delete_button[0].click()

    def delete_toastMsg(self):
        delete_toast_msg = self.driver.find_elements(By.XPATH, self.delete_toastMsgXpath)[0].text
        return delete_toast_msg

    def toastMsg_analystNotes(self):
        toast_msg = self.driver.find_elements(By.XPATH, self.toastMsg_anaylstNotesXpath)[0].text
        return toast_msg


    def click_addnotes(self):
        add_note = self.driver.find_elements(By.XPATH, self.addnotesXpath)
        add_note[0].click()

    def verify_dashboardComment(self, verify_comment):
        Add_dashboardComment = self.driver.find_elements(By.XPATH, self.dashboardCommentXpath)[0].text
        assert Add_dashboardComment == verify_comment

    def enter_dashboardnotes(self, dash_notes):
        Comment_textbox = self.driver.find_elements(By.XPATH, self.sessionNotesXpath)
        Comment_textbox[0].send_keys(dash_notes)

    def submit_dashNotes(self):
        dash_note_submit = self.driver.find_elements(By.XPATH, self.sessionNotesfieldXpath)
        dash_note_submit[0].click()

    def verify_entered_dashnotes(self, dash_notes):
        # dashNotes = self.driver.find_elements(By.XPATH, "//*/tr/td[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]")
        # for n in dashNotes:
        #     if self.driver.find_elements(By.XPATH, "//*/tr[" + str(n) + "]/td[1]/div[1]/div[1]/div[1]/div[2]/div[1]")[0].text == capture_username_time:
        #         assert n[0].text == dash_notes
        #     else:
        #         assert False

        entered_dashNotes = self.driver.find_elements(By.XPATH, self.addedDashNotes1Xpath)[0].text
        assert entered_dashNotes == dash_notes
        print(entered_dashNotes)



    def enter_sessionnotes(self, session_notes):
        enter_session_notes = self.driver.find_elements(By.XPATH, self.sessionNotesXpath)
        enter_session_notes[0].send_keys(session_notes)

    def submit_sessionnotes(self):
        submit_session_notes = self.driver.find_elements(By.XPATH, self.sessionNotesfieldXpath)
        submit_session_notes[0].click()

    def notesAdded_toastMsg(self):
        cap_toastMsg = self.driver.find_elements(By.XPATH, self.notesaddedXpath)[0].text
        assert cap_toastMsg == "Note Added Successfully"

    def capture_usernametime(self):
        capture_username_time = self.driver.find_elements(By.XPATH, self.addedDash1Xpath)[0].text
        return capture_username_time



    def addedDash1(self):
        added_dash1 = self.driver.find_elements(By.XPATH, self.addedDash1Xpath)[0].text
        return added_dash1

    def addedDash_notes1(self):
        added_dashNotes1 = self.driver.find_elements(By.XPATH, self.addedDashNotes1Xpath)[0].text
        return added_dashNotes1

    def verify_dashFound(self, capture_username_time):
        find_dash_notes = self.driver.find_elements(By.XPATH, self.addedDash1Xpath)[0].text
        assert find_dash_notes == capture_username_time

    def clickDashboard_notes(self):
        dashboardNotes = self.driver.find_elements(By.XPATH, self.dashboard_notesXpath)
        dashboardNotes[0].click()

    def verify_dashboardnotesNotFound(self, capture_username_time):
        if len(self.driver.find_elements(By.XPATH, self.dashCommentNotFoundXpath)) >0:
            print("no item found")
        else:
            username_time = self.driver.find_elements(By.XPATH, self.usernameTimeValueXpath)
            for ut in username_time:
                assert ut.text != capture_username_time



    def teardown_pagin_del_savedQuery(self):
        total_pg = len(self.driver.find_elements(By.XPATH, self.total_pgXpath))

        if total_pg > 1:
            nextpg = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button[" + str(total_pg) + "]")
            nextpg[0].click()
            time.sleep(3)
            del1 = len(self.driver.find_elements(By.XPATH, self.del1Xpath))
            for d in range(1, del1 + 1):
                clickdeleteIcon1 = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[2]/div[1]/div[3]/ul[1]/li[" + str(d) + "]/button[2]")
                if clickdeleteIcon1[0].get_attribute('title') == "Delete saved query dest_IP_rule_query":
                    clickdeleteIcon1[0].click()
                    time.sleep(3)
                    deleteButton = self.driver.find_elements(By.XPATH, self.delete_savedQueryButton)
                    deleteButton[0].click()
                    time.sleep(2)
                    break
        else:
            del1 = len(self.driver.find_elements(By.XPATH, self.del1Xpath))
            for d in range(1, del1 + 1):
                clickdeleteIcon1 = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[2]/div[1]/div[3]/ul[1]/li[" + str(d) + "]/button[2]")
                if clickdeleteIcon1[0].get_attribute('title') == "Delete saved query dest_IP_rule_query":
                    clickdeleteIcon1[0].click()
                    time.sleep(3)
                    deleteButton = self.driver.find_elements(By.XPATH, self.delete_savedQueryButton)
                    deleteButton[0].click()
                    time.sleep(2)
                    break

    def teardown_pagin_del_ruleQuery(cls):
        OpenSaveIcon = cls.driver.find_elements_by_xpath(cls.openSaveQueryXpath)
        OpenSaveIcon[0].click()
        time.sleep(2)
        #deleteButtonXpath

        total_pg = len(cls.driver.find_elements_by_xpath(cls.total_pgXpath))

        if total_pg > 1:
            nextpg = cls.driver.find_elements_by_xpath("//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button[" + str(total_pg) + "]")
            nextpg[0].click()
            time.sleep(3)
            cls.driver.find_elements_by_xpath(cls.delete_ruleQueryXpath)[0].click()
            time.sleep(3)
            deleteButton = cls.driver.find_elements_by_xpath(cls.delete_savedQueryButton)
            deleteButton[0].click()
            time.sleep(1)

        else:
            cls.driver.find_elements_by_xpath(cls.delete_ruleQueryXpath)[0].click()
            time.sleep(3)
            deleteButton = cls.driver.find_elements_by_xpath(cls.delete_savedQueryButton)
            deleteButton[0].click()
            time.sleep(1)

    def deletetoastMsg(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, self.deleteToastMsgXpath))
                   )
        delete_toast_msg = self.driver.find_elements(By.XPATH, self.deleteToastMsgXpath)[0].text
        return delete_toast_msg



    def verify_destinIP(self, dest_ip_value):
        dest_ip = self.driver.find_elements_by_xpath(self.get_destinIPXpath)
        for desip in dest_ip:
            assert desip.text == dest_ip_value

    def verify_sourcePort(self, source_port_value):
        source_port = self.driver.find_elements_by_xpath(self.sourcePortXpath)
        for sourcePort in source_port:
            assert sourcePort.text == source_port_value


    def verify_alert_suricata(self):
        # Verify that SURICATA Alerts Categories [MOONDRAGON] exists

        assert len(self.driver.find_elements(By.XPATH, "//span[contains(text(),'SURICATA Alert Categories [MOONDRAGON]')]")) > 0

        assert len(self.driver.find_elements(By.XPATH, "//span[contains(text(),'Suricata Source IP [MOONDRAGON]')]")) > 0

        assert len(self.driver.find_elements(By.XPATH, "//span[contains(text(),'SURICATA Alerts [MOONDRAGON]')]")) > 0

        assert len(self.driver.find_elements(By.XPATH, "//span[contains(text(),'Suricata Dest IP [MOONDRAGON]')]")) > 0

        assert len(self.driver.find_elements(By.XPATH, "//span[contains(text(),'Suricata Src Port [MOONDRAGON]')]")) > 0


    def verifyOutput1(self, verifyoutput):
        table_col = self.driver.find_elements(By.XPATH, self.table_colXpath)
        for col in table_col:
            assert col.text == verifyoutput


    def verifyOutput2(self, verifyoutput2):
        table_col2 = self.driver.find_elements(By.XPATH, self.table_col2Xpath)
        for col_2 in table_col2:
            assert col_2.text == verifyoutput2


















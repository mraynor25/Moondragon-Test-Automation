import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class dashboardPage():
    # Locators of all the elements
    opendateXpath = "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    #selectYearXpath = "//button[contains(text(),'Last 1 year')]"
    #selectYearXpath = "//button[text()='Last 1 year']"
    selectYearXpath = "//*/fieldset[2]/div[1]/ul[1]/li[10]/button[1]"
    selectYearXpath2 = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
    enterQueryXpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
    pressUpdateXpath = "//span[contains(text(),'Update')]"
    openSaveQueryXpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
    saveCurrentqueryXpath = "//span[contains(text(),'Save current query')]"
    enterNameName = "title"
    toggleOnName = "shouldIncludeTimefilter"
    saveXpath = "//*/div[1]/div[3]/button[2]/span[1]/span[1]"
    toastMsgXpath = "//span[contains(text(),'Your query \"IP_Trojan_Query\" was saved')]"
    shareButtonXpath = "//span[contains(text(),'Share')]"
    permalinkXpath = "//span[contains(text(),'Permalinks')]"
    radioButtonSnapshotXpath = "//label[@class='euiRadio__label']"
    copyLinkXpath = "//span[contains(text(),'Copy link')]"
    openSaveQueryXpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
    saveQueryTextXpath = "//span[contains(text(),'IP_Trojan_Query')]"
    checkLastXpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
    DateDropdownMenuXpath = "//div[@class='euiFlexItem']/div[1]/div[1]/input[1]"
    checkDateXpath = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
    deleteIconXpath = "//button[contains(@class, 'euiListGroupItem__extraAction')]"
    deleteButtonXpath = "//span[contains(text(),'Delete')]"
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
    addFilterLinkXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    addArrow_dropdownXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    typeFieldXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    applyfilter_fieldXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    enterButtonClassName = "euiComboBoxOption__content"
    operatorArrowXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    selectOperatorXpath = "//*/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]"
    typeValueXpath = "//*/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    saveButtonXpath = "//span[contains(text(),'Save')]"
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
    dataTagaTabXpath = "//span[text()='Data Tags']"
    notes_tabXpath = "//span[text()='Notes']"
    close_deepdiveXpath = "//body[1]/div[8]/div[3]/div[1]/button[1]"
    close_analystNotesXpath = "//body[1]/div[6]/div[3]/div[1]/button[1]"
    addNewTagXpath = "//strong[text()='Add a New Data Tag']"
    fieldToRefArrowXpath = "//button[@class='euiSuperSelectControl']"
    getRefMenuXpath = "//div[contains(text(),'related.ip')]"
    search_deletedTag1Xpath = "//*/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    noitemfoundXpath = "//*/tbody[1]/tr[1]/td[1]/div[1]/span[1]"





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
        DecoderLink = self.driver.find_elements_by_link_text("Decoder")
        DecoderLink[0].click()
        time.sleep(2)



    def select_Year(self):
        SelectYear = self.driver.find_elements_by_xpath(self.selectYearXpath)
        SelectYear[0].click()

    def dropdown_last(self, value_dropdown):
        dropdownLast = self.driver.find_element(By.XPATH, self.dropdown_lastXpath)
        select2 = Select(dropdownLast)
        select2.select_by_value(value_dropdown)

    def enterNumberofYear(self, num):
        enterNumber = self.driver.find_elements_by_xpath(self.enterNumberXpath)
        if enterNumber[0].get_attribute('value') != "1":
            enterNumber[0].send_keys(Keys.CONTROL + "a")
            enterNumber[0].send_keys(Keys.DELETE)
            enterNumber[0].send_keys(num)
            time.sleep(1)

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
        Enterquery = self.driver.find_elements_by_xpath(self.enterQueryXpath)

        Enterquery[0].send_keys(Keys.CONTROL + "a")
        Enterquery[0].send_keys(Keys.DELETE)
        time.sleep(3)
        Enterquery[0].send_keys(Query_1)

    def pressUpdate(self):
        PressUpdate = self.driver.find_elements_by_xpath(self.pressUpdateXpath)
        PressUpdate[0].click()

    def openSaveQuery(self):
        OpenSaveQuery1 = self.driver.find_elements_by_xpath(self.openSaveQueryXpath)
        OpenSaveQuery1[0].click()


    def saveCurrentquery(self):
        SaveCurrentQuery = self.driver.find_elements_by_xpath(self.saveCurrentqueryXpath)
        SaveCurrentQuery[0].click()

    def enterQueryName(self, query_name):
        EnterName = self.driver.find_element_by_name(self.enterNameName).send_keys(query_name)
        ToggleOn = self.driver.find_elements_by_name(self.toggleOnName)
        ToggleOn[0].click()

    def SaveQuery(self):
        saveQ_button = self.driver.find_elements_by_xpath(self.saveXpath)
        saveQ_button[0].click()

    def toastMsg(self):
        toast_message = self.driver.find_elements_by_xpath(self.toastMsgXpath)[0].text
        assert toast_message == "Your query \"IP_Trojan_Query\" was saved"
        print(toast_message)


    def shareButton(self):
        clickshare = self.driver.find_elements_by_xpath(self.shareButtonXpath)
        clickshare[0].click()

    def permalink(self):
        Permalinks = self.driver.find_elements_by_xpath(self.permalinkXpath)
        Permalinks[0].click()

    def radioButton_snapshot(self):
        radio_button_snapshot = self.driver.find_elements_by_xpath(self.radioButtonSnapshotXpath)
        radio_button_snapshot[0].click()

    def copyLink(self):
        copylink = self.driver.find_elements_by_xpath(self.copyLinkXpath)
        copylink[0].click()

    def openSave_query(self):
        OpenSaveQuery1 = self.driver.find_elements_by_xpath(self.openSaveQueryXpath)
        OpenSaveQuery1[0].click()


    def verifySavedQuery(self):
        total_pg = len(self.driver.find_elements_by_xpath(self.total_pgXpath))

        if total_pg > 1:
            nextpg = self.driver.find_elements_by_xpath("//*/div[3]/div[1]/div[2]/div[1]/nav[1]/button[" + str(total_pg) + "]")
            nextpg[0].click()
            time.sleep(3)
            Savedquerytext = self.driver.find_elements_by_xpath("//span[contains(text(),'IP_Trojan_Query')]")[0].text
            # self.assertEqual("IP_Trojan_Query", Savedquerytext, "Query does not exist! Test failed")
            assert "IP_Trojan_Query" == Savedquerytext
            Savedquery = self.driver.find_elements_by_xpath("//span[contains(text(),'IP_Trojan_Query')]")
            Savedquery[0].click()
            time.sleep(3)
        else:
            Savedquerytext = self.driver.find_elements_by_xpath("//span[contains(text(),'IP_Trojan_Query')]")[0].text
            # self.assertEqual("IP_Trojan_Query", Savedquerytext, "Query does not exist! Test failed")
            assert "IP_Trojan_Query" == Savedquerytext
            Savedquery = self.driver.find_elements_by_xpath("//span[contains(text(),'IP_Trojan_Query')]")
            Savedquery[0].click()
            time.sleep(3)

    def verifyQuery(self):
        Verifyquery = self.driver.find_elements_by_xpath(self.enterQueryXpath)[0].text
        assert "destination.ip: 194.5.249.157 or rule.category: A Network Trojan was detected" == Verifyquery

    def checkLastDate(self):
        CheckLast = self.driver.find_elements_by_xpath(self.checkLastXpath)
        assert CheckLast[0].get_attribute('value') == "last"


    def dateDropdown(self):
        Date_dropdownmenu1 = self.driver.find_elements_by_xpath(self.DateDropdownMenuXpath)
        assert Date_dropdownmenu1[0].get_attribute('value') == "1"

    def checkDate(self):
        CheckDate = self.driver.find_elements_by_xpath(self.checkDateXpath)
        assert CheckDate[0].get_attribute('value') == "y"


    def deleteIcon(self):
        clickdeleteIcon1 = self.driver.find_elements_by_xpath("//*/div[3]/div[1]/div[2]/div[1]/div[3]/ul[1]/li[1]/button[2]")
        if clickdeleteIcon1[0].get_attribute('title') == "Delete saved query IP_Trojan_Query":
            clickdeleteIcon1[0].click()
            time.sleep(3)
            deleteButton = self.driver.find_elements_by_xpath("//*/div[2]/button[2]/span[1]/span[1]")
            deleteButton[0].click()



    def deleteButton(self):
        deleteButton = self.driver.find_elements_by_xpath(self.deleteButtonXpath)
        deleteButton[0].click()

    def getTimeFrame(self):
        GetTimeFrame = self.driver.find_element_by_class_name(self.getTimeframeClassName).text
        return GetTimeFrame


    def addToWorkspace(self):
        clickAddToMyWorkspace = self.driver.find_elements(By.XPATH, self.addToWorkspaceXpath)
        clickAddToMyWorkspace[0].click()

    def checkbox_addToworkspaceMenu(self):
        checkbox = self.driver.find_elements_by_id(self.checkboxID)

        if checkbox[0].is_selected():
            submit = self.driver.find_elements_by_xpath(self.submitXpath)
            submit[0].click()
            time.sleep(2)
        else:
            checkbox[0].click()
            submit = self.driver.find_elements_by_xpath(self.submitXpath)
            submit[0].click()
            time.sleep(2)

    def submit_workspace(self):
        submit = self.driver.find_elements(By.XPATH, self.submitXpath)
        submit[0].click()

    def toastMsg_addworkspace(self):
        ToasterAddWorkspace = self.driver.find_elements(By.XPATH, self.toastMsg_addToworkspaceXpath)[0].text
        assert "Dashboard has been added to your Workspace" == ToasterAddWorkspace


    def addFilter(self):
        clickAddFilter = self.driver.find_element_by_xpath(self.addFilterLinkXpath)
        clickAddFilter.click()

    def selectOperator_menu(self, operator_name):
        SelectOperator = self.driver.find_elements_by_xpath(self.applyfilter_fieldXpath)
        SelectOperator[0].send_keys(operator_name)


    def selectExist(self):
        pressMenuOption = self.driver.find_elements_by_xpath(self.selectExistXpath)
        pressMenuOption[0].click

    def click_save_addfilter(self):
        clickSave = self.driver.find_elements_by_xpath(self.savebutton_addfilterXpath)
        clickSave[0].click()


    def addArrow_dropdown(self):
        clickArrow_dropdown = self.driver.find_elements_by_xpath(self.addArrow_dropdownXpath)
        clickArrow_dropdown[0].click()

    def typeFilter_field(self, filter_value):
        TypeField = self.driver.find_elements_by_xpath(self.typeFieldXpath)
        TypeField[0].send_keys(filter_value)

    def pressEnter(self):
        pressEnter_option = self.driver.find_elements_by_class_name(self.enterButtonClassName)
        pressEnter_option[0].click()

    def operator_arrow(self):
        clickOperatorArrow = self.driver.find_elements_by_xpath(self.operatorArrowXpath)
        clickOperatorArrow[0].click()

    def selectOperator(self):
        SelectOperator = self.driver.find_elements_by_xpath(self.selectOperatorXpath)
        SelectOperator[0].click()

    def TypeValue(self, sensor_filename_value):
        TypeValue = self.driver.find_element_by_xpath(self.typeValueXpath)
        TypeValue.send_keys(sensor_filename_value)

    def saveButton(self):
        clickSave = self.driver.find_element_by_xpath(self.saveButtonXpath)
        clickSave.click()

    def verifyTitle_table(self, data_query):
        getTitle = self.driver.find_elements_by_xpath(self.getTitleXpath)

        for data in getTitle:
            assert data.text == data_query


    def get_Title(self):
        confirm_Title = self.driver.find_elements_by_xpath("//span[contains(text(),'Editing Suricata [MOONDRAGON]')]")
        return confirm_Title

    def get_visual_relIP(self):
        confirm_visual_rel_ip = self.driver.find_elements_by_xpath("//button[contains(text(),'suricata related IP chart')]")[0].text
        return confirm_visual_rel_ip


    def get_toastMsg(self):
        confirm_toast_msg = self.driver.find_elements_by_xpath(self.toastMsg_addToworkspaceXpath)[0].text
        return confirm_toast_msg

    def clickAnalystNotes(self):
        analystsNotes = self.driver.find_elements_by_xpath(self.analyst_notesXpath)
        analystsNotes[0].click()


    def expand_dataTag(self):
        expand_dataTags = self.driver.find_elements_by_xpath(self.expand_dataTagXpath)
        expand_dataTags[0].click()


    def click_idlink(self):
        id_link = self.driver.find_elements_by_xpath(self.id_linkXpath)
        id_link[0].click()


    def click_notesTab(self):
        note_tab = self.driver.find_elements_by_xpath(self.notes_tabXpath)
        note_tab[0].click()


    def add_NewTag(self):
        addNewTag = self.driver.find_elements_by_xpath(self.addNewTagXpath)
        addNewTag[0].click()


    def click_fieldtoRefArrow(self):
        FieldToRef_arrow = self.driver.find_elements_by_xpath(self.fieldToRefArrowXpath)
        FieldToRef_arrow[0].click()


    def getRefMenu(self):
        ref_menu = self.driver.find_elements_by_xpath(self.getRefMenuXpath)[0].text
        return ref_menu


    def selectMenu(self):
        select_menu = self.driver.find_elements_by_xpath("//div[contains(text(),'related.ip')]")
        select_menu[0].click()

    def check4occurance(self):
        checkbox_occurance = self.driver.find_elements_by_xpath("//label[contains(text(),'C​h​e​c​k​ ​t​o​ ​A​p​p​l​y​ ​t​o​ ​A​L​L​ ​O​c​c​')]")
        if checkbox_occurance[0].is_selected():
            print("Checkbox all occurance already selected")
        else:
            checkbox_occurance[0].click()

    def enterTags(self, tag_1, tag_2):
        Enter_tag = self.driver.find_elements_by_xpath("//div[@class='euiComboBox__input']/input[1]")
        Enter_tag[0].send_keys(tag_1)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Enter_tag[0].send_keys(tag_2)
        time.sleep(1)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)


    #submit tag

    def submit_tags(self):
        Submit = self.driver.find_elements_by_xpath("//span[contains(text(),'Submit')]")
        Submit[0].click()

    def verify_enteredTags(self, tag_1, tag_2):
        entered_tag = len(self.driver.find_elements_by_xpath("//*//div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert tag_1 == Tag_value
            else:
                assert tag_2 == Tag_value

    def store_timevalue(self):
        time_value = self.driver.find_elements_by_xpath("//*/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        return time_value


    def click_lookgood(self):
        lookgood_button = self.driver.find_elements_by_xpath("//span[contains(text(),'Looks Good')]")
        lookgood_button[0].click()


    def verify_enteredTags2(self, tag_1, tag_2):
        entered_tag = len(self.driver.find_elements_by_xpath("//*//div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert True
            elif tag_2 == Tag_value:
                assert True
            else:
                assert False


    def close_deepdive(self):
        close_deepdive1 = self.driver.find_elements_by_xpath(self.close_deepdiveXpath)
        close_deepdive1[0].click()


    def close_analystNotes(self):
        close_analystNotes = self.driver.find_elements_by_xpath(self.close_analystNotesXpath)
        close_analystNotes[0].click()
        time.sleep(2)

    def click_dataTagsTab(self):
        data_tags_tab = self.driver.find_elements_by_xpath(self.dataTagaTabXpath)
        data_tags_tab[0].click()


    def search_deletedTags1(self, tag_1):
        search_datatag = self.driver.find_elements_by_xpath(self.search_deletedTag1Xpath)
        search_datatag[0].send_keys(tag_1)

    def search_deletedTags2(self, tag_2):
        search_datatag = self.driver.find_elements_by_xpath(self.search_deletedTag1Xpath)
        search_datatag[0].clear()
        search_datatag[0].send_keys(tag_2)




    def noItemFound_analystResults(self):
        noitemfound = self.driver.find_elements_by_xpath(self.noitemfoundXpath)[0].text
        assert noitemfound == "No items found"





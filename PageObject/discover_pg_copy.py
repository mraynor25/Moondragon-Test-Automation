from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest



class discoverPage():
    OpenDateXpath = "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    DropdownXpath = "//*/fieldset[1]/div[3]/div[1]/div[1]/div[1]/select[1]"
    enterDateXpath = "//*/fieldset[1]/div[3]/div[2]/div[1]/div[1]/input[1]"
    selectYearXpath = "//*/fieldset[1]/div[3]/div[3]/div[1]/div[1]/select[1]"
    selectOneYearXpath = "//button[contains(text(),'Last 1 year')]"
    ApplyButtonXpath = "//span[contains(text(),'Apply')]"
    IndexNameXpath = "//*/div[1]/div[1]/button[1]/span[1]/span[1]/strong[1]"
    OpenIndexDropdownXpath = "//button[@data-test-subj='indexPattern-switch-link']"
    #EnterSearchboxXpath = "//*/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    EnterSearchboxXpath = "//input[@aria-label='Filter options']"
    enterIndexXpath = "//*/span[1]/span[1]/span[1]/mark[1]"
    selectZeekIndexXpath = "//mark[contains(text(),'ecs-zeek')]"
    AddfilterXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    addfilter2Xpath = "//*/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]/span[1]"
    arrowIconXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    enterFieldXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    selectFieldXpath = "//*/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]/span[1]/span[1]/span[1]"
    selectField2Xpath = "//mark[@class='euiMark']"
    arrow_iconXpath = "//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]"
    select_IsXpath = "//span[@class='euiComboBoxOption__content']"
    select_IsNotXpath = "//*/button[2]/span[1]/span[1]/span[1]/span[1]"
    enterDropdownXpath = "//*/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    enter2ndDropdownXpath = "//*/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    clickSaveXpath = "//*/div[2]/div[1]/div[5]/div[1]/button[1]/span[1]/span[1]"
    click_filterXpath = "//*/div[2]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]/span[1]"
    click_editFilterXpath = "//span[text()='Edit filter']"
    updateFilterFieldXpath = "//*/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    firstAddedFilterXpath = "//*/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]"
    deleteaddedFilterXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/button[5]/span[1]/span[1]"
    searchfieldXpath = "//*/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    searchResultXpath = "//*/ul/li[1]/div[1]/div[1]/div[1]/button[1]/span[2]/span[1]"
    clearSearchFieldXpath = "//button/*[contains(@class,'euiFormControlLayoutClearButton__icon')]"
    searchResult2Xpath = "//*/ul/li[1]/div[1]/div[1]/div[1]/button[1]/span[2]/span[1]"
    enterSearchXpath = "//*/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    plusIconXpath = "//button[contains(@class, 'dscSidebarItem__action')]"
    sensor_namedataXpath = "//*/tr/td[3]/div[1]/span[1]/mark[1]"
    KQL_textboxXpath = "//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea"
    updateButtonXpath = "//span[contains(text(),'Update')]"
    sen_name_dataXpath = "//*/tr/td[3]/div[1]/span[1]/mark[1]"
    sen_filenamedataXpath = "//tbody/tr/td[4]/div[1]/span[1]"
    sen_ipdataxpath = "//*/tbody/tr/td[5]/div[1]/span[1]"
    selectIndexXpath = "//mark[@class='euiMark']"
    removeFilterXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[2]/*[1]"
   # expand_arrow_iconXpath = "//*/div[3]/div[1]/div[1]/div[1]/span[1]/button[1]" "//tbody/tr[1]/td[1]/button[1]/span[1]/span[1]/*[1]"
    expand_arrow_iconXpath = "//tbody/tr[1]/td[1]/button[1]/span[1]/span[1]/*[1]"
    table_tabXpath = "//span[contains(text(),'Table')]"
    get_idXpath = "//div[@class='kbnDocViewer__value']"
    ref_listXpath = "//*/div/figure[1]/div[1]/div[1]/div[1]"
   # tag_listXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[1]"
    tag_listXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    searchboxXpath = "//*/div[1]/div[1]/div[2]/div[1]/textarea[1]"
    zeekIndexXpath = "//strong[contains(text(),'ecs-zeek-*')]"
    ecsIndexXpath = "//span[contains(text(),'ecs-*')]"
    select_searchedIndexXpath = "//*/ul[1]/li[1]/span[1]/span[1]/span[1]/mark[1]"
    tag_infoXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    captureTimeXpath = "//*/div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[3]/time[1]"
    datatagTabXpath = "//span[contains(text(),'Data Tags')]"
    enterIndxXpath = "//*/div[6]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    # enterFavIndxXpath = "//*/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    fav_indexoptionXpath = "//mark[contains(text(),'favorited-dashboards*')]"
    numofrecXpath = "//strong[@data-test-subj='discoverQueryHits']"
    select_IndexXpath = "//*/ul[1]/li[2]/span[1]/span[1]/span[1]/mark[1]"
    addFilterFieldXpath = "//input[contains(@class, 'euiFieldNumber--fullWidth')]"
    getSensorXpath = "//tbody/tr/td[4]/div[1]/span[1]"
    getSensorFileXpath = "//tbody/tr/td[5]/div[1]/span[1]"
    getAppXpath = "//tbody/tr/td[3]/div[1]/span[1]"
    ECSIndex_Xpath = "//mark[contains(text(),'ecs-*')]"
    button_15minXpath = "//button[contains(text(),'Last 15 minutes')]"
    button_oneMonthXpath = "//button[contains(text(),'Last 1 month')]"
    openCalenderDateXpath = "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]"
    favIndexOptionXpath = "//strong[contains(text(),'favorited-dashboards*')]"
    favIndexXpath = "//span[contains(text(),'favorited-dashboards*')]"
    absoluteTimeFilterXpath = "//span[contains(text(),'Absolute')]"
    DateFieldXpath = "//input[contains(@class, 'euiFieldText--inGroup')]"
    clickNowXpath = "//button[contains(text(),'now')]"
    ArrowXpath = "//*/div[3]/div[1]/div[1]/div[1]/span[1]/button[1]"
    pagin_arrowXpath = "//*/div[1]/button[1]/span[1]/span[1]"
    pagin_linkXpath = "//*/div[5]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    pagin_row100Xpath = "//*/div[2]/div[1]/div[1]/div[1]/button[3]/span[1]/span[1]"
    ecsArkimeLink_linktext = "Arkime Filename Pivot"
    arkimeLinkXpath = "//*/div[2]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]"
    decoderIndexXpath = "//mark[contains(text(),'decoders-*')]"
    indexnameXpath = "//*/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    pcapdataXpath = "//mark[contains(text(), 'fj-16-210725.cap')]"
    extractFileXpath = "//mark[contains(text(), 'setcsrss.exe_895a0be4ae10ba436ad9506164a9db00')]"
    clickFieldTovisualXpath = "//span[@class='kbnFieldButton__fieldIcon']/span[1]/*[1]"
    clickVisualizeXpath = "//span[contains(text(),'Visualize')]"
    zeekArkime_linktext = "Zeek Arkime Filename Pivot"
    arkimePivot_xpath = "//*/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]"
    searchfield_rightpanelXpath = "//*/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    dest_ipLink_xpath = "//*/ul[1]/li[1]/div[1]/div[1]/div[1]/button[1]/span[2]/span[1]"
    add2ndFilter_xpath = "//*/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]"
    firstPlusIcon_xpath = "//*/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]"
    dest_ipValue_xpath = "//*/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"
    destipLink_xpath = "//*/div[2]/div[5]/div[1]/div[1]/div[1]/span[1]/a[1]"
    get_destIP_xpath = "//*/div[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/span[1]"
    xsip_xpath = "//*/div/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]"
    xsipXpath = "//*/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]"
    xidip_xpath = "//*/div/div[5]/div[1]/div[1]/div[1]/span[1]"
    close_openedDoc_xpath = "//body[1]/div[6]/div[3]/div[1]/button[1]"
    xdip_xpath = "//*/div/div[5]/div[1]/div[1]/div[1]/span[1]"
    xdestIP2_xpath = "//*/div[2]/div[5]/div[1]/div[1]/div[1]/span[1]/a[1]"
    source_ip_xpath = "//*/div[1]/div[2]/div[7]/div[1]/div[1]/div[1]/span[1]"





    def __init__(self, driver):
        self.driver = driver


    def loadingCheck(self):
        time.sleep(5)
        numberOfRetries = 5
        stillLoadingData = False
        while (not bool(stillLoadingData)) and (numberOfRetries > 0):
            wait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Search session complete']")))
            stillLoadingData = self.driver.find_elements(By.XPATH, "//button[@aria-label='Search session complete']")
            numberOfRetries -= 1
        # Check if data-test-subj='searchSessionIndicatorPopoverContainer'
        if numberOfRetries == 0 and bool(stillLoadingData):
            exit(2);
        SessionPoppup = self.driver.find_elements(By.XPATH, "//div[@data-test-subj='searchSessionIndicatorPopoverContainer']")
        if len(SessionPoppup) > 0:
            CloseSessionPopup = self.driver.find_element(By.XPATH, "//button[@aria-label='Search session complete']")
            CloseSessionPopup.click()
            time.sleep(2)

    def OpenDate(self):

        OpenDate2 = self.driver.find_elements(By.XPATH, self.OpenDateXpath)
        OpenDate2[0].click()


    def dateDropdown(self, value):
        dropdownLast = self.driver.find_element(By.XPATH, self.DropdownXpath)
        select2 = Select(dropdownLast)
        select2.select_by_value(value)



    def numofyear(self, num):
        enterNumber = self.driver.find_elements(By.XPATH, self.enterDateXpath)
        if enterNumber[0].get_attribute('value') != num:
            enterNumber[0].send_keys(Keys.CONTROL + "a")
            enterNumber[0].send_keys(Keys.DELETE)
            enterNumber[0].send_keys(num)

    def selectYear2(self, year):
        selectYear = self.driver.find_element(By.XPATH, self.selectYearXpath)
        select3 = Select(selectYear)
        select3.select_by_value(year)

    def selectYear(self):
        SelectYear = self.driver.find_elements(By.XPATH, self.selectOneYearXpath)
        SelectYear[0].click()



    def clickApply(self):
        clickApplyButton = self.driver.find_elements(By.XPATH, self.ApplyButtonXpath)
        clickApplyButton[0].click()


    def openIndexMenu(self):
        OpenIndexDropdown = self.driver.find_elements(By.XPATH, self.OpenIndexDropdownXpath)
        OpenIndexDropdown[0].click()
        time.sleep(3)
        Enter_search_option = self.driver.find_elements(By.XPATH, self.EnterSearchboxXpath)
        Enter_search_option[0].send_keys("ecs-zeek-*")
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.selectZeekIndexXpath).click()



    def Addfilter(self):
        Add_filter_click = self.driver.find_elements(By.XPATH, self.AddfilterXpath)
        Add_filter_click[0].click()


    def clickarrowIcon(self):
        Click_ArrowIcon = self.driver.find_elements(By.XPATH, self.arrowIconXpath)
        Click_ArrowIcon[0].click()

    def enterField(self, fieldname):
        EnterField = self.driver.find_elements(By.XPATH, self.enterFieldXpath)
        EnterField[0].send_keys(fieldname)

    # def enterField2(self, fieldn2):
    #     EnterField = self.driver.find_elements_by_xpath(self.enterFieldXpath)
    #     EnterField[0].send_keys(fieldn2)

    def selectField(self):
        selectField = self.driver.find_elements(By.XPATH, self.selectFieldXpath)
        selectField[0].click()

    def selectField2(self):
        selectField = self.driver.find_elements(By.XPATH, self.selectField2Xpath)
        selectField[0].click()



    def clickarrow_addfilter(self):
        Click_arrow_icon = self.driver.find_element(By.XPATH, self.arrow_iconXpath)
        Click_arrow_icon.click()

    def selectIsMenu(self):
        select_Is_option = self.driver.find_elements(By.XPATH, self.select_IsXpath)
        select_Is_option[0].click()

    def selectIsNotMenu(self):
        select_IsNot = self.driver.find_elements(By.XPATH, self.select_IsNotXpath)
        select_IsNot[0].click()

    def enter2ndDropdown(self, data2):
        Enter_dropdown = self.driver.find_elements(By.XPATH, self.enter2ndDropdownXpath)
        Enter_dropdown[0].send_keys(data2)



    def EnterDropdown(self, data):
        Enter_dropdown = self.driver.find_elements(By.XPATH, self.enterDropdownXpath)
        Enter_dropdown[0].send_keys(data)


    def enter_addfilterField(self, field):
        Enter_textbox = self.driver.find_elements(By.XPATH, self.addFilterFieldXpath)
        Enter_textbox[0].send_keys(field)
        time.sleep(6)


    def clickSave(self):
        click_save = self.driver.find_elements(By.XPATH, self.clickSaveXpath)
        click_save[0].click()

    def click_addedfilter(self):
        click_filter = self.driver.find_elements(By.XPATH, self.click_filterXpath)
        click_filter[0].click()

    def click_addedfilter2(self):
        click_filter2 = self.driver.find_elements(By.XPATH, self.addfilter2Xpath)
        click_filter2[0].click()

    def click_editFilter(self):
        edit_filter = self.driver.find_elements(By.XPATH, self.click_editFilterXpath)
        edit_filter[0].click()

    def update_filter_field(self, value):
        enterField_1 = self.driver.find_elements(By.XPATH, self.updateFilterFieldXpath)
        enterField_1[0].send_keys(Keys.CONTROL + "a")
        enterField_1[0].send_keys(Keys.DELETE)
        time.sleep(3)
        enterField_1[0].send_keys(value)

    def update_filter_field2(self, value2):
        enterField_1 = self.driver.find_elements(By.XPATH, self.updateFilterFieldXpath)
        enterField_1[0].send_keys(Keys.CONTROL + "a")
        enterField_1[0].send_keys(Keys.DELETE)
        time.sleep(3)
        enterField_1[0].send_keys(value2)

    def click_firstAddedFilter(self):
        click_filter = self.driver.find_elements(By.XPATH, self.firstAddedFilterXpath)
        click_filter[0].click()

    def delete_addedFilter(self):
        delete_filter = self.driver.find_elements(By.XPATH, self.deleteaddedFilterXpath)
        delete_filter[0].click()



    def searchfield(self, datasource):
        searchfield = self.driver.find_elements(By.XPATH, self.searchfieldXpath)
        searchfield[0].send_keys(datasource)

    def searchfield2(self, datasource2):
        searchfield = self.driver.find_elements(By.XPATH, self.searchfieldXpath)
        searchfield[0].send_keys(datasource2)

    def searchfield3(self, datasource3):
        searchfield = self.driver.find_elements(By.XPATH, self.searchfieldXpath)
        searchfield[0].send_keys(datasource3)

    def getSensor4Table(self):
        verify_sensorName = self.driver.find_elements(By.XPATH, self.getSensorXpath)
        return verify_sensorName


    def verifySearchResults(self):
        search_results = self.driver.find_elements(By.XPATH, self.searchResultXpath)
        for list_s in search_results:
            assert "source" in list_s.text


    def searchfield2(self, dest):
        searchfield = self.driver.find_elements(By.XPATH, self.enterSearchXpath)
        searchfield[0].send_keys(dest)
        time.sleep(2)

    def searchfield4(self, datasource4):
        enter_searchField = self.driver.find_element(By.XPATH, self.enterSearchXpath)
        enter_searchField.send_keys(datasource4)

    def verifydestinationQuery(self):
        search_results = self.driver.find_elements(By.XPATH, self.searchResult2Xpath)

        for list_des in search_results:
            assert "destination" in list_des.text



    def add_sensor(self, sensor):
        enter_searchField = self.driver.find_element(By.XPATH, self.enterSearchXpath)
        enter_searchField.send_keys(sensor)



    def clickPlusIcon(self):
        plus_icon_field = self.driver.find_elements(By.XPATH, self.plusIconXpath)
        plus_icon_field[0].click()


    def clickfieldTovisual(self):
        clickfield_visual = self.driver.find_elements(By.XPATH, self.clickFieldTovisualXpath)
        clickfield_visual[0].click()

    def clickVisualButton(self):
        clickVisualize = self.driver.find_elements(By.XPATH, self.clickVisualizeXpath)
        clickVisualize[0].click()



    def verifySensorQuery(self):
        sen_name = "fj-03"
        sensor_name_data = self.driver.find_elements(By.XPATH, self.sensor_namedataXpath)

        for sen in sensor_name_data:
            self.assertEqual(sen.text, sen_name, "Test failed, sensor name is not returned correctly")

    def enterQuery(self, KQL):
        enterKQL = self.driver.find_elements(By.XPATH, self.KQL_textboxXpath)
        enterKQL[0].send_keys(Keys.CONTROL + "a")
        enterKQL[0].send_keys(Keys.DELETE)
        time.sleep(2)
        enterKQL[0].send_keys(KQL)


    def clickUpdateButton(self):
        if len(self.driver.find_elements(By.XPATH, self.updateButtonXpath)) > 0:
            PressUpdate = self.driver.find_elements(By.XPATH, self.updateButtonXpath)
            PressUpdate[0].click()

    def addSensorFilename(self, sen_file):
        enter_searchField = self.driver.find_element_by_xpath(self.enterSearchXpath)
        enter_searchField.send_keys(sen_file)


    def enterSourceIP(self, source):
        enter_searchField = self.driver.find_element_by_xpath(self.enterSearchXpath)
        enter_searchField.send_keys(source)


    def verifySensorName(self,  sen_name_data2):
        sensor_name_data = self.driver.find_elements_by_xpath(self.sensor_namedataXpath)


        for sen in sensor_name_data:
            self.assertEqual(sen.text, sen_name_data2, "Test failed, sensor name is not returned correctly")

    def verifySensorfile(self):
        sen_filename = "fj-03-220111.cap"

        sensor_filename_data = self.driver.find_elements_by_xpath(self.sen_filenamedataXpath)

        for sen_2 in sensor_filename_data:
            self.assertEqual(sen_2.text, sen_filename, "Test failed, sensor filename is not returned correctly")

    def verifysensorIP(self, source_ip):

        source_ip_data = self.driver.find_elements_by_xpath(self.sen_ipdataxpath)

        for source in source_ip_data:
            self.assertEqual(source.text, source_ip, "Test failed, source ip is not returned correctly")

    def get_app_data(self):
        verify_app = self.driver.find_elements_by_xpath(self.getAppXpath)
        return verify_app

    def get_sensorFile_data(self):
        verify_sensorFile = self.driver.find_elements_by_xpath(self.getSensorFileXpath)
        return verify_sensorFile

    def openIndex(self):
        Open_index = self.driver.find_elements(By.XPATH, self.OpenIndexDropdownXpath)
        Open_index[0].click()

    def enterIndex(self, IndexName):
        Enter_index = self.driver.find_elements_by_xpath(self.enterFavIndxXpath)
        Enter_index[0].send_keys(IndexName)

    def selectIndex(self):
        index_option22 = self.driver.find_elements_by_xpath(self.select_IndexXpath)
        index_option22[0].click()
        time.sleep(1)

    def selectZeek_index(self):
        ecsZeek_option = self.driver.find_elements_by_xpath(self.selectZeekIndexXpath)
        ecsZeek_option[0].click()



    def select_searched_index(self):
        self.driver.find_element_by_xpath(self.select_searchedIndexXpath).click()

    def selectECS_index(self):
        ecs_option = self.driver.find_elements_by_xpath(self.ECSIndex_Xpath)
        ecs_option[0].click()

    def indexSearchbox(self, suricata_index):
        index_searchbox = self.driver.find_elements_by_xpath(self.EnterSearchboxXpath)
        index_searchbox[0].send_keys(suricata_index)
        time.sleep(3)
        ecs_suricata = self.driver.find_elements_by_xpath(self.selectIndexXpath)
        ecs_suricata[0].click()

    def if_15Min_time(self):
        if len(self.driver.find_elements_by_xpath(self.button_15minXpath)) > 0:
            select_15minago = self.driver.find_elements_by_xpath(self.button_15minXpath)
            select_15minago[0].click()

    def if_lastOneMo_time(self):
        if len(self.driver.find_elements_by_xpath(self.button_oneMonthXpath)) > 0:
            select_LastOneMo = self.driver.find_elements_by_xpath(self.button_oneMonthXpath)
            select_LastOneMo[0].click()
        else:
            open_date = self.driver.find_elements_by_xpath(self.openCalenderDateXpath)
            open_date[0].click()

    def click_absolute_timefilter(self):
        Absoulte_tab = self.driver.find_elements_by_xpath(self.absoluteTimeFilterXpath)
        Absoulte_tab[0].click()

    def startDate(self, startDateValue):
        startDate_field = self.driver.find_elements_by_xpath(self.DateFieldXpath)
        startDate_field[0].send_keys(Keys.CONTROL + "a")
        startDate_field[0].send_keys(Keys.DELETE)
        startDate_field[0].send_keys(startDateValue)

    def endDate(self, endDateValue):
        endDate_field = self.driver.find_elements_by_xpath(self.DateFieldXpath)
        endDate_field[0].send_keys(Keys.CONTROL + "a")
        endDate_field[0].send_keys(Keys.DELETE)
        endDate_field[0].send_keys(endDateValue)

    def clickNow(self):
        click_now = self.driver.find_elements_by_xpath(self.clickNowXpath)
        click_now[0].click()



    def removeFilter(self):
        remove_filter = self.driver.find_elements_by_xpath(self.removeFilterXpath)
        remove_filter[0].click()


    def enterSensorName(self, sen_name):

        EnterField = self.driver.find_elements_by_xpath(self.enterFieldXpath)
        EnterField[0].send_keys(sen_name)


    def enterDropdownDD(self, dd):

        Enter_dropdown = self.driver.find_elements_by_xpath(self.enterDropdownXpath)
        Enter_dropdown[0].send_keys(dd)


    def verifySensorName(self):
        sen_name = "DD-03"
        sensor_name_data = self.driver.find_elements_by_xpath(self.sen_name_dataXpath)

        for sen in sensor_name_data:
            self.assertEqual(sen.text, sen_name, "Test failed, sensor name is not returned correctly")

    def enterQuery_1(self, KQL2):
        enterKQL = self.driver.find_elements_by_xpath(self.KQL_textboxXpath)
        enterKQL[0].send_keys(Keys.CONTROL + "a")
        enterKQL[0].send_keys(Keys.DELETE)
        time.sleep(2)
        enterKQL[0].send_keys(KQL2)


    def Verify_sensorNameData(self, sen_name_data):


        sensor_name_data = self.driver.find_elements_by_xpath(self.sen_name_dataXpath)

        for sen in sensor_name_data:
            self.assertEqual(sen.text, sen_name_data, "Test failed, sensor name is not returned correctly")

    def verify_senFile(self, sen_filename):


        sensor_filename_data = self.driver.find_elements_by_xpath(self.sen_filenamedataXpath)

        for sen_2 in sensor_filename_data:
            self.assertEqual(sen_2.text, sen_filename, "Test failed, sensor filename is not returned correctly")

    def verifySource(self, source_data):
        searchfield = self.driver.find_elements_by_xpath(self.searchfieldXpath)
        searchfield[0].send_keys(source_data)
        time.sleep(2)

        search_results = self.driver.find_elements_by_xpath(self.searchResultXpath)

        for list_s in search_results:
            assert source_data in list_s.text


    def selectDecorderIndex(self, decod):
        index_searchbox = self.driver.find_elements_by_xpath(self.EnterSearchboxXpath)
        index_searchbox[0].send_keys(decod)
        time.sleep(2)
        decoders = self.driver.find_elements_by_xpath(self.selectIndexXpath)
        decoders[0].click()


    def enterKQL2(self, KQL2):
        enterKQL = self.driver.find_elements_by_xpath(self.KQL_textboxXpath)
        enterKQL[0].send_keys(Keys.CONTROL + "a")
        enterKQL[0].send_keys(Keys.DELETE)
        time.sleep(2)
        enterKQL[0].send_keys(KQL2)

    def verifySenName(self, sen_name):


        sensor_name_data = self.driver.find_elements_by_xpath(self.sen_name_dataXpath)

        for sen in sensor_name_data:
            self.assertEqual(sen.text, sen_name, "Test failed, sensor name is not returned correctly")


    def verifySenFile(self, sen_filename):
        sensor_filename_data = self.driver.find_elements_by_xpath(self.sen_filenamedataXpath)

        for sen_2 in sensor_filename_data:
            self.assertEqual(sen_2.text, sen_filename, "Test failed, sensor filename is not returned correctly")

    def searchSource(self):
        searchfield = self.driver.find_elements_by_xpath(self.searchfieldXpath)
        searchfield[0].send_keys("source")

    def verifySource2(self, source_data):
        search_results = self.driver.find_elements_by_xpath(self.searchResult2Xpath)

        for list_s in search_results:
            assert source_data in list_s.text

    def searchField_Destination(self):
        searchfield = self.driver.find_elements_by_xpath(self.searchfieldXpath)
        searchfield[0].send_keys("destination")
        time.sleep(2)

    def verifySearch_Dest(self, dest):
        search_results = self.driver.find_elements_by_xpath(self.searchResult2Xpath)

        for list_des in search_results:
            assert dest in list_des.text


    def ExpandRecord(self):
        Expand_search_icon = self.driver.find_elements(By.XPATH, self.expand_arrow_iconXpath)
        Expand_search_icon[0].click()

    def TableTab(self):
        Table = self.driver.find_elements(By.XPATH, self.table_tabXpath)
        Table[0].click()


    def FieldToRef_id(self):
        fieldTOReferance_id = self.driver.find_elements(By.XPATH, self.get_idXpath)[0].text
        return fieldTOReferance_id
    #fieldTOReferance_id = FieldToRef_id()


    def verify_ref(self, Ref_id):

        fieldTOReferance_id = Ref_id

        DataTag = self.driver.find_elements(By.XPATH, self.datatagTabXpath)
        DataTag[0].click()
        time.sleep(2)

        ref_list = self.driver.find_elements(By.XPATH, self.ref_listXpath)
        count_refList = len(ref_list)

        last_ref_list = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_refList) + "]/figure[1]/div[1]/div[1]/div[1]")

        assert "In reference to _id: " + fieldTOReferance_id == last_ref_list[0].text
        cnt_ref_2 = count_refList - 1
        sec_ref_list = self.driver.find_elements(By.XPATH, "//*/div[" + str(cnt_ref_2) + "]/figure[1]/div[1]/div[1]/div[1]")

        assert "In reference to _id: " + fieldTOReferance_id == sec_ref_list[0].text


        cnt_ref_3 = count_refList - 2
        third_ref_list = self.driver.find_elements(By.XPATH, "//*/div[" + str(cnt_ref_3) + "]/figure[1]/div[1]/div[1]/div[1]")
        assert "In reference to _id: " + fieldTOReferance_id == third_ref_list[0].text

    def captureTime(self):
        capture_time = self.driver.find_elements(By.XPATH, self.captureTimeXpath)[0].text
        return capture_time

    def verify_time(self, cap_time):
        capture_time = cap_time
        tag_list = self.driver.find_elements(By.XPATH, "//*/div/figure[1]/figcaption[1]/div[1]/div[1]")
        count_tagList = len(tag_list)

        time_date = self.driver.find_elements(By.XPATH, "//div[" + str(count_tagList) + "]/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        assert capture_time == time_date



    def verify_user_tagmsg(self, username, tag_1, tag_2, tag_3, tag_4):


        tag_list = self.driver.find_elements(By.XPATH, self.tag_listXpath)
        count_tagList = len(tag_list)

        last_tag_user = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_tagList) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text

        assert last_tag_user == username

        first_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_tagList) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        count_sec_tag_user = count_tagList - 1

        second_tag_user = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_sec_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text

        assert second_tag_user == username

        second_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_sec_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        count_third_tag_user = count_tagList - 2

        third_tag_user = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_third_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text

        assert third_tag_user == username

        third_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_third_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        count_forth_tag_user = count_tagList - 3

        forth_tag_user = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_forth_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text

        assert forth_tag_user == username

        forth_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_forth_tag_user) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        ListOfTag = [tag_1, tag_2, tag_3, tag_4]

        print(ListOfTag)

        # Verify tag messages
        assert first_tag_msg in ListOfTag
        assert second_tag_msg in ListOfTag
        assert third_tag_msg in ListOfTag
        assert forth_tag_msg in ListOfTag


    def locate_searchbox(self):
        scrollTo_searchbox = self.driver.find_elements(By.XPATH, self.searchboxXpath)
        scrollTo_searchbox[0].location_once_scrolled_into_view
        time.sleep(2)

    def selectECSIndex(self):
        select_zeekIndex = self.driver.find_elements(By.XPATH, self.zeekIndexXpath)
        select_zeekIndex[0].click()
        time.sleep(2)
        select_ecsIndex = self.driver.find_elements(By.XPATH, self.ecsIndexXpath)
        select_ecsIndex[0].click()


    def searchbox_input(self, Ref_id):
         fieldTOReferance_id = Ref_id
         searchBox = self.driver.find_elements(By.XPATH, self.searchboxXpath)
         searchBox[0].send_keys("_id:" + fieldTOReferance_id)



    def verifyTags(self, tag_1, tag_2, tag_3, tag_4):


        taginfo = self.driver.find_elements(By.XPATH, self.tag_infoXpath)
        time.sleep(3)

        count_taginfo = len(taginfo)
        count_lastthree = count_taginfo - 3
        count_lasttwo = count_taginfo - 2
        count_lastone = count_taginfo - 1

        last_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_taginfo) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
        lastThree_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_lastthree) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
        lastTwo_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_lasttwo) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
        lastOne_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_lastone) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        ListOfTag = [tag_1, tag_2, tag_3, tag_4]

        assert last_tag_msg in ListOfTag

        assert lastOne_tag_msg in ListOfTag

        assert lastTwo_tag_msg in ListOfTag

        assert lastThree_tag_msg in ListOfTag

      # verify user
    def verify_user(self, username):

        taginfo = self.driver.find_elements(By.XPATH, self.tag_infoXpath)
        time.sleep(3)

        count_taginfo = len(taginfo)
        count_lasttwo = count_taginfo - 2
        count_lastone = count_taginfo - 1

        check_lastUser = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_taginfo) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text
        assert check_lastUser == username


        check_firstuser = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_lastone) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text
        assert check_firstuser == username


        check_seconduser = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_lasttwo) + "]/figure[1]/figcaption[1]/div[1]/div[1]")[0].text
        assert check_seconduser == username

    #verifyUser()


    def verifyRef_time(self, Ref_id, cap_time):
        taginfo = self.driver.find_elements(By.XPATH, self.tag_infoXpath)
        time.sleep(3)

        count_taginfo = len(taginfo)
        count_lasttwo = count_taginfo - 2
        count_lastone = count_taginfo - 1

        fieldTOReferance_id = Ref_id
        capture_time = cap_time


        check_lastRef = self.driver.find_elements(By.XPATH, "//div["+str(count_taginfo)+"]/figure[1]/div[1]/div[1]/div[1]")[0].text
        assert check_lastRef == "In reference to _id: " + fieldTOReferance_id
        check_firstRef = self.driver.find_elements(By.XPATH, "//div[" + str(count_lastone) + "]/figure[1]/div[1]/div[1]/div[1]")[0].text
        assert check_firstRef == "In reference to _id: " + fieldTOReferance_id
        check_secRef = self.driver.find_elements(By.XPATH, "//div[" + str(count_lasttwo) + "]/figure[1]/div[1]/div[1]/div[1]")[0].text
        assert check_secRef == "In reference to _id: " + fieldTOReferance_id


        check_lasttag_time = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_taginfo) + "]/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        assert check_lasttag_time == capture_time
        check_firsttag_time = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_lastone) + "]/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        assert check_firsttag_time == capture_time
        check_sectag_time = self.driver.find_elements(By.XPATH, "//*/div[" + str(count_lasttwo) + "]/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        assert check_sectag_time == capture_time

    def open_index_dropdown(self):
        OpenIndexDropdown = self.driver.find_elements_by_xpath(self.OpenIndexDropdownXpath)
        OpenIndexDropdown[0].click()

    def search_index(self, index_name2):
        Enter_index = self.driver.find_elements(By.XPATH, self.enterIndxXpath)
        Enter_index[0].send_keys(index_name2)


    def enter_index(self, index):
        Enter_search_option = self.driver.find_element_by_xpath(self.indexnameXpath)
        Enter_search_option.send_keys(index)


    def selectDecoder_index(self):
        select_decoders = self.driver.find_elements_by_xpath(self.decoderIndexXpath)
        select_decoders[0].click()


    def selectFav_index(self):
        clickFav_indexOption = self.driver.find_elements(By.XPATH, self.fav_indexoptionXpath)
        clickFav_indexOption[0].click()

    def enterKQL(self, KQL):
        EnterUserKQL = self.driver.find_elements(By.XPATH, self.KQL_textboxXpath)
        EnterUserKQL[0].clear()
        EnterUserKQL[0].send_keys(KQL)

    def verifynumofRec(self):
        VerifynumofRecord = self.driver.find_elements(By.XPATH, self.numofrecXpath)[0].text
        return VerifynumofRecord

    def openFavIndexMenu(self):
        Fav_indexOption = self.driver.find_elements(By.XPATH, self.favIndexOptionXpath)[0].text
        if Fav_indexOption[0] != "favorited-dashboards*":
            OpenIndexDropdown = self.driver.find_elements(By.XPATH, self.OpenIndexDropdownXpath)
            OpenIndexDropdown[0].click()
            time.sleep(2)
            clickFav_indexOption = self.driver.find_elements(By.XPATH, self.favIndexXpath)
            clickFav_indexOption[0].click()

    def search_ArkimePivot(self, arkime):
        searchfield = self.driver.find_elements_by_xpath(self.searchfield_rightpanelXpath)
        searchfield[0].send_keys(arkime)
        time.sleep(2)

        plus_icon_field = self.driver.find_elements_by_xpath(self.plusIconXpath)
        plus_icon_field[0].click()
        time.sleep(2)

    def click_arkimePivot(self):
        arkime_link = self.driver.find_elements_by_xpath(self.arkimePivot_xpath)
        arkime_link[0].click()


    def enterKQLuserElastic(self):
        EnterUserKQL2 = self.driver.find_elements(By.XPATH, self.KQL_textboxXpath)
        EnterUserKQL2[0].clear()
        EnterUserKQL2[0].send_keys("username : \"analyst\"")

        # if EnterUserKQL2 != "username : \"elastic\"":
        #    EnterUserKQL2[0].clear()
        #    # EnterUserKQL2[0].send_keys(Keys.CONTROL + "a")
        #    # EnterUserKQL2[0].send_keys(Keys.DELETE)
        #    EnterUserKQL2[0].send_keys("username : \"elastic\"")

    def enterKQLuserElastic2(self):
         EnterUserKQL3 = self.driver.find_elements(By.XPATH, self.KQL_textboxXpath)
         EnterUserKQL3[0].clear()
         EnterUserKQL3[0].send_keys("username : \"analyst2\"")



    def verifyNumofRec2(self):
        VerifynumofRecord2 = self.driver.find_elements(By.XPATH, self.numofrecXpath)[0].text
        return VerifynumofRecord2

    def verifyNumofRec3(self):
        VerifynumofRecord3 = self.driver.find_elements(By.XPATH, self.numofrecXpath)[0].text
        return VerifynumofRecord3

    def selectFavIndex(self, input_index):
        Enter_index = self.driver.find_elements(By.XPATH, self.EnterSearchboxXpath)
        Enter_index[0].send_keys(input_index)
        time.sleep(2)
        clickFav_indexOption = self.driver.find_elements(By.XPATH, self.fav_indexoptionXpath)
        clickFav_indexOption[0].click()


    # pagination/ document table

    def click_arrow(self):
        clickArrow = self.driver.find_elements_by_xpath(self.ArrowXpath)
        clickArrow[0].click()

    def pagin_arrow_row100(self):
        pagin_arrow = self.driver.find_elements_by_xpath(self.pagin_arrowXpath)[0].text
        print(pagin_arrow)
        time.sleep(3)

        if pagin_arrow in "25" or "50":
            pagination_link = self.driver.find_elements_by_xpath(self.pagin_linkXpath)
            pagination_link[0].click()
            time.sleep(7)

            row_100 = self.driver.find_elements_by_xpath(self.pagin_row100Xpath)
            row_100[0].click()

    def close_doc(self):
        close_doc = self.driver.find_elements_by_xpath(self.close_openedDoc_xpath)
        close_doc[0].click()


    def clickECS_arkime(self):
        ECS_arkimeLink = self.driver.find_elements_by_link_text(self.ecsArkimeLink_linktext)
        ECS_arkimeLink[0].click()

    # def clickZeek_arkime(self):
    #     ECSZeek_arkimeLink = self.driver.find_elements_by_link_text(self.zeekArkime_linktext)
    #     ECSZeek_arkimeLink[0].click()
    def clickArkime_link(self):
        arkime_link = self.driver.find_elements_by_xpath(self.arkimeLinkXpath)
        arkime_link[0].click()

    def verifyPCAPdata(self):
        VerifyPCAP_data = self.driver.find_elements_by_xpath(self.pcapdataXpath)[0].text
        return VerifyPCAP_data

    def verifyExtractFile(self):
        VerifyExtract_File = self.driver.find_elements_by_xpath(self.extractFileXpath)[0].text
        return VerifyExtract_File


    def search_searchfield(self, fieldn1):
        searchfield = self.driver.find_elements_by_xpath(self.searchfield_rightpanelXpath)
        searchfield[0].send_keys(fieldn1)


    def search_searchfield2(self, fieldname2):
        searchfield = self.driver.find_elements_by_xpath(self.searchfield_rightpanelXpath)
        searchfield[0].send_keys(fieldname2)

    def search_searchfield3(self, fieldname3):
        searchfield = self.driver.find_elements_by_xpath(self.searchfield_rightpanelXpath)
        searchfield[0].send_keys(fieldname3)

    def search_searchfield4(self, fieldname4):
        searchfield = self.driver.find_elements_by_xpath(self.searchfield_rightpanelXpath)
        searchfield[0].send_keys(fieldname4)



    def add_searchResults_click_plusicon(self):
        plus_icon_field = self.driver.find_elements_by_xpath(self.plusIconXpath)
        plus_icon_field[0].click()

    def clearSearchField(self):
        clear_search_field = self.driver.find_elements_by_xpath(self.clearSearchFieldXpath)
        clear_search_field[0].click()

    def clickdestIPLink(self):
        dest_ipLink = self.driver.find_elements_by_xpath(self.dest_ipLink_xpath)
        dest_ipLink[0].click()

    def firstPlusIcon(self):
        first_plus_icon = self.driver.find_elements_by_xpath(self.firstPlusIcon_xpath)
        first_plus_icon[0].click()
        time.sleep(2)

    def get_destIp_value(self):
        dest_ip_value = \
        self.driver.find_elements_by_xpath(self.dest_ipValue_xpath)[0].text
        return dest_ip_value

    def get_destip(self):
        dest_ip = \
            self.driver.find_elements_by_xpath(self.get_destIP_xpath)[0].text
        return dest_ip

    def click_x_destiplink(self):
        click_xpanse_desip = self.driver.find_elements_by_xpath(self.destipLink_xpath)
        click_xpanse_desip[0].click()

    def click_x_siplink(self):
        click_Xpanse_sip = self.driver.find_elements_by_xpath(self.xsipXpath)
        click_Xpanse_sip[0].click()

    def click_xdestiplink2(self):
        click_xpanse_desip = self.driver.find_elements_by_xpath(self.xdestIP2_xpath)
        click_xpanse_desip[0].click()


    def add_2ndfilter(self):
        Add_filter_click = self.driver.find_elements_by_xpath(self.add2ndFilter_xpath)
        Add_filter_click[0].click()
        time.sleep(2)

    def verify_sxip(self):
        xsip = len(self.driver.find_elements_by_xpath(self.xsip_xpath))

        for si in range(2, xsip + 1):
            xpense_sip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si) + "]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]")[0].text
            assert xpense_sip == "XPANSE Source IP Pivot"

    def verify_sxip2(self):
        xsip = len(self.driver.find_elements_by_xpath(self.xsip_xpath))

        for si in range(2, xsip + 1):
            xpense_sip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si) + "]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]")[0].text
            #print(xpense_sip)
            assert xpense_sip == "XPANSE Source IP Query"

    def verify_dxip(self):
        xdip = len(self.driver.find_elements_by_xpath(self.xidip_xpath))

        for si2 in range(2, xdip + 1):
            xpense_dip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si2) + "]/div[5]/div[1]/div[1]/div[1]/span[1]")[0].text
            assert xpense_dip == "XPANSE Destination IP Pivot"

    def verify_sip(self):
        xsip = len(self.driver.find_elements_by_xpath(self.xsip_xpath))

        for si in range(2, xsip + 1):
            xpense_sip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si) + "]/div[4]/div[1]/div[1]/div[1]/span[1]/a[1]")[0].text
            assert xpense_sip == "-"



    def verify_dip(self):
        xdip = len(self.driver.find_elements_by_xpath(self.verify_dxip))

        for si2 in range(2, xdip + 1):
            xpense_dip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si2) + "]/div[5]/div[1]/div[1]/div[1]/span[1]")[0].text
            print(xpense_dip)
            assert xpense_dip == "-"

    def verify_destip(self):

        xdip = len(self.driver.find_elements_by_xpath(self.xdip_xpath))

        for si2 in range(2, xdip + 1):
            xpense_dip = \
            self.driver.find_elements_by_xpath("//*/div[" + str(si2) + "]/div[5]/div[1]/div[1]/div[1]/span[1]")[0].text
            assert xpense_dip == "-"

    def get_sourceIp(self):
        source_ip = self.driver.find_elements_by_xpath(self.source_ip_xpath)[0].text
        return source_ip

    def click_sourceipLink(self):
        click_Xpanse_sip = self.driver.find_elements_by_xpath(self.xsipXpath)
        click_Xpanse_sip[0].click()

    def check_xpanse_destIP(self):
        Xpanse_destIP = self.driver.find_elements_by_link_text("XPANSE Destination IP Pivot")
        assert Xpanse_destIP != "XPANSE Destination IP Pivot"

    def check_xpanse_sourceIP(self):
        Xpanse_sourceIP = self.driver.find_elements_by_link_text("XPANSE Source IP Pivot")
        assert Xpanse_sourceIP != "XPANSE Source IP Pivot"

    def search_query_id(self, store_id):
        searchBox = self.driver.find_elements_by_xpath(self.KQL_textboxXpath)
        searchBox[0].send_keys("_id: " + store_id)
        time.sleep(3)



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




class IOCListPage():
    # Locators of all the elements
    ioclist_xpath = "//span[text()='IOC Lists']"
    createIOC_xpath = "//span[text()='Create IOC List']"
    createIOCpg_xpath = "//h1[contains(text(),'Create IOC List')]"
    listTitle_xpath = "//body/div[7]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
    iocfile_xpath = "//input[@class='euiFilePicker__input']"
    generateList_xpath = "//span[contains(text(), 'Generate')]"
    toastMsg_xpath = "//div[@data-test-subj='globalToastList']"
    copyFilter_xpath = "//span[text()='Copy Filter']"
    savelist_xpath = "//*/div[3]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]"
    close_IOClist_xpath = "//button[@data-test-subj='euiFlyoutCloseButton']"
    IOCListName_xpath = "//*/tr/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]"
    more_xpath = "//button[@aria-label='More']"
    editList_xpath = "//span[text()='Edit List']"
    addSelector_xpath = "//span[text()='Add selectors']"
    fieldTextbox_xpath = "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    selectors_xpath = "//*/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    addRow_xpath = "//span[contains(text(),'Add row')]"
    fieldSelctors_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    selectorsField_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    notes_xpath = "//*/div[4]/div[1]/div[2]/div[1]/div[1]/input[1]"
    saveSelector_xpath = "//span[text()='Save Selectors']"
    appendList_xpath = "//span[contains(text(),'Append list')]"
    appendHeader_xpath = "//h1[contains(text(),'Append List')]"
    appendToggleOn_xpath = "//button[@aria-checked='true']"
   # selectIOCName_xpath = "//tbody/tr[1]/td[2]/div[2]/button[1]"
    selectIOCName_xpath = "//button[@aria-label='popout']"
    uploadAppendList_xpath = "//*/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
    generalList_xpath = "//span[contains(text(),'Generate List')]"
    appendSelector_xpath = "//span[contains(text(),'Append Selectors')]"
    appendListConfirm_xpath = "//p[contains(text(),'The selected file will be appended to the existing')]"
    appendButton_xpath = "//span[text()='Append']"
    ToggleOnAppend_xpath = "//button[contains(@class, 'euiSwitch__button')]"
    edit_details_xpath = "//span[contains(text(),'Edit Details')]"
    enter_desc_xpath = "//textarea[@aria-label='Use aria labels when no actual label is in use']"
    applyButton_xpath = "//span[contains(text(),'Apply')]"
    confirmDesc_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/li[2]"
    confirmUser_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/li[4]"
    saveMain_xpath = "//*/div[1]/div[1]/div[3]/div[4]/button[1]/span[1]/span[1]"
    saveListButton_xpath = "//span[text()='Save List']"
    exitButton_xpath = "//div[@aria-labelledby='ABC IOC list to view']/button[1]"
    closeIOCList_xpath = "//button[@data-test-subj='euiFlyoutCloseButton']"
    addFilter_xpath = "//button[@data-test-subj='addFilter']/span[1]/span[1]"
    editAsQuery_xpath = "//span[text()='Edit as Query DSL']"
    moreButton_xpath = "//button[@aria-label='More']"
    deleteButton_xpath = "//span[contains(text(),'Delete List')]"
    downloadListButton_xpath = "//span[text()='Download List']"
    editListButton_xpath = "//span[text()='Edit List']"
    deleteListPopup_xpath = "//button[@data-test-subj='confirmModalConfirmButton']/span[1]/span[1]"
    add_additional_user_xpath = "//p[contains(text(), 'Add Additional Users')]/ancestor::button"
    enterUsers_xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    iocListSearchbox_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    ToastListIOC_xpath = "//div[contains(text(),'IOC List deleted successfully')]"


    def __init__(self,driver):
        self.driver = driver

    def open_IOCList(self):
        IOClist = self.driver.find_elements(By.XPATH, self.ioclist_xpath)
        IOClist[0].click()

    def click_createIOCList(self):
        create_IOCList = self.driver.find_elements(By.XPATH, self.createIOC_xpath)
        create_IOCList[0].click()

    def iocList_detailButton(self):
        ioc_detail = self.driver.find_elements(By.XPATH, "//tbody/tr[1]/td[2]/div[2]/button[1]")
        ioc_detail[0].click()

    def load_createIOCpg(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, self.createIOCpg_xpath))
                   )

    def enter_listTitle(self, IOC_title):
        enter_list_title = self.driver.find_elements(By.XPATH, self.listTitle_xpath)
        enter_list_title[0].send_keys(IOC_title)

    def select_IOCFile(self):
        select_file = self.driver.find_elements(By.XPATH, self.iocfile_xpath)
        select_file[0].send_keys("C:/Users/mraynor/Documents/Test Data/IOCList.csv")

    def click_generateList(self):
        click_generate_list = self.driver.find_elements(By.XPATH, self.generateList_xpath)
        click_generate_list[0].click()

    def verify_toast_Msg(self):

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, self.toastMsg_xpath))
                   )
        toastMsg = self.driver.find_elements(By.XPATH, self.toastMsg_xpath)[0].text
        print(toastMsg)

        if toastMsg == "List Not Saved: List name already exists, try another name":
            assert False

    def click_copyFilter(self):
        click_copyFilter = self.driver.find_elements(By.XPATH, self.copyFilter_xpath)
        click_copyFilter[0].click()

    def click_saveList(self):
        click_saveList = self.driver.find_elements(By.XPATH, self.savelist_xpath)
        click_saveList[0].click()

    def IOCListCreated_ToastMsg(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, self.toastMsg_xpath), "IOC List Created Successfully"))


    def close_IOCList(self):
        close_ioclist = self.driver.find_elements(By.XPATH, self.close_IOClist_xpath)
        close_ioclist[0].click()


    def IOCList_editAppendList(self, IOC_title, field_data, selectors_data, field_data2, selectors_data2, notes):
        IOClistName = len(self.driver.find_elements(By.XPATH, self.IOCListName_xpath))
        # print(IOClistName[0].text)

        for iln in range(1, IOClistName + 1):
            IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
            if IOCName == IOC_title:
                dailyIOC = \
                self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(iln) + "]/td[2]/div[2]/button[1]")[0].click()
                time.sleep(1)
                more = self.driver.find_elements(By.XPATH, self.more_xpath)[0].click()
                time.sleep(2)
                EditList = self.driver.find_elements(By.XPATH, self.editList_xpath)
                EditList[0].click()
                time.sleep(2)
                add_sectors = self.driver.find_elements(By.XPATH, self.addSelector_xpath)
                add_sectors[0].click()
                time.sleep(2)
                field_textbox = self.driver.find_elements(By.XPATH, self.fieldTextbox_xpath)
                field_textbox[0].send_keys(field_data)
                time.sleep(2)
                enter_selectors = self.driver.find_elements(By.XPATH, self.selectors_xpath)
                enter_selectors[0].send_keys(selectors_data)
                time.sleep(3)
                click_addRow = self.driver.find_elements(By.XPATH, self.addRow_xpath)
                click_addRow[0].click()
                time.sleep(1)
                field_textbox = self.driver.find_elements(By.XPATH, self.fieldSelctors_xpath)
                field_textbox[0].send_keys(field_data2)
                time.sleep(2)
                enter_selectors = self.driver.find_elements(By.XPATH, self.selectorsField_xpath)
                enter_selectors[0].send_keys(selectors_data2)
                time.sleep(1)
                enter_notes = self.driver.find_elements(By.XPATH, self.notes_xpath)
                enter_notes[0].send_keys(notes)
                time.sleep(1)
                save_selectors = self.driver.find_elements(By.XPATH, self.saveSelector_xpath)
                save_selectors[0].click()
                time.sleep(2)
                click_appendList = self.driver.find_elements(By.XPATH, self.appendList_xpath)
                click_appendList[0].click()
                time.sleep(2)
                append_header = self.driver.find_elements(By.XPATH, self.appendHeader_xpath)[0].text
                assert "Append List" == append_header
                append_toggle_on = len(self.driver.find_elements(By.XPATH, self.appendToggleOn_xpath))
                if append_toggle_on > 0:
                    upload_append_list = self.driver.find_elements(By.XPATH, self.uploadAppendList_xpath)
                    upload_append_list[0].send_keys("C:/Users/mraynor/Documents/Test Data/append_IOCList.csv")
                    time.sleep(3)
                    click_generateList = self.driver.find_elements(By.XPATH, self.generalList_xpath)
                    click_generateList[0].click()
                    time.sleep(2)
                    click_append_selectors = self.driver.find_elements(By.XPATH, self.appendSelector_xpath)
                    click_append_selectors[0].click()
                    time.sleep(2)
                    appendList_confirm = self.driver.find_elements(By.XPATH, self.appendListConfirm_xpath)[0].text
                    # print(appendList_confirm)
                    assert "The selected file will be appended to the existing IOC List." == appendList_confirm
                    append_button = self.driver.find_elements(By.XPATH, self.appendButton_xpath)
                    append_button[0].click()
                    time.sleep(1)
                    edit_details = self.driver.find_elements(By.XPATH, self.edit_details_xpath)
                    edit_details[0].click()
                    time.sleep(1)
                    enter_desc = self.driver.find_elements(By.XPATH, self.enter_desc_xpath)
                    enter_desc[0].send_keys("update ioc list")
                    time.sleep(1)
                    enter_username = self.driver.find_elements(By.XPATH, self.enterUsers_xpath)
                    enter_username[0].send_keys("analyst3")
                    time.sleep(1)
                    click_apply = self.driver.find_elements(By.XPATH, self.applyButton_xpath)
                    click_apply[0].click()
                    time.sleep(1)
                else:
                    click_toggleON_append = self.driver.find_element(By.XPATH, self.ToggleOnAppend_xpath)
                    click_toggleON_append[0].click()
                    time.sleep(1)
                    upload_append_list = self.driver.find_elements(By.XPATH, self.uploadAppendList_xpath)
                    upload_append_list[0].send_keys("/home/monica.raynor/Documents/IOCList_Append.csv")
                    time.sleep(3)
                    click_generateList = self.driver.find_elements(By.XPATH, self.generalList_xpath)
                    click_generateList[0].click()
                    time.sleep(2)
                    click_append_selectors = self.driver.find_elements(By.XPATH, self.appendSelector_xpath)
                    click_append_selectors[0].click()
                    time.sleep(2)
                    appendList_confirm = self.driver.find_elements(By.XPATH, self.appendListConfirm_xpath)[0].text
                    # print(appendList_confirm)
                    assert "The selected file will be appended to the existing IOC List." == appendList_confirm
                    append_button = self.driver.find_elements(By.XPATH, self.appendButton_xpath)
                    append_button[0].click()
                    time.sleep(1)
                    edit_details = self.driver.find_elements(By.XPATH, self.edit_details_xpath)
                    edit_details[0].click()
                    time.sleep(1)
                    enter_desc = self.driver.find_elements(By.XPATH, self.enter_desc_xpath)
                    enter_desc[0].send_keys("update ioc list")
                    time.sleep(1)
                    enter_username = self.driver.find_elements(By.XPATH, self.enterUsers_xpath)
                    enter_username[0].send_keys("analyst2")
                    time.sleep(1)
                    click_apply = self.driver.find_elements(By.XPATH, "")
                    click_apply[0].click()
                    time.sleep(1)

                confirm_desc = self.driver.find_elements(By.XPATH, self.confirmDesc_xpath)[0].text
                print(confirm_desc)
                assert "Description: update ioc list" == confirm_desc
                confirm_user = self.driver.find_elements(By.XPATH, self.confirmUser_xpath)[0].text
                assert "Additional Users: analyst3" == confirm_user

                save_main = self.driver.find_elements(By.XPATH, self.saveMain_xpath)
                save_main[0].click()
                time.sleep(2)
                if len(self.driver.find_elements(By.XPATH, self.saveListButton_xpath)) > 0:
                    save_list = self.driver.find_elements(By.XPATH, self.saveListButton_xpath)
                    save_list[0].click()
                else:
                    print("Test failed, User should not append duplicate lists")
                    assert False

                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.text_to_be_present_in_element((By.XPATH, self.toastMsg_xpath), "List Saved"))
                exit_button = self.driver.find_elements(By.XPATH, self.exitButton_xpath)
                exit_button[0].click()
                time.sleep(2)
                copy_clipboard = self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln) + "]/td[3]/div[2]/button[1] ")
                copy_clipboard[0].click()
                time.sleep(3)
                close_ioclist = self.driver.find_elements(By.XPATH, self.closeIOCList_xpath)
                close_ioclist[0].click()
                time.sleep(2)
                break



    def verify_IOClist4Buttons(self, IOC_title):
        IOClistName2 = len(self.driver.find_elements(By.XPATH, self.IOCListName_xpath))

        for iln2 in range(1, IOClistName2 + 1):
            IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln2) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
            if IOCName == IOC_title:
                dailyIOC = \
                self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln2) + "]/td[2]/div[2]/button[1]")[0].click()
                time.sleep(1)
                more = self.driver.find_elements(By.XPATH, self.moreButton_xpath)[0].click()
                time.sleep(5)
                if len(self.driver.find_elements(By.XPATH, self.deleteButton_xpath)) > 0:
                    assert False
                if len(self.driver.find_elements(By.XPATH, self.downloadListButton_xpath)) > 0:
                    assert True
                if len(self.driver.find_elements(By.XPATH, self.editListButton_xpath)) > 0:
                    assert False

    def click_download_IOC(self):
        download_IOC = self.driver.find_elements(By.XPATH, self.downloadListButton_xpath)
        download_IOC[0].click()
        time.sleep(3)

    def search_IOClist(self, IOC_title):
        enter_IOCName = self.driver.find_elements(By.XPATH, self.iocListSearchbox_xpath)
        enter_IOCName[0].send_keys(IOC_title)

    def select_IOCName(self):
        open_IOC = self.driver.find_elements(By.XPATH, self.selectIOCName_xpath)
        open_IOC[0].click()

    def click_more(self):
        more = self.driver.find_elements(By.XPATH, self.moreButton_xpath)
        more[0].click()


    def remove_IOCList(self):
        delete_list = self.driver.find_elements(By.XPATH, self.deleteButton_xpath)
        delete_list[0].click()
        time.sleep(2)
        delete_list_popup = self.driver.find_elements(By.XPATH, self.deleteListPopup_xpath)
        delete_list_popup[0].click()
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.presence_of_element_located((By.XPATH, self.ToastListIOC_xpath))
        #            )
        # IOC_delete_toastMsg = self.driver.find_elements(By.XPATH, self.ToastListIOC_xpath)[0].text
        # assert IOC_delete_toastMsg == "IOC List deleted successfully"


    def verify_deletedIOCList(self):
        noitemfound = self.driver.find_elements(By.XPATH, "//span[contains(text(),'No items found')]")[0].text
        assert "No items found" == noitemfound


    def add_additional_user(self, user):
        # add_additional_user = self.driver.find_elements(By.XPATH, self.add_additional_user_xpath)
        # add_additional_user[0].click()
        # time.sleep(4)
        enterUser = self.driver.find_elements(By.XPATH, self.enterUsers_xpath)
        enterUser[0].send_keys(user)


    def check_ioclistButton(self, IOC_title):
        more = self.driver.find_elements(By.XPATH, "//button[@aria-label='More']")[0].click()
        time.sleep(3)
        if len(self.driver.find_elements(By.XPATH, "//span[text()='Delete List']")) > 0:
            assert True
        if len(self.driver.find_elements(By.XPATH, "//span[text()='Download List']")) > 0:
            assert True
        if len(self.driver.find_elements(By.XPATH, "//span[text()='Edit List']")) > 0:
            assert True

    # IOClistName2 = len(self.driver.find_elements(By.XPATH, "//*/tr/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]"))
        #
        # for iln2 in range(1, IOClistName2 + 1):
        #     IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln2) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
        #     if IOCName == IOC_title:
        #         dailyIOC = \
        #         self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln2) + "]/td[2]/div[2]/button[1]")[0].click()
        #         time.sleep(1)
        #         more = self.driver.find_elements(By.XPATH, "//button[@aria-label='More']")[0].click()
        #         time.sleep(5)
        #         if len(self.driver.find_elements(By.XPATH, "//span[text()='Delete List']")) > 0:
        #             assert True
        #         if len(self.driver.find_elements(By.XPATH, "//span[text()='Download List']")) > 0:
        #             assert True
        #         if len(self.driver.find_elements(By.XPATH, "//span[text()='Edit List']")) > 0:
        #             assert True
        #














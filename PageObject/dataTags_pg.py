from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DatatagPage():
    DataTagXpath = "//span[contains(text(),'Data Tags')]"
    addNewtagXpath = "//strong[contains(text(),'Add a New Data Tag')]"
    selectDropdownMenuXpath = "//*/div[1]/div[2]/div[3]/div[1]/div[1]/button/span[1]/span[1]/div[1]"
    enterTagFieldXpath = "//div[@class='euiComboBox__input']/input[1]"
    submitTagXpath = "//span[contains(text(),'Submit')]"
    enterTagXpath = "//*//div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    captureTimeXpath = "//*/div[2]/div[1]/div[1]/div[1]/div/figure[1]/figcaption[1]/div[1]/div[3]/time[1]"
    LookgoodXpath = "//span[contains(text(),'Looks Good')]"
    tag_listXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[1]"
    getTagInfoXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    fieldToRefXpath = "//button[@class='euiSuperSelectControl']"
    refMenuXpath = "//div[contains(text(),'related.ip')]"
    ref_id_className = "kbnDocViewer__value"
    tag_infoXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    tagslist_xpath = "//*/div[2]/div[1]/div[3]/div[1]/figure[1]/div[1]/div[1]/p[1]"
    searchBox_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]"
    searchButton_xpath = "//span[contains(text(),'Search')]"
    bulkTagName_xpath = "//tbody/tr[1]/td[1]/div[1]"
    settingIcon_xpath = "//button[@aria-label='Actions']"
    edit_xpath = "//span[contains(text(),'Edit')]"
    view_xpath = "//span[contains(text(),'View')]"
    delete_xpath = "//span[contains(text(),'Delete')]"
    toggleOnDelete_xpath = "//button[@aria-checked='true']"
    deleteTag_xpath = "//span[contains(text(),'Delete Tag')]"
    togglebutton_xpath = "//*/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[1]"
    noitem_xpath = "//div[contains(text(),'No Items')]"
    clear_field_xpath = "//button[@aria-label='Clear input']"
    close_modal_xpath = "//button[@aria-label='Closes this modal window']"
    createTab_xpath = "//button[contains(text(),'Create')]"
    createHeader_xpath = "//h1[contains(text(),'Create Tag')]"
    toggleOn_xpath = "//button[@aria-checked='true']"
    click_togglebutton_xpath = "//button[@class='euiSwitch__button']"
    tagnameTextbox_xpath = "//input[@placeholder='Tag name']"
    tagDetailTextbox_xpath = "//textarea[@placeholder='Tag details']"
    tagname_xpath = "//*/div[1]/div[1]/div[1]/div[1]/h1[1]"
    ownersInfo_xpath = "//*/div[1]/div[2]/div[1]/dl[1]/dt[1]"
    userInfo_xpath = "//dd[contains(text(),'analyst2')]"
    detailTextbox_xpath = "//textarea[@placeholder='Tag details']"
    addAdditionalUser_xpath = "//p[text()='Add Additional Users']"
    username_tag_xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    usernameInput_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    confirmHeader_xpath = "//h1[contains(text(),'Please Confirm Your Tag')]"
    confirmTagname_xpath = "//dd[contains(text(),'sample ecs tag')]"
    confirmTagname2_xpath = "//dd[contains(text(),'test tag for ecs')]"
    confirmDetailMsg_xpath = "//dd[contains(text(),'This is your imbedded tag message. Please add, modify, delete tag as you wish')]"
    imbedded_searchbar_xpath = "//input[@placeholder='Search...']"
    addExistingTab_xpath = "//button[contains(text(),'Add existing')]"
    addexistingTagHeader_xpath = "//h1[contains(text(), 'Add Existing Tag')]"
    additionalUser_xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    tagname_option_xpath = "//mark[contains(text(),'sample ecs tag')]"
    tagname_option_xpath2 = "//mark[contains(text(),'test tag for ecs')]"
    createDataTag_xpath = "//span[contains(text(),'Create Data Tag')]"
    modal_header_xpath = "//h1[contains(text(),'Please Confirm Your Tag Selection')]"
    tag1_modal_xpath = "//li[contains(text(),'sample ecs tag')]"
    tag1_modal2_xpath = "//li[contains(text(),'test tag for ecs')]"
    completeDeleteToggleOn_xpath = "//button[aria-checked='false']"
    completeDeleteToggle_classname = "euiSwitch__button"
    tag_name_xpath = "//div[contains(text(),'Data Management tag')]"
    tag_name_xpath2 = "//div[contains(text(),'sample tag for data mgnt')]"
    detailMsg_xpath = "//div[contains(text(),'This is your data tag message. Please add, modify,')]"
    owner_xpath = "//tbody/tr[1]/td[3]/div[1]"
    user_xpath = "//div[contains(text(),'analyst2')]"
    confirm_tagname_xpath = "//dd[contains(text(),'Data Management tag')]"
    confirm_tagname_xpath2 = "//dd[contains(text(),'sample tag for data mgnt')]"
    confirm_detailMsg_xpath = "//dd[contains(text(),'This is your data tag message. Please add, modify,')]"
    confirm_user_xpath = "//dd[contains(text(),'analyst2')]"
    mytag_xpath = "//tbody/tr/td[1]/div[1]"



    def __init__(self, driver):
        self.driver = driver


    def DataTagTab(self):
        DataTag = self.driver.find_elements(By.XPATH, self.DataTagXpath)
        DataTag[0].click()

    def addNewTag(self):
        Add_newtag2 = self.driver.find_elements(By.XPATH, self.addNewtagXpath)
        Add_newtag2[0].click()

    def selectDropdownMenu(self):
        select_menu = self.driver.find_elements(By.XPATH, self.selectDropdownMenuXpath)
        select_menu[0].click()


    def EnterTags(self, tag_1, tag_2, tag_3, tag_4):
        Enter_tag = self.driver.find_elements(By.XPATH, self.enterTagFieldXpath)
        Enter_tag[0].send_keys(tag_1)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Enter_tag[0].send_keys(tag_2)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(2)
        Enter_tag[0].send_keys(tag_3)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(3)
        Enter_tag[0].send_keys(tag_4)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(3)


    def enter2Tags(self, tag_1, tag_2):
        Enter_tag = self.driver.find_elements(By.XPATH, self.enterTagFieldXpath)
        Enter_tag[0].send_keys(tag_1)
        time.sleep(2)
        Enter_tag[0].send_keys(Keys.ENTER)
        time.sleep(1)
        Enter_tag[0].send_keys(tag_2)
        time.sleep(1)
        Enter_tag[0].send_keys(Keys.ENTER)


    def EnterTags(self, tags):
        Enter_tag = self.driver.find_elements(By.XPATH, self.enterTagFieldXpath)
        for tag in tags:
            Enter_tag[0].send_keys(tag)
            time.sleep(2)
            Enter_tag[0].send_keys(Keys.ENTER)
            time.sleep(2)


    def verify_enteredTag(self, tag_1, tag_2, tag_3, tag_4):
        entered_tag = len(self.driver.find_elements(By.XPATH, self.enterTagXpath))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements(By.XPATH, "//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert True
            elif tag_2 == Tag_value:
                assert True
            elif tag_3 == Tag_value:
                assert True
            elif tag_4 == Tag_value:
                assert True
            else:
                assert False


    def verify_entered2Tags(self, tag_1, tag_2):
        entered_tag = len(self.driver.find_elements(By.XPATH, self.enterTagXpath))

        for tag in range(1, entered_tag + 1):
            Tag_value = self.driver.find_elements(By.XPATH, "//*/div[2]/div[1]/div[1]/div[1]/div[" + str(tag) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
            if tag_1 == Tag_value:
                assert True
            elif tag_2 == Tag_value:
                assert True
            else:
                assert False

    def submit_tag(self):
        Submit = self.driver.find_elements(By.XPATH, self.submitTagXpath)
        Submit[0].click()

    def capture_time(self):
        capture_time_val = self.driver.find_elements(By.XPATH, self.captureTimeXpath)[0].text
        return capture_time_val

    def LookGood_button(self):
        lookgood_button = self.driver.find_elements(By.XPATH, self.LookgoodXpath)
        lookgood_button[0].click()

    def verify_capTime(self):
        capture_time_val = self.capture_time()
        tag_list = self.driver.find_elements(By.XPATH, self.tag_listXpath)
        count_tagList = len(tag_list)

        time_date = self.driver.find_elements(By.XPATH, "//div[" + str(count_tagList) + "]/figure[1]/figcaption[1]/div[1]/div[3]/time[1]")[0].text
        self.assertEqual(capture_time_val, time_date, "Time/date is not matching from confirmation modal")


    def get_ref_id(self):
        grab_id = self.driver.find_elements(By.CLASS_NAME, self.ref_id_className)[0].text
        return grab_id

    def getTagInfo(self):
        taginfo = self.driver.find_elements(By.XPATH, self.getTagInfoXpath)
        time.sleep(3)

        count_taginfo = len(taginfo)
        count_lasttwo = count_taginfo - 2
        count_lastone = count_taginfo - 1

        last_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_taginfo) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
        lastTwo_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_lasttwo) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
        lastOne_tag_msg = self.driver.find_elements(By.XPATH, "//div[" + str(count_lastone) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text

        return count_taginfo, count_lastone, count_lasttwo


    def fieldToRef_arrow(self):
        FieldToRef_arrow = self.driver.find_elements(By.XPATH, self.fieldToRefXpath)
        FieldToRef_arrow[0].click()



    def enter_tagName(self, tag_name):
        enter_tagname = self.driver.find_elements(By.XPATH, self.tagnameTextbox_xpath)
        enter_tagname[0].send_keys(tag_name)

    def enter_tagName2(self, tag_name2):
        enter_tagname = self.driver.find_elements(By.XPATH, self.tagnameTextbox_xpath)
        enter_tagname[0].send_keys(tag_name2)

    def refMenu(self):
        ref_menu = self.driver.find_elements(By.XPATH, self.refMenuXpath)[0].text
        return ref_menu

    def ref_menu_option(self):
        select_menu = self.driver.find_elements(By.XPATH, self.refMenuXpath)
        select_menu[0].click()


    def verifyTag_notfound(self, tag_1, tag_2):
        taginfo = self.driver.find_elements(By.XPATH, self.tag_infoXpath)
        time.sleep(1)

        count_taginfo = len(taginfo)
        ListOfTag = [tag_1, tag_2]

        if len(self.driver.find_elements(By.XPATH, self.tag_listXpath)) > 0:
            assert True
        else:
            for tag_name in range(1, count_taginfo + 1):
                tag_list = self.driver.find_elements(By.XPATH, "//div[" + str(tag_name) + "]/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]")[0].text
                assert ListOfTag != tag_list
                break


    def searchTags_dataMgnt(self, bulkTag_name):
        enter_searchbox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        enter_searchbox[0].send_keys(bulkTag_name)

    def searchTags_dataMgnt2(self, bulkTag_name2):
        enter_searchbox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        enter_searchbox[0].send_keys(bulkTag_name2)

    def searchTag_dataMgnt(self, tag_name):
        enter_searchbox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        enter_searchbox[0].send_keys(tag_name)

    def searchTag2_dataMgnt(self, Tag_name2):
        enter_searchbox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        enter_searchbox[0].send_keys(Tag_name2)

    def waitSearchbutton_display(self):
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.XPATH, self.searchButton_xpath))
                   )

    def click_SearchButton(self):
        click_search = self.driver.find_elements(By.XPATH, self.searchButton_xpath)
        click_search[0].click()

    def create_dataTag(self):
        click_dataTag = self.driver.find_elements(By.XPATH, self.createDataTag_xpath)
        click_dataTag[0].click()


    def verify_tagname(self, bulkTag_name):
        tagname = self.driver.find_elements(By.XPATH, self.bulkTagName_xpath)[0].text
        assert tagname == bulkTag_name

    def verify_tagname2(self, bulkTag_name2):
        tagname2 = self.driver.find_elements(By.XPATH, self.bulkTagName_xpath)[0].text
        assert tagname2 == bulkTag_name2

    def settingIcon_visable(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.settingIcon_xpath))
                   )

    def waituntil_createDataTag(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.createDataTag_xpath))
                   )


    def click_settingIcon(self):
        setting_icon = self.driver.find_elements(By.XPATH, self.settingIcon_xpath)
        setting_icon[0].click()

    def verifyButtons4owner(self):
        if len(self.driver.find_elements(By.XPATH, self.edit_xpath)) > 0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.view_xpath)) > 0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.delete_xpath)) > 0:
            assert True

    def verifyButtons4AdditionalUser(self):
        if len(self.driver.find_elements(By.XPATH, self.edit_xpath)) > 0:
            assert False
        if len(self.driver.find_elements(By.XPATH, self.view_xpath)) > 0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.delete_xpath)) > 0:
            assert False

    def click_viewButton(self):
        viewButton = self.driver.find_elements(By.XPATH, self.view_xpath)
        viewButton[0].click()


    def click_deleteButton(self):
        deleteButton = self.driver.find_elements(By.XPATH, self.delete_xpath)
        deleteButton[0].click()

    def verify_viewTag(self):
        tag_name = self.driver.find_elements(By.XPATH, self.tagname_xpath)[0].text
        assert "Viewing: sensor tag" == tag_name
        ownner_info = self.driver.find_elements(By.XPATH, self.ownersInfo_xpath)[0].text
        assert "Owner: analyst" == ownner_info
        user_info = self.driver.find_elements(By.XPATH, self.userInfo_xpath)[0].text
        assert "analyst2" == user_info



    def togglecheck_completeDelete(self):
        if len(self.driver.find_elements(By.XPATH, self.toggleOnDelete_xpath)) > 0:
            deleteTag = self.driver.find_elements(By.XPATH, self.deleteTag_xpath)
            deleteTag[0].click()
        else:
            toggle_on = self.driver.find_elements(By.XPATH, self.togglebutton_xpath)
            toggle_on[0].click()
            time.sleep(1)
            deleteTag = self.driver.find_elements(By.XPATH, self.deleteTag_xpath)
            deleteTag[0].click()

    def verify_tag_exists(self, bulkTag_name):
        mytag = len(self.driver.find_elements(By.XPATH, self.mytag_xpath))
        for tg in range(1, mytag+1):
            mytag_text = self.driver.find_elements(By.XPATH, "//tbody/tr[" + str(tg) + "]/td[1]/div[1]")[0].text
            assert bulkTag_name != mytag_text


    def verify_2ndtag_exists(self, bulkTag_name2):
        mytag = len(self.driver.find_elements(By.XPATH, self.mytag_xpath))
        for tg in range(1, mytag + 1):
            mytag_text = self.driver.find_elements(By.XPATH, "//tbody/tr[" + str(tg) + "]/td[1]/div[1]")[0].text
            assert bulkTag_name2 != mytag_text

    def click_deleteTag(self):
        deleteTag = self.driver.find_elements(By.XPATH, self.deleteTag_xpath)
        deleteTag[0].click()

    def verify_noItems(self):
        noItem = self.driver.find_elements(By.XPATH, self.noitem_xpath)[0].text
        print(noItem)
        assert noItem == "No Items"


    def clear_searchbox(self):
        clear_field = self.driver.find_elements(By.XPATH, self.clear_field_xpath)
        clear_field[0].click()

    def close_modal(self):
        close = self.driver.find_elements(By.XPATH, self.close_modal_xpath)
        close[0].click()

    def enter_tag_detail(self, detail_msg):
        enter_detail = self.driver.find_elements(By.XPATH, self.tagDetailTextbox_xpath)
        enter_detail[0].send_keys(detail_msg)

    def enter_tag_username(self, add_username):
        enter_tagUser = self.driver.find_elements(By.XPATH, self.username_tag_xpath)
        enter_tagUser[0].send_keys(add_username)


    def click_addUser(self):
        addUser = self.driver.find_elements(By.XPATH, self.addAdditionalUser_xpath)
        addUser[0].click()


    def verify_confirmMsg2(self):
        confirm_msg = self.driver.find_elements(By.XPATH, self.confirmHeader_xpath)[0].text
        assert confirm_msg == "Please Confirm Your Tag"

        if len(self.driver.find_elements(By.XPATH, self.confirmTagname2_xpath)) >0:
            assert True


    def click_addExistingTab(self):
        addExisting = self.driver.find_elements(By.XPATH, self.addExistingTab_xpath)
        addExisting[0].click()

    def waituntilAddExistingTag_popup(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, self.addexistingTagHeader_xpath))
                   )

    def enterTagName(self, tag_name, tag_name2):
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(tag_name)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath)
        select_tagname[0].click()
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(tag_name2)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath2)
        select_tagname[0].click()

    def verify_searchedTagName(self, tag_name):
        check_tagname = self.driver.find_elements(By.XPATH, self.tag_name_xpath)[0].text
        assert check_tagname == tag_name

    def verify_searchedTagName2(self, tag_name):
        check_tagname = self.driver.find_elements(By.XPATH, self.tag_name_xpath2)[0].text
        assert check_tagname == tag_name

    def verify_detailMsg(self, detail_msg):
        check_deailMsg = self.driver.find_elements(By.XPATH, self.detailMsg_xpath)[0].text
        assert check_deailMsg == detail_msg

    def verify_owner(self, username):
        check_owner = self.driver.find_elements(By.XPATH, self.owner_xpath)[0].text
        assert username == check_owner

    def verify_user(self, add_username):
        check_user = self.driver.find_elements(By.XPATH, self.user_xpath)[0].text
        assert check_user == add_username


    def confirm_tagname_modal(self, tag_name):
        check_tagname = self.driver.find_elements(By.XPATH, self.confirm_tagname_xpath)[0].text
        assert check_tagname == tag_name

    def confirm_tagname_modal2(self, tag_name):
        check_tagname = self.driver.find_elements(By.XPATH, self.confirm_tagname_xpath2)[0].text
        assert check_tagname == tag_name

    def confirm_detailMsg_modal(self, detail_msg):
        check_detailMsg = self.driver.find_elements(By.XPATH, self.confirm_detailMsg_xpath)[0].text
        assert check_detailMsg == detail_msg

    def confirm_user_modal(self, add_username):
        check_user = self.driver.find_elements(By.XPATH, self.confirm_user_xpath)[0].text
        assert check_user == add_username


























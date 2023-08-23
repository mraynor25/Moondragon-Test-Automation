import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class ImbeddedTagPage():
    # Locators of all the elements
    createTab_xpath = "//button[contains(text(),'Create')]"
    createHeader_xpath = "//h1[contains(text(),'Create Tag')]"
    toggleOn_xpath = "//button[@aria-checked='true']"
    click_togglebutton_xpath = "//button[@class='euiSwitch__button']"
    tagnameTextbox_xpath = "//input[@placeholder='Tag name']"
    tagname_xpath = "//*/div[1]/div[1]/div[1]/div[1]/h1[1]"
    ownersInfo_xpath = "//*/div[1]/div[2]/div[1]/dl[1]/dt[1]"
    userInfo_xpath = "//dd[contains(text(),'analyst2')]"
    detailTextbox_xpath = "//textarea[@placeholder='Tag details']"
    addAdditionalUser_xpath = "//p[text()='Add Additional Users']"
    usernameInput_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    confirmHeader_xpath = "//h1[contains(text(),'Please Confirm Your Tag')]"
    confirmTagname_xpath = "//dd[contains(text(),'sample ecs tag')]"
    confirmTagname2_xpath = "//dd[contains(text(),'Tag for ecs')]"
    confirmDetailMsg_xpath = "//dd[contains(text(),'This is your imbedded tag message. Please add, modify, delete tag as you wish')]"
    imbedded_searchbar_xpath = "//input[@placeholder='Search...']"
    addExistingTab_xpath = "//button[contains(text(),'Add existing')]"
    addexistingTagHeader_xpath = "//h1[contains(text(), 'Add Existing Tag')]"
    additionalUser_xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    tagname_option_xpath = "//mark[contains(text(),'sample ecs tag')]"
    tagname_option_xpath2 = "//mark[contains(text(),'Tag for ecs')]"
    modal_header_xpath = "//h1[contains(text(),'Please Confirm Your Tag Selection')]"
    tag1_modal_xpath = "//li[contains(text(),'sample ecs tag')]"
    tag1_modal2_xpath = "//li[contains(text(),'Tag for ecs')]"
    imbeddedTag_xpath = "//*/tr[1]/th[1]/div[2]/span[1]"
    imbeddedUser_xpath = "//*/tr[1]/td[1]/div[2]/span[1]"
    imbeddedOwner_xpath = "//*/tr[1]/td[4]/div[2]/span[1]"
    imbeddedDesc_xpath = "//*/tr[1]/td[6]/div[2]/span[1]"
    submitTagXpath = "//span[contains(text(),'Submit')]"
    LookgoodXpath = "//span[contains(text(),'Looks Good')]"
    noitemfound_xpath = "//span[contains(text(),'No items found')]"
    clearInput_xpath = "//button[@aria-label='Clear input']"




    def __init__(self,driver):
        self.driver = driver

    def create_imbeddedTag(self):
        click_tag = self.driver.find_elements(By.XPATH, self.createTab_xpath)
        click_tag[0].click()

    def verify_tagnameindoc(self, tag_name):
        imbeddedTagName = self.driver.find_elements(By.XPATH, self.imbeddedTag_xpath)[0].text
        assert tag_name == imbeddedTagName

    def verify_tagname2indoc(self, tag_name2):
        imbeddedTagName = self.driver.find_elements(By.XPATH, self.imbeddedTag_xpath)[0].text
        assert tag_name2 == imbeddedTagName

    def verify_userindoc(self, add_username):
        imbeddedUser = self.driver.find_elements(By.XPATH, self.imbeddedUser_xpath)[0].text
        assert add_username == imbeddedUser

    def verify_ownerindoc(self, username):
        imbeddedOwner = self.driver.find_elements(By.XPATH, self.imbeddedOwner_xpath)[0].text
        assert username == imbeddedOwner

    def verify_descindoc(self, detail_msg):
        imbeddedDesc = self.driver.find_elements(By.XPATH, self.imbeddedDesc_xpath)[0].text
        assert detail_msg == imbeddedDesc


    def verify_createHeaderExist(self):
        header_name = self.driver.find_elements(By.XPATH, self.createHeader_xpath)[0].text
        assert "Create Tag" == header_name

    def checkToggleON(self):
        if len(self.driver.find_elements(By.XPATH, self.toggleOn_xpath)) > 0:
            assert True
        else:
            click_toggle_on = self.driver.find_elements(By.XPATH, self.click_togglebutton_xpath)
            click_toggle_on[0].click()

    def checkToggleOFF(self):
        if len(self.driver.find_elements(By.XPATH, self.toggleOn_xpath)) > 0:
            click_toggle_off = self.driver.find_elements(By.XPATH, self.click_togglebutton_xpath)
            click_toggle_off[0].click()


    def enter_tagName(self, tag_name):
        enter_tagname = self.driver.find_elements(By.XPATH, self.tagnameTextbox_xpath)
        enter_tagname[0].send_keys(tag_name)

    def enter_tagName2(self, tag_name2):
        enter_tagname = self.driver.find_elements(By.XPATH, self.tagnameTextbox_xpath)
        enter_tagname[0].send_keys(tag_name2)

    def enter_details(self, detail_msg):
        detail_textbox = self.driver.find_elements(By.XPATH, self.detailTextbox_xpath)
        detail_textbox[0].send_keys(detail_msg)

    def click_addUser(self):
        addUser = self.driver.find_elements(By.XPATH, self.addAdditionalUser_xpath)
        addUser[0].click()

    def enter_additional_username(self, add_username):
        userInputbox = self.driver.find_elements(By.XPATH, self.usernameInput_xpath)
        userInputbox[0].send_keys(add_username)

    def submit_tag(self):
        Submit = self.driver.find_elements(By.XPATH, self.submitTagXpath)
        Submit[0].click()

    def verify_confirmMsg(self):
        if len(self.driver.find_elements(By.XPATH, self.confirmHeader_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.confirmTagname_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.confirmDetailMsg_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.userInfo_xpath)) >0:
            assert True

    def verify_confirmMsg2(self):
        if len(self.driver.find_elements(By.XPATH, self.confirmHeader_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.confirmTagname2_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.confirmDetailMsg_xpath)) >0:
            assert True
        if len(self.driver.find_elements(By.XPATH, self.userInfo_xpath)) >0:
            assert True


    def LookGood_button(self):
        lookgood_button = self.driver.find_elements(By.XPATH, self.LookgoodXpath)
        lookgood_button[0].click()

    def enter_searchbar(self, tag_name):
        imbedded_searchbar = self.driver.find_elements(By.XPATH, self.imbedded_searchbar_xpath)
        imbedded_searchbar[0].send_keys(tag_name)

    def enter_searchbar2(self, tag_name2):
        imbedded_searchbar = self.driver.find_elements(By.XPATH, self.imbedded_searchbar_xpath)
        imbedded_searchbar[0].send_keys(tag_name2)

    def verify_NoSearchResult(self):
        if len(self.driver.find_elements(By.XPATH, self.noitemfound_xpath)) >0:
            assert True

    def clear_searchInput(self):

        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.XPATH, self.clearInput_xpath))
                   )

        search_input = self.driver.find_elements(By.XPATH, self.clearInput_xpath)
        search_input[0].click()

    def click_addExistingTab(self):
        addExisting = self.driver.find_elements(By.XPATH, self.addExistingTab_xpath)
        addExisting[0].click()

    def waituntilAddExistingTag_popup(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, self.addexistingTagHeader_xpath))
                   )

    def enterTagName(self, tag_name2):
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(tag_name2)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath2)
        select_tagname[0].click()

    def click_existing_header(self):
        add_existing_header = self.driver.find_elements(By.XPATH, self.addexistingTagHeader_xpath)
        add_existing_header[0].click()























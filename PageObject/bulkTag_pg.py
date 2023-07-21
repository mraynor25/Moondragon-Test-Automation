import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class bulkQueryPage():
    # Locators of all the elements
    addBulk_xpath = "//span[contains(text(),'Bulk Add Tag')]"
    bulkAddTagHeader_xpath = "//h1[contains(text(),'Bulk Add Tag')]"
    createTag_xpath = "//button[contains(text(),'Create Tag')]"
    tagname_xpath = "//*/div[2]/div[1]/div[2]/div[1]/input[1]"
    tagdesc_xpath = "//*/div[6]/div[3]/div[1]/div[1]/div[2]/div[1]/textarea[1]"
    additionalUser_xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    submit_xpath = "//span[contains(text(),'Submit')]"
    confirmTagname_xpath = "//*/div[2]/div[1]/div[1]/dl[1]/dd[1]"
    confirmTagdesc_xpath = "//*/div[2]/div[1]/div[1]/dl[1]/dd[2]"
    confirmAdduser_xpath = "//*/div[2]/div[1]/div[1]/dl[1]/dd[3]"
    looksgoodButton_xpath = "//span[contains(text(),'Looks Good')]"
    bulkAddTag_xpath = "//button[contains(text(),'Bulk Add Tag')]"
    addexistingTagHeader_xpath = "//h1[contains(text(), 'Add Existing Tag')]"
    tagname_option_xpath = "//mark[contains(text(),'sample bulk query')]"
    tagname_option_xpath2 = "//mark[contains(text(),'sample bulk')]"
    addTagButton_xpath = "//span[contains(text(),'Add Tag/s')]"
    closeButton_xpath = "//span[contains(text(),'Close')]"



    def __init__(self,driver):
        self.driver = driver

    def click_addBulkMenu(self):
        click_addbulk = self.driver.find_elements(By.XPATH, self.addBulk_xpath)
        click_addbulk[0].click()


    def wait4bulkTagPagetoLoad(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.bulkAddTagHeader_xpath))
                   )


    def click_createTag(self):
        click_createTag = self.driver.find_elements(By.XPATH, self.createTag_xpath)
        click_createTag[0].click()


    def enter_tagname(self, bulkTag_name):
        enterTagName = self.driver.find_elements(By.XPATH, self.tagname_xpath)
        enterTagName[0].send_keys(bulkTag_name)

    def enter_tagDescription(self, bulkTag_desc):
        enterTagDesc = self.driver.find_elements(By.XPATH, self.tagdesc_xpath)
        enterTagDesc[0].send_keys(bulkTag_desc)

    def enter_additionalUser(self, user):
        enter_additionalUser = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        enter_additionalUser[0].send_keys(user)


    def click_submit(self):
        submit = self.driver.find_elements(By.XPATH, self.submit_xpath)
        submit[0].click()

    def verify_confirmTag(self, bulkTag_name, bulkTag_desc, user):
        tagname = self.driver.find_elements(By.XPATH, self.confirmTagname_xpath)[0].text
        assert bulkTag_name == tagname

        tagdesc = self.driver.find_elements(By.XPATH, self.confirmTagdesc_xpath)[0].text
        assert bulkTag_desc == tagdesc

        add_user = self.driver.find_elements(By.XPATH, self.confirmAdduser_xpath)[0].text
        assert user == add_user

    def verify_confirmTag2(self, bulkTag_name2):
        tagname = self.driver.find_elements(By.XPATH, self.confirmTagname_xpath)[0].text
        assert bulkTag_name2 == tagname

    def click_looksgood(self):
        looksgood = self.driver.find_elements(By.XPATH, self.looksgoodButton_xpath)
        looksgood[0].click()

    def click_bulkAddTag(self):
        bulkAddTag = self.driver.find_elements(By.XPATH, self.bulkAddTag_xpath)
        bulkAddTag[0].click()

    def waituntilAddExistingTag_popup(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, self.addexistingTagHeader_xpath))
                   )

    def enterTagName(self, bulkTag_name, bulkTag_name2):
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(bulkTag_name)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath)
        select_tagname[0].click()
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(bulkTag_name2)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath2)
        select_tagname[0].click()

    def click_addExistingPopup(self):
        addExisting = self.driver.find_elements(By.XPATH, self.addexistingTagHeader_xpath)
        addExisting[0].click()

    def enterTagName2(self, bulkTag_name2):
        tag_name_dropdown = self.driver.find_elements(By.XPATH, self.additionalUser_xpath)
        tag_name_dropdown[0].send_keys(bulkTag_name2)
        time.sleep(1)
        select_tagname = self.driver.find_elements(By.XPATH, self.tagname_option_xpath2)
        select_tagname[0].click()

    def click_addTagButton(self):
        addTagButton = self.driver.find_elements(By.XPATH, self.addTagButton_xpath)
        addTagButton[0].click()

    def verifyAddedTag(self, bulkTag_name, bulkTag_name2):
        addedTag = self.driver.find_elements(By.XPATH, "//*/div[2]/p[1]/dl[2]/dd[1]/li[1]")[0].text
        assert addedTag == bulkTag_name
        added2ndTag = self.driver.find_elements(By.XPATH, "//*/div[2]/p[1]/dl[2]/dd[1]/li[2]")[0].text
        assert added2ndTag == bulkTag_name2

    def click_close(self):
        closeButton = self.driver.find_elements(By.XPATH, self.closeButton_xpath)
        closeButton[0].click()

    def verifyAddedTag2(self, bulkTag_name2):
        addedTag = self.driver.find_elements(By.XPATH, "//*/div[2]/p[1]/dl[2]/dd[1]/li[1]")[0].text
        assert addedTag == bulkTag_name2

    def verify_addedBulkTag(self):
        showTags = self.driver.find_elements(By.XPATH, "//tbody/tr/td[3]/div[1]")
        for t in showTags:
            added_tags = self.driver.find_elements(By.XPATH, "//tbody/tr["+str(t)+"]/td[3]/div[1]")[0].text
            print(added_tags)


























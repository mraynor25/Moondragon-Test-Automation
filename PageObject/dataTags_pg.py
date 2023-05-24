from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
    checkToapplyAllXpath = "//label[contains(text(),'C​h​e​c​k​ ​t​o​ ​A​p​p​l​y​ ​t​o​ ​A​L​L​ ​O​c​c​')]"
    ref_id_className = "kbnDocViewer__value"
    tag_infoXpath = "//*/div/figure[1]/figcaption[1]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/span[1]"
    tagslist_xpath = "//*/div[2]/div[1]/div[3]/div[1]/figure[1]/div[1]/div[1]/p[1]"




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

    def refMenu(self):
        ref_menu = self.driver.find_elements(By.XPATH, self.refMenuXpath)[0].text
        return ref_menu

    def ref_menu_option(self):
        select_menu = self.driver.find_elements(By.XPATH, self.refMenuXpath)
        select_menu[0].click()


    def checkbox_occr(self):
        checkbox_occurance = self.driver.find_elements(By.XPATH, self.checkToapplyAllXpath)
        if checkbox_occurance[0].is_selected():
            print("Checkbox all occurance already selected")
        else:
            checkbox_occurance[0].click()


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






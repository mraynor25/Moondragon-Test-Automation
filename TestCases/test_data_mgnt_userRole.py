import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.dataTags_pg import DatatagPage
from PageObject.imbeddedTag_pg import ImbeddedTagPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner
# Test passed sept 13 2023
# no Test Case data management created by teammate

class Test_imbeddedTag_delete_add(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    tag_name = "Data Management tag"
    tag_name2 = "Data Management tag"
    detail_msg = "This is your data tag message. Please add, modify, delete tag as you wish"
    add_username = "analyst2"
    field1 = "analyst_tags"
    KQL = "analyst_tags: \"sample ecs tag\" AND analyst_tags: \"Tag for ecs\""
    analyst_tag_name = "sample ecs tag"


    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(5)
        print(cls.driver.title)
        time.sleep(5)

    def test_data_management(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(2)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(1)

        dap = DatatagPage(self.driver)
        dap.DataTagTab()
        time.sleep(5)
        dap.waituntil_createDataTag()
        time.sleep(1)
        dap.create_dataTag()
        time.sleep(1)
        dap.enter_tagName(self.tag_name)
        time.sleep(1)
        dap.enter_tag_detail(self.detail_msg)
        time.sleep(1)
        dap.enter_tag_username(self.add_username)
        time.sleep(1)
        dap.submit_tag()
        time.sleep(2)
        dap.confirm_tagname_modal(self.tag_name)
        time.sleep(1)
        dap.confirm_detailMsg_modal(self.detail_msg)
        time.sleep(1)
        dap.confirm_user_modal(self.add_username)
        time.sleep(1)
        dap.LookGood_button()
        time.sleep(1)

        dap.searchTag_dataMgnt(self.tag_name)
        time.sleep(1)
        dap.click_SearchButton()
        time.sleep(1)
        dap.verify_searchedTagName(self.tag_name)
        time.sleep(1)
        dap.verify_detailMsg(self.detail_msg)
        time.sleep(1)
        dap.verify_owner(self.username)
        time.sleep(1)
        dap.verify_user(self.add_username)
        time.sleep(1)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(1)

        dp = discoverPage(self.driver)
        dp.loadingCheck()
        dp.OpenDate()
        time.sleep(1)
        dp.selectFiveYear()
        time.sleep(1)
        dp.expand_record()
        time.sleep(1)

        dtp = DatatagPage(self.driver)
        dtp.DataTagTab()
        imp = ImbeddedTagPage(self.driver)
        imp.click_addExistingTab()

        imp.waituntilAddExistingTag_popup()
        time.sleep(1)
        imp.enterTagName2(self.tag_name)
        time.sleep(1)
        imp.verify_tag_nameExists()
        time.sleep(1)
        imp.click_existing_header()
        time.sleep(1)
        imp.submit_tag()
        time.sleep(1)
        imp.verify_confirmMsg2()
        time.sleep(1)
        imp.LookGood_button()
        time.sleep(1)

        imp.enter_searchbar(self.tag_name)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        imp.verify_tagnameindoc(self.tag_name)
        time.sleep(1)
        imp.verify_ownerindoc(self.username)
        time.sleep(1)
        imp.verify_descindoc(self.detail_msg)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(1)

        dap.DataTagTab()
        time.sleep(4)
        dap.waitSearchbutton_display()
        dap.searchTag_dataMgnt(self.tag_name)
        time.sleep(2)
        dap.click_SearchButton()
        time.sleep(2)
        dap.click_settingIcon()
        time.sleep(1)
        dap.click_deleteButton()
        time.sleep(1)
        dap.click_deleteTag()
        time.sleep(1)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(1)
        dp.OpenDate()
        time.sleep(1)
        dp.selectFiveYear()
        time.sleep(1)
        dp.expand_record()
        time.sleep(1)

        dtp.DataTagTab()
        time.sleep(1)
        imp.enter_searchbar(self.tag_name)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        imp.verify_NoSearchResult()




    def tearDown(self):
        hp = homePage(self.driver)
        # hp.clickHambergerMenu()
        # time.sleep(1)
        # hp.clickWorkspace_Menu()
        # time.sleep(1)
        #
        # dap = DatatagPage(self.driver)
        # dap.DataTagTab()
        # time.sleep(4)
        # dap.waitSearchbutton_display()
        # dap.searchTag_dataMgnt(self.tag_name)
        # time.sleep(2)
        # dap.click_SearchButton()
        # time.sleep(2)
        # dap.click_settingIcon()
        # time.sleep(1)
        # dap.click_deleteButton()
        # time.sleep(1)
        # # dap.completeDelete_on()
        # time.sleep(1)
        # dap.click_deleteTag()
        # time.sleep(4)
        # # verify toast message?
        # dap.clear_searchbox()
        # time.sleep(1)
        # dap.searchTag2_dataMgnt(self.tag_name2)
        # time.sleep(1)
        # dap.click_SearchButton()
        # time.sleep(3)
        # #bug found below because of remaining bug
        # dap.click_settingIcon()
        # time.sleep(1)
        # dap.click_deleteButton()
        # time.sleep(1)
        # # dap.completeDelete_on()
        # # time.sleep(1)
        # dap.click_deleteTag()
        # time.sleep(1)
        #



        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()



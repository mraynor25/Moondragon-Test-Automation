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

# also work on modify tag entery
# bug is found because of searching mulitple tags in workspace - blocked
#Test Case moon-569

class Test_imbeddedTag_delete_add(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    tag_name = "sample ecs tag"
    tag_name2 = "Tag for ecs"
    detail_msg = "This is your imbedded tag message. Please add, modify, delete tag as you wish"
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

    def test_imbedded_datatag(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
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
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.discover_pg_loads()
        dp.open_index_dropdown()
        time.sleep(1)
        dp.enter_ECSIndex(self.index)
        dp.selectECS_index()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(2)
        dp.selectYear()
        time.sleep(2)
        dp.loadingCheck()
        dp.expand_record()
        time.sleep(1)
        dp.TableTab()
        time.sleep(1)
        get_id = dp.FieldToRef_id()

        dtp = DatatagPage(self.driver)
        dtp.DataTagTab()
        time.sleep(1)
        imp = ImbeddedTagPage(self.driver)
        imp.create_imbeddedTag()
        time.sleep(1)
        imp.verify_createHeaderExist()
        time.sleep(1)
        imp.checkToggleON()
        time.sleep(1)
        imp.enter_tagName(self.tag_name)
        time.sleep(1)
        imp.enter_details(self.detail_msg)
        time.sleep(1)
        imp.click_addUser()
        time.sleep(1)
        imp.enter_additional_username(self.add_username)
        time.sleep(1)
        imp.submit_tag()
        time.sleep(1)
        imp.verify_confirmMsg()
        time.sleep(1)
        imp.LookGood_button()
        time.sleep(1)

        imp.enter_searchbar(self.tag_name)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        imp.verify_tagnameindoc(self.tag_name)
        time.sleep(1)
        imp.verify_userindoc(self.add_username)
        time.sleep(1)
        imp.verify_ownerindoc(self.username)
        time.sleep(1)
        imp.verify_descindoc(self.detail_msg)
        time.sleep(1)

        imp.create_imbeddedTag()
        time.sleep(1)
        imp.verify_createHeaderExist()
        time.sleep(1)
        imp.checkToggleOFF()
        time.sleep(1)
        imp.enter_tagName2(self.tag_name2)
        time.sleep(1)
        imp.enter_details(self.detail_msg)
        time.sleep(1)
        imp.click_addUser()
        time.sleep(1)
        imp.enter_additional_username(self.add_username)
        time.sleep(1)
        imp.submit_tag()
        time.sleep(1)
        imp.verify_confirmMsg2()
        time.sleep(1)
        imp.LookGood_button()
        time.sleep(4)
        imp.clear_searchInput()
        time.sleep(1)
        imp.enter_searchbar2(self.tag_name2)
        time.sleep(2)
        imp.verify_NoSearchResult()
        time.sleep(1)
        imp.click_addExistingTab()
        time.sleep(1)
        imp.waituntilAddExistingTag_popup()
        time.sleep(1)
        imp.enterTagName(self.tag_name2)
        time.sleep(1)
        imp.click_existing_header()
        time.sleep(1)
        imp.submit_tag()
        time.sleep(1)
        imp.verify_confirmMsg2()
        time.sleep(1)
        imp.LookGood_button()
        time.sleep(2)
        imp.verify_tagname2indoc(self.tag_name2)
        time.sleep(1)
        imp.verify_userindoc(self.add_username)
        time.sleep(1)
        imp.verify_ownerindoc(self.username)
        time.sleep(1)
        imp.verify_descindoc(self.detail_msg)
        time.sleep(2)

        dp.search_searchfield(self.field1)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.enterKQL(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.verify_imbeddedTagsindoc(self.tag_name, self.tag_name2)
        time.sleep(1)

        dp.expand_record()
        time.sleep(1)
        dtp.DataTagTab()
        time.sleep(1)
        imp.delete_imbeddedTag()
        time.sleep(1)
        imp.waituntilDeleteTag_popup()
        time.sleep(1)
        imp.enterTagName(self.tag_name2)
        time.sleep(1)
        imp.submit_tag()
        time.sleep(1)
        imp.verify_confirmMsg2()
        time.sleep(1)
        imp.delete_confirm_imbeddedTag()
        time.sleep(1)
        imp.enter_searchbar2(self.tag_name2)
        time.sleep(2)
        imp.verify_NoSearchResult()
        time.sleep(1)

        dp.click_refresh()
        time.sleep(1)
        dp.verify_analystTagsNotExist(self.analyst_tag_name)



    def tearDown(self):
        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(1)

        dap = DatatagPage(self.driver)
        dap.DataTagTab()
        time.sleep(1)
        dap.waitSearchbutton_display()
        dap.searchTag_dataMgnt(self.tag_name)
        time.sleep(4)
        dap.click_SearchButton()
        time.sleep(2)
        dap.click_settingIcon()
        time.sleep(2)
        dap.click_deleteButton()
        time.sleep(1)
        # dap.completeDelete_on()
        time.sleep(1)
        dap.click_deleteTag()
        time.sleep(4)
        # verify toast message?
        dap.clear_searchbox()
        time.sleep(1)
        dap.searchTag2_dataMgnt(self.tag_name2)
        time.sleep(1)
        dap.click_SearchButton()
        time.sleep(3)
        #bug found below because of remaining bug
        dap.click_settingIcon()
        time.sleep(1)
        dap.click_deleteButton()
        time.sleep(1)
        # dap.completeDelete_on()
        # time.sleep(1)
        dap.click_deleteTag()
        time.sleep(1)






        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()



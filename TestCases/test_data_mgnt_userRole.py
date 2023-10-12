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
# Test passed oct 12 2023
# no Test Case data management created by teammate

class Test_imbeddedTag_delete_add(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    tag_name = "sample tag for data mgnt"
    detail_msg = "This is your data tag message. Please add, modify, delete tag as you wish"
    add_username = "analyst2"


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

    def test_data_userrole_management(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(4)
        Ip.clickdefault()
        time.sleep(4)

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
        dap.submit_tag()
        time.sleep(2)
        dap.confirm_tagname_modal2(self.tag_name)
        time.sleep(1)
        dap.confirm_detailMsg_modal(self.detail_msg)
        time.sleep(1)
        dap.LookGood_button()
        time.sleep(1)

        dap.searchTag_dataMgnt(self.tag_name)
        time.sleep(1)
        dap.click_SearchButton()
        time.sleep(1)
        dap.verify_searchedTagName2(self.tag_name)
        time.sleep(1)
        dap.verify_detailMsg(self.detail_msg)
        time.sleep(1)


        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername2(self.username2)
        time.sleep(1)
        Ip.setPassword2(self.password2)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault2()
        time.sleep(4)

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
        imp.verify_tag_nameNotExists()
        time.sleep(1)
        imp.click_close()
        time.sleep(1)

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
        dap.verifyButtons4AdditionalUser()
        time.sleep(1)

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(2)
        Ip.clickdefault()
        time.sleep(3)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(1)

        dap = DatatagPage(self.driver)
        dap.DataTagTab()
        time.sleep(5)
        dap.waitSearchbutton_display()
        dap.searchTag_dataMgnt(self.tag_name)
        time.sleep(2)
        dap.click_SearchButton()
        time.sleep(2)
        dap.click_settingIcon()
        time.sleep(1)
        dap.verifyButtons4owner()
        time.sleep(1)



    def tearDown(self):
        dap = DatatagPage(self.driver)
        dap.click_deleteButton()
        time.sleep(1)
        dap.click_deleteTag()
        time.sleep(1)


        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()



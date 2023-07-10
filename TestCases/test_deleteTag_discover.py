from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.dataTags_pg import DatatagPage
from PageObject.workspace_pg import workspacePage
import time
import unittest
import HtmlTestRunner
# we no longer have DATA TAG SECTION in the discover as feature is modified OBE
#Test failed for toast messages adding tag April 21, 2023

#Moon-154 Test Case
class TestDelete_tags(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    tag_1 = "del_tag"
    tag_2 = "del_tag2"
    username2 = "analyst2"
    password2 = "Password1!"

    @classmethod
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(15)
        print(cls.driver.title)
        time.sleep(5)


    def test_deleteTag_discover(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(4)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.openIndexMenu()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.selectYear()
        time.sleep(2)

       # self.driver.execute_script("window.scrollBy(0,1000)", "")
        dp.ExpandRecord()
        time.sleep(2)
        dp.TableTab()
        time.sleep(2)

        dtp = DatatagPage(self.driver)
        store_id = dtp.get_ref_id()
        dtp.DataTagTab()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        dtp.addNewTag()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(2)
        dtp.fieldToRef_arrow()
        time.sleep(3)
        dtp.selectDropdownMenu()
        time.sleep(2)
        dtp.enter2Tags(self.tag_1, self.tag_2)
        time.sleep(1)
        dtp.submit_tag()
        time.sleep(3)
        dtp.verify_entered2Tags(self.tag_1, self.tag_2)
        dtp.LookGood_button()
        time.sleep(4)
        dtp.verify_entered2Tags(self.tag_1, self.tag_2)
       # dp.closeTags_modalWindow()
        #bug found below with toast messages
       # dtp.verify_entered2Tags(self.tag_1, self.tag_2)


        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        time.sleep(7)
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(3)

        wp = workspacePage(self.driver)
        wp.click_myDataTagTab()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(4)
        wp.nofind_deleted_tag(self.tag_1, self.tag_2)
        time.sleep(2)

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(6)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(3)

        wp.click_myDataTagTab()
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(2)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)
        dp.openIndexMenu()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.selectYear()
        time.sleep(2)
        dp.search_query_id(store_id)
        time.sleep(3)
        dp.clickUpdateButton()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,2400)", "")

        dp.ExpandRecord()
        time.sleep(3)
        dtp.DataTagTab()
        time.sleep(2)
        dtp.verifyTag_notfound(self.tag_1, self.tag_2)


if __name__ == '__main__':
    unittest.main()
from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.dashboardSearch_pg import dashboardSearchPage
from PageObject.dashboard_pg import dashboardPage
from PageObject.discover_pg_copy2 import discoverPage
from PageObject.workspace_pg import workspacePage
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner

#Test failed OBE because of expand data tag has no data line 79 This test case is OBE

#Moon-154 Test Case
class TestfavIndex(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "welcome"
    tag_1 = "del_IP"
    tag_2 = "del_IP2"
    username2 = "analyst2"
    password2 = "Password1!"
# test failed because of fail to load data tag panel april 24 line 79 failed

    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(13)
        print(cls.driver.title)
        time.sleep(5)


    def test_delete_tag_dash(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(2)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDashboard()
        time.sleep(3)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(4)
        dsp.welcomeDashboard()
        time.sleep(2)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(1)
        dap.selectLastOneyear()
        time.sleep(2)
        dap.clickAnalystNotes()
        time.sleep(2)
        dap.click_dataTagsTab()
        self.driver.implicitly_wait(5)

        dap.expand_dataTag()
        time.sleep(2)
        dap.click_idlink()

        dp = discoverPage(self.driver)
        dp.loadingCheck()
        time.sleep(3)

        dap.click_notesTab()
        time.sleep(9)
        self.driver.execute_script("window.scrollBy(0,5000)", "")
        dap.add_NewTag()
        time.sleep(3)
        dap.click_fieldtoRefArrow()
        time.sleep(3)

        ref_menu = dap.getRefMenu()
        dap.selectMenu()
        time.sleep(2)
        dap.check4occurance()
        time.sleep(3)
        dap.enterTags(self.tag_1, self.tag_2)
        dap.submit_tags()
        time.sleep(2)
        dap.verify_enteredTags(self.tag_1, self.tag_2)
        time_val = dap.store_timevalue()
        dap.click_lookgood()
        time.sleep(2)
        dap.verify_enteredTags2(self.tag_1, self.tag_2)
        dap.close_deepdive()
        time.sleep(1)
        dap.close_analystNotes()
        time.sleep(2)

        lp = loginPage(self.driver)
        lp.logout()
        time.sleep(11)

        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        time.sleep(7)
        Ip.clickdefault()
        time.sleep(5)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(3)

        wp = workspacePage(self.driver)
        wp.click_myDataTagTab()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        time.sleep(3)
        wp.click_row100()
        time.sleep(3)
        wp.find_tagsfromList(self.tag_1, self.tag_2)

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
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
        self.driver.execute_script("window.scrollBy(0, 6000)", "")
        time.sleep(3)
        wp.deleteTags(self.tag_1, self.tag_2)
        time.sleep(2)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)

        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.welcomeDashboard()
        time.sleep(2)

        dap.clickAnalystNotes()
        self.driver.implicitly_wait(6)
        dap.click_dataTagsTab()
        time.sleep(2)
        dap.search_deletedTags1(self.tag_1)
        dap.noItemFound_analystResults()
        dap.search_deletedTags2(self.tag_2)
        time.sleep(5)
        dap.noItemFound_analystResults()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
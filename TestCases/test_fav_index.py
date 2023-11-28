from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.dataView_pg import dataViewPage
from PageObject.dashboardSearch_pg import dashboardSearchPage
from PageObject.dashboard_pg import dashboardPage
from PageObject.workspace_pg import workspacePage
from PageObject.discover_pg import discoverPage
import time
import unittest
import HtmlTestRunner

# index name is not same as CCU
#Test passed oct 12 2023 discover copy2 applied

#Moon-154 Test Case, Moon-98 User story
class TestfavIndex(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    search_val = "favorited-dashboards*"
    dashboard_name = "http [MOONDRAGON]"
    dashboard_name2 = "Welcome"
    num = "2"
    index_name2 = "favorited-dashboards*"
    value_dropdown = "last"
    value_y = "y"
    KQL = "username : \"analyst\""
    input_index = "favorited-dashboards*"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    dashboard_name3 = "smtp [MOONDRAGON]"

    @classmethod
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        # self.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(20)
        print(cls.driver.title)
        time.sleep(5)


    def test_favorite_index(self):
        lp = loginPage(self.driver)
        lp.setUsername(self.username)
        time.sleep(1)
        lp.setPassword(self.password)
        time.sleep(1)
        lp.clickLogin()
        time.sleep(3)
        lp.clickdefault()
        time.sleep(4)


        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickStackMgntMenu()
        time.sleep(4)
        hp.clickDataView()
        time.sleep(2)

        dvp = dataViewPage(self.driver)
        dvp.enterSearchField(self.search_val)
        time.sleep(10)
        # look below search fav exist
        dvp.search_favExist()
        time.sleep(5)

        hp.clickDashboard()
        time.sleep(3)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(2)
        dsp.clickHTTPlink()
        time.sleep(3)


        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(5)
        dap.selectLastOneyear()
        time.sleep(3)
        dap.addToWorkspace()
        time.sleep(3)
        dap.submit_workspace()
        time.sleep(4)
        dap.dashboard_menu()
        time.sleep(3)

        dsp.enterSearchDashboard2(self.dashboard_name2)
        time.sleep(2)

        dsp.welcomeDashboard()
        time.sleep(4)
        dap.addToWorkspace()
        time.sleep(1)
        dap.submit_workspace()
        time.sleep(2)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickWorkspace_Menu()
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(5)

        wp = workspacePage(self.driver)
        count_dash = wp.countTotal_dashboard()

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)
        self.driver.implicitly_wait(4)

        dip = discoverPage(self.driver)
        dip.openIndex()
        time.sleep(2)
        dip.search_index(self.index_name2)
        time.sleep(2)
        dip.selectFav_index()
        time.sleep(2)
        dip.enterKQL(self.KQL)
        time.sleep(3)
        dip.clickUpdateButton()
        time.sleep(7)
        numofRec = dip.verifynumofRec()
        self.assertEqual(int(numofRec), count_dash, "Test failed: Number of record(s) of fav index is not matching")
        time.sleep(2)

        hp.clickHambergerMenu()
        time.sleep(3)
        hp.clickWorkspace_Menu()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(5)

        wp.delete_workspace(count_dash)
        time.sleep(4)
        removeDash_message = wp.remove_ws_msg()

        self.assertEqual("Remove This Dashboard", removeDash_message, "Test failed: No delete message for removing dashboard")
        wp.remove_dashYes()
        time.sleep(1)
        Update_rec = wp.updatedDash_Rec()  #UpdatedDashboardRec

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        dip.openFavIndexMenu()
        time.sleep(2)
        dip.enterKQLuserElastic()
        time.sleep(3)
        dip.clickUpdateButton()
        time.sleep(2)
        numofRec2 = dip.verifyNumofRec2()
        self.assertEqual(int(numofRec2), len(Update_rec), "Test failed: Number of record(s) of fav index is not match")
        time.sleep(2)

        lp.logout()
        time.sleep(3)
        lp.waituntilUsername_appear()
        self.driver.implicitly_wait(5)
        lp.setUsername2(self.username2)
        time.sleep(1)
        lp.setPassword2(self.password2)
        lp.clickLogin()
        time.sleep(12)
        lp.clickdefault2()
        time.sleep(2)

        hp.clickHambergerMenu()
        hp.clickDashboard()
        time.sleep(3)

        dsp.enterSearchDashboard3(self.dashboard_name3)
        time.sleep(2)
        dsp.clicksmtplink()
        time.sleep(2)

        dap.opendate()
        time.sleep(1)
        dap.dropdown_last(self.value_dropdown)
        time.sleep(2)
        dap.enternumof2ndYear()
        time.sleep(2)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()
        time.sleep(3)
        dap.addToWorkspace()
        time.sleep(1)
        dap.submit_workspace()
        time.sleep(1)
        dap.toastMsg_addworkspace()
        time.sleep(2)

        hp.clickHambergerMenu()
        hp.clickWorkspace_Menu()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)

        added2ndDash = wp.added2ndUser_workspace()
        lp.logout4user()
        time.sleep(4)
        lp.elasticLogin()
        lp.setUsername(self.username)
        time.sleep(1)
        lp.setPassword(self.password)
        time.sleep(1)
        lp.clickLogin()
        time.sleep(3)
        lp.clickdefault2()
        time.sleep(4)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)
        dip.openIndex()
        dip.selectFavIndex(self.input_index)
        time.sleep(2)
        dip.enterKQLuserElastic2()
        time.sleep(3)
        dip.clickUpdateButton()
        time.sleep(5)
        added3rdDash = dip.verifyNumofRec3()
        self.assertEqual(int(added3rdDash), len(added2ndDash), "Test failed: Number of record(s) of fav index is not match for 2nd user")


    def tearDown(cls):

        cls.driver.close()
        cls.driver.quit()


#if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/monica.raynor/PycharmProjects/MoonDragon/QA_Results'))


if __name__ == '__main__':
    unittest.main()

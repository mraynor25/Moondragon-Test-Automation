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
from PageObject.workspace_pg import workspacePage
from selenium.webdriver.common.by import By

import time
import unittest
import HtmlTestRunner

#Test pass DEC 11 2023

class Test_decoder_dashboard(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "Suricata [MOONDRAGON]"
    value_dropdown = "last"
    num = "1"
    value_y = "y"
    Query_1 = "rule.category: \"A Network Trojan was detected\" AND network.transport : \"tcp\""


    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(15)
        print(cls.driver.title)
        time.sleep(5)


    def test_queries_workspace(self):
        lp = loginPage(self.driver)
        lp.elasticLogin()
        lp.setUsername(self.username)
        time.sleep(1)
        lp.setPassword(self.password)
        time.sleep(1)
        lp.clickLogin()
        time.sleep(3)
        lp.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)

        ds = dashboardSearchPage(self.driver)
        ds.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        ds.clickSuricatalink()
        time.sleep(2)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(2)
        dap.dropdown_last(self.value_dropdown)
        dap.enterNumberofYear(self.num)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()
        time.sleep(1)
        getTime = dap.getTimeFrame()
        dap.enterKQL_query(self.Query_1)
        dap.pressUpdate()
        time.sleep(2)
        dap.addToWorkspace()
        time.sleep(3)
        dap.checkbox_addToworkspaceMenu()
        dap.toastMsg_addworkspace()

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickWorkspace_Menu()
        self.driver.execute_script("window.scrollBy(0,3000)", "")
        time.sleep(8)
        self.assertTrue(len(self.driver.find_elements(By.XPATH, "//strong[contains(text(),'Suricata [MOONDRAGON]')]")) > 0)

        wp = workspacePage(self.driver)
        wp.last_favorite()
        time.sleep(10)
        TimeFilter = wp.getMyTimefilter()
        self.assertEqual(getTime, TimeFilter, "test failed, time filter query should match with dashboard")


if __name__ == '__main__':
    unittest.main()
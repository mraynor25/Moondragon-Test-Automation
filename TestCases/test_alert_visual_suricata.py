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

from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner

#Test passed sept 25 2023 modified

#Moon-154 Test Case
class TestAlert_suricata(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "suricata"
    value_dropdown = "last"
    num = "1"
    value_y = "y"
    Query_1 = "rule.description: \"FakeSSLXOR XOR Key Exchange\"  and rule.category: \"A Network Trojan was detected\""
    verifyoutput = "A Network Trojan was detected"
    verifyoutput2 = "FakeSSLXOR XOR Key Exchange"
    Query_name = "Rule_Query"

    @classmethod
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(5)
        print(cls.driver.title)


    def test_alert_suricata(self):
        Ip = loginPage(self.driver)
        Ip.clickdefault()
        time.sleep(3)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(2)
        Ip.clickLogin()
        time.sleep(12)
        Ip.clickdefault2()
        time.sleep(10)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDashboard()
        time.sleep(2)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.clickSuricatalink()
        time.sleep(2)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(1)
        dap.dropdown_last(self.value_dropdown)
        dap.enterNumberofYear(self.num)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()
        time.sleep(5)
        # dap.clickRefresh()
        dap.verify_alert_suricata()
        dap.enterKQL_query(self.Query_1)
        dap.pressUpdate()
        time.sleep(3)
        dap.verifyOutput1(self.verifyoutput)
        dap.openSaveQuery()
        dap.saveCurrentquery()
        time.sleep(1)
        dap.enterQueryName(self.Query_name)
        time.sleep(2)
        dap.toggleON_saveQuery()
        time.sleep(1)
        dap.SaveQuery()
        time.sleep(1)
        dap.verify_alertRuleQuery()
        dap.dashboard_menu()
        time.sleep(2)

        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.clickSuricatalink()
        time.sleep(2)

        dap.openSaveQuery()
        time.sleep(3)
        dap.verifySavedQuery2()
        dap.verify_alert_suricata()


if __name__ == '__main__':
    unittest.main()
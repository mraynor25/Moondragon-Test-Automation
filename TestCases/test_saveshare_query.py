import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.dashboardSearch_pg import dashboardSearchPage
from PageObject.dashboard_pg import dashboardPage
import time


class TestMethods_Xpanse(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "suricata [MOONDRAGON]"
    Query_1 = "destination.ip: 194.5.249.157 or rule.category: A Network Trojan was detected"
    query_name = "IP_Trojan_Query"
    username2 = "analyst2"
    password2 = "Welcome2020!"

    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(20)
        print(cls.driver.title)
        time.sleep(5)

    def test_saveShare_query(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(2)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDashboard()
        time.sleep(3)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        dsp.clickSuricatalink()

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(6)
        dap.select_Year()
        time.sleep(2)
        dap.enterKQL_query(self.Query_1)
        time.sleep(2)
        dap.pressUpdate()
        time.sleep(3)
        dap.openSaveQuery()
        time.sleep(2)
        dap.saveCurrentquery()
        time.sleep(3)
        dap.enterQueryName(self.query_name)
        time.sleep(1)
        dap.SaveQuery()
        time.sleep(2)
        dap.toastMsg()
        time.sleep(2)
        dap.shareButton()
        time.sleep(1)
        dap.permalink()
        time.sleep(2)
        dap.radioButton_snapshot()
        time.sleep(1)
        dap.copyLink()
        time.sleep(3)

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
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)
        dsp.welcomeDashboard()
        time.sleep(2)

        dap.openSave_query()
        time.sleep(3)
        dap.verifySavedQuery()
        time.sleep(3)
        dap.verifyQuery()
        time.sleep(1)
        dap.opendate()
        time.sleep(1)
        dap.checkLastDate()
        dap.dateDropdown()
        dap.checkDate()
        dap.opendate()
        time.sleep(2)
        dap.openSaveQuery()
        time.sleep(2)
        dap.deleteIcon()
        time.sleep(2)

        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

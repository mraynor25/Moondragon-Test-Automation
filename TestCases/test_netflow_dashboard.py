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
import unittest
import HtmlTestRunner

# netflow dashboard is not exist therefore, unable to run this scripts. failed
# currently working on it

class TestfavIndex(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "netflow"
    Query_1 = "sensor.name : * AND source.port: 443"
    dest_ip_value = "65.254.219.206"
    source_port_value = "443"
    value_dropdown = "last"
    num = "1"
    value_y = "y"


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


    def test_netflow_dashboard(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(11)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDashboard()
        time.sleep(2)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.click_netflowLink()
        time.sleep(5)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(2)
        dap.dropdown_last(self.value_dropdown)
        dap.enterNumberofYear(self.num)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()

        dap.enterKQL_query(self.Query_1)
        time.sleep(2)
        dap.remove_addedFilters()
        time.sleep(1)
        dap.pressUpdate()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(2)

        dap.verify_destinIP(self.dest_ip_value)
        dap.verify_sourcePort(self.source_port_value)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


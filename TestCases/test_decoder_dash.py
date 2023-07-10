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


import time
import unittest
import HtmlTestRunner

# NOt added to PO update
#Moon-64 Test Case
class Test_decoder_dashboard(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "decoder"
    value_dropdown = "last"
    num = "5"
    value_y = "y"
    Query_1 = "decoder_name: \"lucky7\""
    filterField_value = "content.command_type"
    filter_value = "CONNECT"
    data_query = "Lucky7"


#Test pass May15 2023, changed filter field and value, changed 5 year
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


    def test_decoder_dashboard(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(10)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.clickdecoderlink()
        time.sleep(2)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(2)
        dap.dropdown_last(self.value_dropdown)
        dap.enterNumberofYear(self.num)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()
        time.sleep(2)
        dap.enterKQL_query(self.Query_1)
        time.sleep(2)
        dap.addFilter()
        time.sleep(3)
        dap.addArrow_dropdown()
        time.sleep(3)
        dap.typeFilter_field(self.filterField_value)
        time.sleep(4)
        dap.pressEnter()
        time.sleep(2)
        dap.operator_arrow()
        time.sleep(2)
        dap.selectOperator()
        time.sleep(3)
        dap.TypeValue(self.filter_value)
        time.sleep(2)
        dap.saveButton()
        time.sleep(2)
        dap.pressUpdate()
        time.sleep(4)
        dap.verifyTitle_table(self.data_query)
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
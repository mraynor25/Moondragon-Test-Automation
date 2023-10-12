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

#Test passed oct 12 2023

#Moon-154 Test Case
class TestfavIndex(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    welcome_dashboard = "Welcome [MOONDRAGON]"
    dashboard_name = "http [MOONDRAGON]"
    value_dropdown = "last"
    num = "1"
    value_y = "y"
    enter_welcome = "Welcome"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    dashboard_name2 = "smtp"

    @classmethod
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(10)
        print(cls.driver.title)
        time.sleep(5)


    def test_favorite_index(self):
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
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(3)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(4)
        dsp.clickHTTPlink()
        time.sleep(3)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(2)
        dap.dropdown_last(self.value_dropdown)
        dap.enterNumberofYear(self.num)
        dap.selectYear(self.value_y)
        time.sleep(2)
        dap.clickApply()
        time.sleep(2)
        dap.addToWorkspace()
        time.sleep(1)
        dap.submit_workspace()
        time.sleep(3)
        dap.toastMsg_addworkspace()
        time.sleep(2)
        dap.dashboard_menu()
        time.sleep(3)

        dsp.enterSearchDashboard(self.enter_welcome)
        time.sleep(2)
        dsp.welcomeDashboard()
        time.sleep(3)

        dap.addToWorkspace()
        time.sleep(1)
        dap.submit_workspace()
        time.sleep(2)
        dap.toastMsg_addworkspace()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)

        wp = workspacePage(self.driver)
        wp.clickWorkspace_Menu()
        time.sleep(3)
        wp.firstUser_dashboard()
        FirstUser_dash = wp.firstUser_dashboard()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        wp.verifyHTTP_dash()
        wp.verifyWelcome_dash()

        Ip.logout()
        time.sleep(9)
        Ip.elasticLogin()
        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        time.sleep(10)
        Ip.clickdefault()
        time.sleep(2)

        hp.clickHambergerMenu()
        time.sleep(1)
        wp.clickWorkspace_Menu()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        wp.verify_addedDashboard(FirstUser_dash)
        time.sleep(2)
        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard2()
        time.sleep(2)

        dsp.enterSearchDashboard2(self.dashboard_name2)
        time.sleep(1)
        dsp.clicksmtplink()
        time.sleep(2)

        dap.addToWorkspace()
        time.sleep(1)
        dap.submit_workspace()
        time.sleep(2)
        # dap.toastMsg_addworkspace()
        # time.sleep(5)
        # Unable to verify when there is so many utilities alert messages pops up (We have no control over this)

        hp.clickHambergerMenu()
        time.sleep(1)
        wp.clickWorkspace_Menu()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        wp.verifySMTP_dash()
        time.sleep(3)
        self.assertFalse(len(self.driver.find_elements(By.XPATH, "//strong[contains(text(),'HTTP [MOONDRAGON]')]")) > 0)

        Ip.logout()
        time.sleep(5)
        Ip.elasticLogin()
        time.sleep(2)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(10)
        Ip.clickdefault2()
        time.sleep(5)
        hp.clickHambergerMenu()
        time.sleep(1)

        hp.clickWorkspace_Menu()
        time.sleep(3)
        self.assertFalse(len(self.driver.find_elements(By.XPATH, "//strong[contains(text(),'SMTP [Moondragon]')]")) > 0)
        self.assertTrue(len(self.driver.find_elements(By.XPATH, "//strong[contains(text(),'*Welcome [MOONDRAGON]')]")) > 0)
        self.assertTrue(len(self.driver.find_elements(By.XPATH, "//strong[contains(text(),'HTTP [MOONDRAGON]')]")) > 0)

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
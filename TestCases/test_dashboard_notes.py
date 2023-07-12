from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.dashboardSearch_pg import dashboardSearchPage
from PageObject.dashboard_pg import dashboardPage
from PageObject.discover_pg import discoverPage
import re
import time
import unittest

#test pass may 25 2023 applied discover


class TestMethods_Xpanse(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    dashboard_name = "welcome"
    verify_comment = "Add Dashboard Comment"
    dash_notes = "You’re in the home stretch of your release cycle. It’s time to ship your product...and you have to write release notes. " \
                 "Many companies treat release notes."
    dashboard_name2 = "HTTP [MOONDRAGON]"
    dashboard_name3 = "FTP [MOONDRAGON]"
    username2 = "analyst2"
    password2 = "Welcome2020!"


    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(14)
        time.sleep(2)

    def test_dashboard_notes(self):
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
        hp.clickDashboard()
        time.sleep(2)

        dsp = dashboardSearchPage(self.driver)
        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(2)
        dsp.welcomeDashboard()
        time.sleep(2)

        dbp = dashboardPage(self.driver)
        dbp.opendate()


        dbp.selectLastOneyear()
        time.sleep(2)
        dbp.clickAnalystNotes()
        time.sleep(2)
        dbp.clickDashboard_notes()
        time.sleep(2)
        dbp.click_addnotes()
        time.sleep(2)
        dbp.verify_dashboardComment(self.verify_comment)
        dbp.enter_dashboardnotes(self.dash_notes)
        dbp.submit_dashNotes()
        time.sleep(2)
        dbp.notesAdded_toastMsg()
        capture_username_time = dbp.capture_usernametime()
        dp = discoverPage(self.driver)
        dp.loadingCheck()
        dbp.verify_entered_dashnotes(self.dash_notes)

        dp.loadingCheck()

        hp = homePage(self.driver)
        hp.clickDashboardMenu()
        time.sleep(2)
        dsp.enterSearchDashboard3(self.dashboard_name3)
        time.sleep(2)
        dsp.clickFTPlink()
        time.sleep(2)
        dbp.clickAnalystNotes()
        time.sleep(2)
        dbp.clickDashboard_notes()
        time.sleep(2)
        dbp.verify_dashboardnotesNotFound(capture_username_time)

        hp.clickDashboardMenu()
        time.sleep(2)

        dsp.enterSearchDashboard2(self.dashboard_name2)
        time.sleep(1)
        dsp.clickHTTPlink()
        time.sleep(3)

        dbp.clickAnalystNotes()
        time.sleep(2)
        dbp.clickDashboard_notes()
        time.sleep(2)
        dbp.verify_dashboardnotesNotFound(capture_username_time)

        Ip.logout()
        time.sleep(8)
        Ip.elasticLogin()
        time.sleep(1)

        # Login as another user

        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)

        dsp.welcomeDashboard()
        time.sleep(2)
        dbp.clickAnalystNotes()
        time.sleep(2)
        dbp.clickDashboard_notes()
        time.sleep(2)
        find_dashnotes = dbp.findDashNotes()
        print(find_dashnotes)
        print(capture_username_time)
        assert find_dashnotes == capture_username_time
        time.sleep(3)

        dbp.delete_icon_sessionNotes()
        time.sleep(2)
        toast_msg = dbp.toastMsg_analystNotes()
        assert toast_msg == "Error: Dashboard comment was not deleted-Username did not match"
        time.sleep(2)

        Ip.logout()
        time.sleep(5)
        Ip.elasticLogin()
        self.driver.implicitly_wait(6)
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
        Ip.clickLogin()
        time.sleep(6)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDashboard()
        time.sleep(2)

        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(2)
        dsp.welcomeDashboard()
        time.sleep(2)
        dbp.clickAnalystNotes()
        time.sleep(2)
        dbp.clickDashboard_notes()
        time.sleep(2)
        find_dash_notes1 = dbp.findDashNotes1()
        print(find_dash_notes1)
        assert find_dash_notes1 == capture_username_time
        dbp.delete_icon_sessionNotes()
        time.sleep(2)
        delete_toast_msg = dbp.deletetoastMsg()
        assert delete_toast_msg == "Dashboard comment deleted successfully"

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


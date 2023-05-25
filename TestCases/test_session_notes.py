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


# Test pass may 15 2023

class TestMethods_sessionNotes(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    Query_1 = "destination.ip: 194.5.249.157 or rule.category: A Network Trojan was detected"
    Query_name = "dest_IP_rule_query"
    session_name = "dest_IP_rule_query"
    session_notes = "This is a destination IP rule query notes."
    dashboard_name = "files"

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

    def test_xpanse(self):
        lp = loginPage(self.driver)
        lp.setUsername(self.username)
        time.sleep(1)
        lp.setPassword(self.password)
        time.sleep(1)
        lp.clickLogin()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDashboard()
        time.sleep(3)

        dsp = dashboardSearchPage(self.driver)
        dsp.welcomeDashboard()
        time.sleep(2)

        dap = dashboardPage(self.driver)
        dap.opendate()
        time.sleep(1)
        dap.selectLastOneyear()
        time.sleep(2)
        dap.enterKQL_query(self.Query_1)
        time.sleep(2)
        dap.pressUpdate()
        time.sleep(3)
        dap.openSavedQuery()
        time.sleep(2)
        dap.save_currentQuery()
        time.sleep(3)

        dap.enterQueryName(self.Query_name)
        dap.toggleON_saveQuery()
        time.sleep(3)
        dap.saveButton()
        time.sleep(2)
        dap.saveToastMsg()
        dap.clickAnalystNotes()
        time.sleep(2)
        dap.click_SessionNotesTab()
        dap.sessionField(self.session_name)
        time.sleep(3)
        dap.select_query()
        time.sleep(2)
        dap.click_addnotes()
        time.sleep(2)
        dap.enter_sessionnotes(self.session_notes)
        time.sleep(2)
        dap.submit_sessionnotes()
        time.sleep(2)
        dap.notesAdded_toastMsg()
        first_addedDash = dap.addedDash1()
        first_addedDashNotes = dap.addedDash_notes1()
        dap.dashboard_menu()
        time.sleep(1)

        dsp.enterSearchDashboard(self.dashboard_name)
        time.sleep(1)
        dsp.click_filesLink()
        time.sleep(2)
        dap.clickAnalystNotes()
        time.sleep(1)
        self.driver.implicitly_wait(18)
        dap.click_SessionNotesTab()
        time.sleep(2)
        dap.sessionField(self.session_name)
        dap.select_query()
        time.sleep(2)
        second_addeddash = dap.add_dash2()
        assert first_addedDash == second_addeddash
        second_addeddashNotes = dap.add_dashNotes2()
        assert first_addedDashNotes == second_addeddashNotes
        dap.delete_icon_sessionNotes()
        time.sleep(2)
        deleteToastMsg = dap.delete_toastMsg()
        assert deleteToastMsg == "Session comment deleted successfully"
        dap.close_analystNotes()
        time.sleep(1)

    def tearDown(self):
        dap = dashboardPage(self.driver)
        dap.openSavedQuery()
        time.sleep(2)
        dap.teardown_pagin_del_savedQuery()

        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


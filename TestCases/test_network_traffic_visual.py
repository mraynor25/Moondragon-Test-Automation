from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.dashboard_pg import dashboardPage
from PageObject.visualize_pg import visualizePage
import time
import unittest

#Fix the test for adding last 5 years line 88 errors chose pie chart

class TestMethods(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    suricata_index = "ecs-suricata"
    value = "last"
    num = "5"
    year = "y"
    datasource4 = "related.ip"
    field = "@version"
    title = "suricata related IP chart"
    dashboard_name = "Suricata [Moondragon]"
    filterField = "source.port"
    operator_name = "exists"


    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(17)
        print(cls.driver.title)
        time.sleep(5)

    def test_network_traffic_visual(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(9)
        Ip.clickdefault()
        time.sleep(4)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(3)

        dp = discoverPage(self.driver)
        dp.open_index_dropdown()
        time.sleep(3)
        dp.indexSearchbox(self.suricata_index)
        time.sleep(3)
        dp.OpenDate()
        time.sleep(1)
        dp.dateDropdown(self.value)
        time.sleep(2)
        dp.numofyear(self.num)
        time.sleep(2)
        dp.clickApply()
        # self.driver.implicitly_wait(10)
        time.sleep(5)
        dp.searchfield4(self.datasource4)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.clickfieldTovisual()
        time.sleep(2)
        dp.clickVisualButton()
        time.sleep(12)

        vp = visualizePage(self.driver)
        vp.selectPieChart()
        self.driver.execute_script("window.scrollBy(0,100)", "")
        time.sleep(2)
        vp.clickPlusIconTodrop()
        vp.enterFieldtoVisual(self.field)
        vp.clickSelectVersion()
        time.sleep(3)
        vp.clickSave()
        time.sleep(8)
        saveLen_value = vp.get_saveLenVis()
        self.assertEqual("Save Lens visualization", saveLen_value, "Save modal does not pop-up")
        vp.enter_visual_title(self.title)
        time.sleep(1)
        vp.textboxDash(self.dashboard_name)
        time.sleep(1)
        vp.select_suricata()
        time.sleep(1)
        vp.saveTogoDashboard()
        time.sleep(4)

        dap = dashboardPage(self.driver)
        confirmTitle = dap.get_Title()
        self.assertEqual(confirmTitle[0].text, "Editing Suricata [MOONDRAGON]", "User is not on Suricata Dasbhoard screen")
        print(confirmTitle[0].text)
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(7)

        confirm_visual_rel_ip = dap.get_visual_relIP()
        self.assertEqual("suricata related IP chart", confirm_visual_rel_ip, "Test failed, visual is not added in the suricata dashboard")
        self.driver.execute_script("window.scrollBy(0,-1000)", "")
        time.sleep(2)
        dap.addFilter()
        time.sleep(2)
        dap.enteraddedfilter_field(self.filterField)
        time.sleep(1)
        dap.select_sourceip()
        time.sleep(2)
        # dap.operator_arrow()
        # time.sleep(2)
        # dap.typeFilter_field(self.filter_value)
        # time.sleep(6)
        # dap.pressEnter()
        # time.sleep(1)
        # dap.operator_arrow()
        # time.sleep(2)
        dap.selectOperator_menu(self.operator_name)
        dap.selectExist()
        time.sleep(1)
        # dap.pressEnter()
        # time.sleep(2)
        dap.click_save_addfilter()
        time.sleep(3)
        toast_msg = dap.get_toastMsg()
        self.assertEqual("Dashboard \'Suricata [MOONDRAGON]\' was saved", toast_msg, "Test failed for suricata")
        time.sleep(1)

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()


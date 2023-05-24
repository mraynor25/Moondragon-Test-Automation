from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.xpanse_pg import XpansePage
from PageObject.discover_pg import discoverPage
import time
import unittest
# We cannot run XPANSE in the lab as there is no XPANSE available

class TestMethods_Xpanse(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    IndexName = "armoredsaint-*"
    fieldn1 = "Xpanse source IP Pivot"
    fieldname2 = "Xpanse destination IP Pivot"
    fieldname = "destination.ip"
    data = "0.0.0.0"
    fieldname3 = "destination.ip"
    KQL = "not source.ip: 0.0.0.0"
    fieldname4 = "source.ip"
    x_username = "user55@sandstone.ili.expanse.co"
    x_password = "4ndEs3wA8WFH!#F"
    KQL2 = "source.ip: 0.0.0.0"

    @classmethod
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

        hp.clickDiscover()
        time.sleep(3)

        dp = discoverPage(self.driver)
        dp.openIndex()
        time.sleep(3)
        dp.enterIndex(self.IndexName)
        time.sleep(8)
        dp.select_searched_index()
        self.driver.implicitly_wait(20)
        dp.OpenDate()
        time.sleep(1)
        dp.selectYear()
        dp.search_searchfield(self.fieldn1)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield2(self.fieldname2)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.Addfilter()
        time.sleep(2)
        dp.enterField(self.fieldname)
        time.sleep(2)
        dp.selectField2()
        time.sleep(4)
        dp.clickarrow_addfilter()
        time.sleep(3)
        dp.selectIsMenu()
        time.sleep(2)
        dp.EnterDropdown(self.data)
        time.sleep(2)
        dp.clickSave()
        time.sleep(3)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield3(self.fieldname3)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(1)
        dp.enterQuery(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.search_searchfield4(self.fieldname4)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.verify_sxip2()
        dp.verify_destip()
        get_sip = dp.get_sourceIp()
        main_page = self.driver.current_window_handle
        dp.click_sourceipLink()
        time.sleep(2)

        xp = XpansePage(self.driver)
        xp.switchToXpanse(self.x_username, self.x_password)
        xp.verify_sip(get_sip)
        self.driver.switch_to_window(main_page)

        dp.click_firstAddedFilter()
        time.sleep(2)
        dp.delete_addedFilter()
        time.sleep(3)
        dp.Addfilter()
        time.sleep(2)
        dp.clickarrowIcon()
        time.sleep(2)
        dp.enterField(self.fieldname)
        time.sleep(2)
        dp.selectField2()
        time.sleep(4)
        dp.clickarrow_addfilter()
        time.sleep(3)
        dp.selectIsNotMenu()
        time.sleep(2)
        dp.EnterDropdown(self.data)
        time.sleep(2)
        dp.clickSave()
        time.sleep(10)
        dp.verify_sxip2()
        dp.verify_dxip()
        get_dest_IP = dp.get_destip()
        dp.click_xdestiplink2()
        time.sleep(5)
        xp.switchToXpase_get_DestIP(get_dest_IP)
        time.sleep(3)

        self.driver.switch_to_window(main_page)
        dp.enterQuery_1(self.KQL2)
        dp.clickUpdateButton()
        time.sleep(8)
        dp.verify_sip()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



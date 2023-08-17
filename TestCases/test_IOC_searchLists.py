import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.ioclist_pg import IOCListPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner

# Test passed August 17 2023


class Test_search_IOCList(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    IOC_title = "AAA IOC List"
    lowercase_IOC_title = "aaa ioc list"
    no_results = "No items found"

    field_data = "source.ip"
    selectors_data = "98.175.230.2"
    field_data2 = "destination.ip"
    selectors_data2 = "68.105.28.16"
    notes = "This is a destination ip note"
    IOC_dropdown = "User"
    IOC_dropdown2 = "Expanse"
    IOC_dropdown3 = "All"

    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(7)
        print(cls.driver.title)
        time.sleep(5)

    def test_IOC_searchlist(self):


        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        time.sleep(2)
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
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.discover_pg_loads()
        dp.open_index_dropdown()
        time.sleep(1)
        dp.enter_ECSIndex(self.index)
        dp.selectECS_index()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(2)
        dp.selectYear()
        time.sleep(2)

        ip = IOCListPage(self.driver)
        ip.open_IOCList()
        time.sleep(2)
        ip.click_createIOCList()
        time.sleep(2)
        ip.load_createIOCpg()
        ip.enter_listTitle(self.IOC_title)
        time.sleep(2)
        ip.select_IOCFile()
        time.sleep(2)
        ip.click_generateList()
        time.sleep(3)
        ip.click_saveList()
        time.sleep(1)
        ip.IOCListCreated_ToastMsg()
        time.sleep(2)

        ip.enter_IOCSearchList(self.IOC_title)
        time.sleep(2)
        ip.iocList_detailButton()
        time.sleep(2)
        ip.verify_ioc_header(self.IOC_title)
        ip.close_IOC_detail()
        time.sleep(1)
        ip.verify_IOCSearchResults(self.IOC_title)
        time.sleep(1)
        ip.select_ioclistDropdown_option(self.IOC_dropdown)
        time.sleep(1)
        ip.verify_IOCSearchResults(self.IOC_title)
        time.sleep(1)
        ip.clear_search_input()
        time.sleep(1)
        ip.enter_lowercase_IOCSearchList(self.lowercase_IOC_title)
        time.sleep(1)
        ip.verify_IOCSearchResults(self.IOC_title)
        time.sleep(1)
        ip.select_ioclistDropdown_option2(self.IOC_dropdown2)
        time.sleep(1)
        ip.verify_IOCSearchNoResults(self.no_results)
        time.sleep(1)
        ip.select_ioclistDropdown_option3(self.IOC_dropdown3)
        time.sleep(1)
        ip.verify_IOCSearchResults(self.IOC_title)




    def tearDown(self):
        ip = IOCListPage(self.driver)
        ip.select_IOCName()
        time.sleep(2)
        ip.click_more()
        time.sleep(1)
        ip.remove_IOCList()
        time.sleep(2)
        ip.open_IOCList()
        time.sleep(2)
        ip.search_IOClist(self.IOC_title)
        time.sleep(1)
        ip.verify_deletedIOCList()




        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



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

# Test passed July 28 2023


class Test_IOCList(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    IOC_title = "ABC IOC list to view"
    field_data = "source.ip"
    selectors_data = "98.175.230.2"
    field_data2 = "destination.ip"
    selectors_data2 = "68.105.28.16"
    notes = "This is my destination ip notes"

    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(7)
        print(cls.driver.title)
        time.sleep(5)

    def test_IOC_list(self):


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
        time.sleep(1)
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
        time.sleep(2)
        ip.verify_toast_Msg()
        ip.click_copyFilter()
        time.sleep(2)
        ip.click_saveList()
        time.sleep(1)
        ip.IOCListCreated_ToastMsg()
        ip.close_IOCList()
        time.sleep(2)

        dp.Addfilter()
        time.sleep(2)
        dp.click_editAsQyery()
        time.sleep(3)
        dp.editAsQueryForm()
        time.sleep(3)
        dp.click_saveQuery()
        time.sleep(2)

        ip.open_IOCList()
        time.sleep(2)
        ip.IOCList_editAppendList(self.IOC_title, self.field_data, self.selectors_data, self.field_data2, self.selectors_data2, self.notes)

        dp.add_filter()
        time.sleep(2)
        dp.click_editAsQyery()
        time.sleep(3)
        dp.editAsQueryForm()
        time.sleep(3)
        dp.createCustomLabel()
        time.sleep(2)
        dp.enterCustomLabel(self.IOC_title)
        time.sleep(3)
        dp.click_saveQuery()
        time.sleep(2)


        Ip.logout()
        time.sleep(10)
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
        hp.clickDiscover()
        time.sleep(2)

        ip.open_IOCList()
        time.sleep(3)
        ip.verify_IOClist4Buttons(self.IOC_title)
        ip.click_download_IOC()
        time.sleep(2)


        Ip.logout()
        time.sleep(2)
        Ip.waituntilUsername_appear()
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(1)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(1)

        ip.open_IOCList()
        time.sleep(3)
        ip.search_IOClist(self.IOC_title)
        time.sleep(2)



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



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
# pass test July 18 2023


class Test_IOCList_UserRole(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    IOC_title = "The best IOC list top 10"
    user = "analyst2"



    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(4)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(4)
        print(cls.driver.title)
        time.sleep(5)

    def test_IOC_list(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.waituntilUsername_appear()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(3)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.open_index_dropdown()
        time.sleep(3)
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
        ip.enter_listTitle(self.IOC_title)
        time.sleep(2)
        ip.select_IOCFile()
        time.sleep(2)
        ip.add_additional_user(self.user)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ip.click_generateList()
        time.sleep(2)
        ip.verify_toast_Msg()
        ip.click_saveList()
        time.sleep(1)
        ip.IOCListCreated_ToastMsg()
        ip.close_IOCList()
        time.sleep(2)

        Ip.logout()
        time.sleep(3)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        time.sleep(4)
        Ip.clickdefault()
        time.sleep(4)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        ip.open_IOCList()
        time.sleep(3)
        ip.search_IOClist(self.IOC_title)
        time.sleep(2)
        ip.iocList_detailButton()
        time.sleep(2)
        ip.check_ioclistButton(self.IOC_title)

        Ip.logout()
        time.sleep(7)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
        Ip.clickLogin()
        time.sleep(5)
        Ip.clickdefault()
        time.sleep(3)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        ip.open_IOCList()
        time.sleep(2)

    def tearDown(self):
        ip = IOCListPage(self.driver)
        ip.search_IOClist(self.IOC_title)
        time.sleep(2)
        ip.select_IOCName()
        time.sleep(2)
        ip.click_more()
        time.sleep(1)
        ip.remove_IOCList()
        time.sleep(1)
        ip.open_IOCList()
        time.sleep(1)
        ip.search_IOClist(self.IOC_title)
        time.sleep(1)
        ip.verify_deletedIOCList()

        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



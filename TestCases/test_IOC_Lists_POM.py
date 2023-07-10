import unittest
import sys
sys.path.append("/home/monica.raynor/PycharmProjects/MoonDragon")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg1 import discoverPage
from PageObject.ioclist_pg import IOCListPage
import time
import HtmlTestRunner



class Test_IOCList(unittest.TestCase):
    username = "elastic"
    password = "98nBF5KMDCPYySNEGIaixfzi"
    username2 = "analyst2"
    password2 = "Password1!"
    IOC_title = "ABC list"
    field_data = "source.ip"
    selectors_data = "98.175.230.2"
    field_data2 = "destination.ip"
    selectors_data2 = "68.105.28.16"
    notes = "This is my destination ip notes"

    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://moondragon-kibana.ccu.cloud:9243/')
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
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.open_index_dropdown()
        time.sleep(3)
        dp.enter_ECSIndex()
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
        time.sleep(4)
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
        time.sleep(5)
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
        time.sleep(5)
        dp.createCustomLabel()
        time.sleep(2)
        dp.enterCustomLabel(self.IOC_title)
        time.sleep(3)
        dp.click_saveQuery()
        time.sleep(2)


        Ip.logout()
        time.sleep(11)
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
        time.sleep(10)
        ip.verify_IOClist4Buttons(self.IOC_title)
        ip.click_download_IOC()
        time.sleep(3)


        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
        Ip.clickLogin()
        time.sleep(7)
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)
        ip.open_IOCList()
        time.sleep(2)






    def tearDown(self):
        ip = IOCListPage(self.driver)
        ip.delete_IOClist(self.IOC_title)



        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()





if __name__ == '__main__':
    unittest.main()
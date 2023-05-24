import unittest
import time
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.arkime_pg import arkimePage

from selenium import webdriver
import HtmlTestRunner

# test failed due to arkime filename pivot does not exist in the lab may15 2023

#Feature Moon-385 Automate ability to test Arkime


class Test_arkime(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020"
    IndexName = "ecs-zeek-*"
    KQL2 = "sensor.filename : \"dd-03-230131.cap\""
    fieldname = "arkime filename pivot"
    fieldname2 = "sensor.filename"
    Query = "file == \"*dd-03-230131.cap\" && port.dst == 80 && ip.dst == 144.121.162.12"
    file_data = "/mnt/pcap/active/dd/dd-03/23/01/31/dd-03-230131.cap"
    ip_dst = "144.121.162.12"
    port_dst = "80"
    Query2 = "file == \"*dd-03-230131.cap\" && packets == 1"
    pockets = "1"
    pockets_integer = 1
    Query3 = "tags == dd && tags == dd-03"
    sen_name = "dd-03"
    ops_check = "dd"



    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        # self.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(20)
        print(cls.driver.title)
        time.sleep(5)

    def test_arkime_query(self):



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
        hp.clickDiscover()
        time.sleep(3)

        dp = discoverPage(self.driver)
        dp.openIndex()
        time.sleep(2)
        dp.enterIndex(self.IndexName)
        time.sleep(2)
        dp.selectZeek_index()
        time.sleep(7)
        dp.OpenDate()
        time.sleep(1)
        dp.selectYear()
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.enterQuery_1(self.KQL2)
        time.sleep(1)
        dp.search_searchfield(self.fieldname)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(1)
        dp.search_searchfield2(self.fieldname2)
        time.sleep(2)
        dp.add_searchResults_click_plusicon()
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(10)
        dp.clickArkime_link()
        time.sleep(6)


        ap = arkimePage(self.driver)
        ap.switchToArkime_pg()
        self.driver.implicitly_wait(10)
        ap.verifyActualFile_ToggleTag(self.file_data)
        ap.clearSearchbox()
        time.sleep(1)
        ap.enter_searchbox(self.Query)
        time.sleep(2)
        ap.click_searchButton()
        time.sleep(2)
        ap.verify_ipdst(self.ip_dst)
        ap.verify_portdst(self.port_dst)
        ap.clearSearchbox()
        time.sleep(1)
        ap.enter_searchbox2(self.Query2)
        time.sleep(2)
        ap.click_searchButton()
        time.sleep(4)
        ap.verify_packet(self.pockets)
        time.sleep(1)
        ap.verify_packets_integer(self.pockets_integer)
        ap.clearSearchbox()
        time.sleep(1)
        ap.enter_searchbox3(self.Query3)
        time.sleep(2)
        ap.click_searchButton()
        time.sleep(2)
        ap.verify_sensor(self.sen_name)
        ap.verify_ops(self.ops_check)







    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

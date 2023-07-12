from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.arkime_pg import arkimePage
import time
import unittest
import HtmlTestRunner

# test failed - development of test transfer not completed due to arkime filename pivot missing
# MD-42 test case


class TestDelete_tags(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    index = "ecs-*"
    startDateValue = "Apr 1, 2021 @ 00:00:00.000"
    endDateValue = "Jul 24, 2021 @ 15:00:00.000"
    KQL = "sensor.filename : \"Hancitor-with-Ficker-Stealer-and-Cobalt-Strike.pcap\" AND _id : \"95ypTYcBXz0Qf4-j7VVQ\""
    arkime = "arkime filename pivot"


    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(14)
        print(cls.driver.title)
        time.sleep(5)


    def test_downloadPCAP_time(self):
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
        time.sleep(3)

        dp = discoverPage(self.driver)
        dp.discover_pg_loads()
        dp.openIndex()
        time.sleep(1)
        dp.enter_ECSIndex(self.index)
        time.sleep(3)
        dp.selectECS_index()
        time.sleep(4)
        dp.if_15Min_time()
        time.sleep(2)
        dp.if_lastOneMo_time()
        time.sleep(2)
        dp.click_absolute_timefilter()
        time.sleep(2)
        dp.startDate(self.startDateValue)
        time.sleep(2)
        dp.clickNow()
        time.sleep(1)
        dp.click_absolute_timefilter()
        time.sleep(5)
        dp.endDate(self.endDateValue)
        time.sleep(10)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.enterQuery(self.KQL)
        time.sleep(1)
        dp.clickUpdateButton()
        time.sleep(4)
        dp.search_ArkimePivot(self.arkime)

        self.driver.execute_script("window.scrollBy(0, 2000)", "")
        dp.click_arkimePivot()
        time.sleep(8)

        akp = arkimePage(self.driver)
        akp.switchToArkime_pg()
        time.sleep(8)
        akp.click_dropArrow()
        time.sleep(2)
        akp.click_ExportPCAP()
        time.sleep(4)
        akp.click_plusIcon()
        time.sleep(14)
        elapsed_time = akp.verifydetect_downloadPCAP()
        self.assertLess(elapsed_time, 10, "PCAP Download time is not less than 10 second")
        print(elapsed_time)

        akp.GobackToKibana_screen()
        time.sleep(3)

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
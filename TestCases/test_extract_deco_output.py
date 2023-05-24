from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from selenium import webdriver

import time
import unittest
import HtmlTestRunner

# extract deco output failed due to content.extracted_file field does not exists! 5-8-23
# not sure of this - netflow dashboard is not exist therefore, unable to run this scripts. failed

class TestExtract_deco(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    index = "decoders-*"
    startDateValue = "Jan 14, 2019 @ 00:00:00.000"
    endDateValue = "Feb 13, 2019 @ 00:00:00.000"
    fieldname = "content.expected_file_size"
    field = "84480"
    KQL = "sensor.filename: \"fj-46a-190118.cap\" AND source.ip_rfc: \"RFC_1366\""


    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(13)
        print(cls.driver.title)
        time.sleep(5)


    def test_extract_deco_output(self):
        PCAP_data = "fj-46a-190118.cap"
        Extracted_file_data = "setcsrss.exe_895a0be4ae10ba436ad9506164a9db00"

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(8)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(3)

        dp = discoverPage(self.driver)
        dp.open_index_dropdown()
        time.sleep(3)
        dp.enter_index(self.index)
        time.sleep(1)
        dp.selectDecoder_index()
        time.sleep(2)
        dp.if_15Min_time()
        time.sleep(1)
        dp.if_lastOneMo_time()
        time.sleep(1)
        dp.click_absolute_timefilter()
        time.sleep(2)
        dp.startDate(self.startDateValue)
        time.sleep(2)
        dp.clickNow()
        time.sleep(1)
        dp.click_absolute_timefilter()
        dp.endDate(self.endDateValue)
        time.sleep(7)
        dp.clickUpdateButton()
        time.sleep(8)
        dp.Addfilter()
        time.sleep(2)
        dp.enterField(self.fieldname)
        time.sleep(4)
        dp.clickarrow_addfilter()
        time.sleep(3)
        dp.selectIsMenu()
        time.sleep(2)
        dp.enter_addfilterField(self.field)
        time.sleep(6)
        dp.clickSave()
        time.sleep(3)
        dp.enterQuery(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(8)
        PCAPData = dp.verifyPCAPdata()
        self.assertEqual(PCAP_data, PCAPData, "Search results do not match for PCAP data")
        # get_extractfile = dp.verifyExtractFile()
        # self.assertEqual(Extracted_file_data, get_extractfile, "Search results do not match for extracted file data")

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


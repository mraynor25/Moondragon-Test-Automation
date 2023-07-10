from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg1 import discoverPage
import time
import unittest
import HtmlTestRunner

# Test pass May 23 2023


class TestQuery_PCAP_content(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    index = "ecs-*"
    startDateValue = "Jun 2, 2021 @ 00:00:00.000"
    KQL1 = "network.ip_bytes: 216 AND  _id: \"ExVO-YgBA8VWYOo0KVlz\""
    datasource = "network.ip_bytes"
    fieldn1 = "_id"
    networkip_value = 216
    _id_value = "ExVO-YgBA8VWYOo0KVlz"
    decod = "decoders-*"
    value = "last"
    num = "5"
    year = "y"
    KQL = "sensor.name: \"dm-01\" AND decoder_name : \"Gh0st\""
    fieldname2 = "sensor.name"
    verify_sensor_output = "dm-01"
    fieldname3 = "decoder_name"
    verifydata_ghost = "Gh0st"
    IndexName = "ecs-suricata-*"
    KQL2 = "source.ip_public: \"false\" AND destination.ip_public: \"true\""
    fieldname4 = "source.ip_public"
    fieldname5 = "destination.ip_public"
    source_ip_pub = "false"
    destin_ip_pub = "true"
    KQL3 = "destination.ip_public: true OR source.ip_public: true"
    source_ip_pub2 = "true"
    fieldname = "sensor.filename"
    field = "/mnt/pcap/active/dm/dm-01/23/04/19/2023-04-Unit42-Wireshark-quiz.pcap"
    fieldname6 = "sensor.filename"
    sensor_filename = "/mnt/pcap/active/dm/dm-01/23/04/19/2023-04-Unit42-Wireshark-quiz.pcap"
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(14)
        print(cls.driver.title)
        time.sleep(5)


    def test_query_PCAP_content(self):
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
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.discover_pg_loads()
        time.sleep(2)
        dp.openIndex()
        time.sleep(1)
        dp.enter_ECSIndex(self.index)
        time.sleep(1)
        dp.selectECS_index()
        time.sleep(1)
        dp.loadingCheck()
        time.sleep(1)
        dp.select_timeFilter()
        dp.click_absolute_timefilter()
        time.sleep(1)
        # dp.loadingCheck()
        dp.startDate(self.startDateValue)
        time.sleep(2)
        dp.clickNow()
        time.sleep(1)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.enterKQL1(self.KQL1)
        time.sleep(1)
        dp.loadingCheck()
        dp.clickUpdateButton()
        time.sleep(3)
      #  dp.loadingCheck()
        dp.searchfield(self.datasource)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(2)

        #modified below verify_networkIP
        dp.verify_networkIP_bytes()
        time.sleep(1)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield(self.fieldn1)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(8)
        dp.verify_addedField2()
        time.sleep(1)
        dp.verify_firstValue(self.networkip_value)
        time.sleep(2)
        dp.verify_secValue(self._id_value)
        time.sleep(2)
        dp.openIndex()
        time.sleep(2)
        dp.selectDecorderIndex(self.decod)
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.dateDropdown(self.value)
        time.sleep(2)
        dp.numofyear(self.num)
        time.sleep(2)
        dp.selectYear2(self.year)
        dp.clickApply()
        dp.enterKQL(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(5)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield2(self.fieldname2)
        time.sleep(3)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.verify_sensorOutput(self.verify_sensor_output)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield3(self.fieldname3)
        time.sleep(1)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.verify_ghostData(self.verifydata_ghost)
        dp.openIndex()
        time.sleep(2)
        dp.enterIndex(self.IndexName)
        time.sleep(2)
        dp.selectSuricata_index()
        time.sleep(1)
        dp.enterKQL2(self.KQL2)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(6)
        dp.search_searchfield4(self.fieldname4)
        time.sleep(3)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.search_searchfield5(self.fieldname5)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.verify_sourceip_pub(self.source_ip_pub)
        dp.verify_dest_ip_pub(self.destin_ip_pub)
        dp.openIndexMenu()
        time.sleep(2)
        dp.enterKQL3(self.KQL3)
        time.sleep(3)
        dp.clickUpdateButton()
        time.sleep(5)
        dp.verify_sourceDestinIP_pub2(self.source_ip_pub2, self.destin_ip_pub)
        dp.Addfilter()
        time.sleep(2)
        dp.loadingCheck()
        dp.enterField(self.fieldname)
        time.sleep(2)
        dp.select_addfilter_senFilename()
        time.sleep(2)
        dp.clickarrow_addfilter()
        time.sleep(1)
        dp.loadingCheck()
        time.sleep(2)
        dp.selectIsMenu()
        time.sleep(1)
        dp.enter_addfilterField(self.field)
        time.sleep(2)
        dp.clickSave()
        time.sleep(2)
        dp.search_searchfield6(self.fieldname6)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(1)
        dp.clickUpdateButton()
        time.sleep(4)
        dp.verify_sensorFilename_col7(self.sensor_filename)


def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
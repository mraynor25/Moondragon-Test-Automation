from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
import time
import unittest
import HtmlTestRunner

#Test passed may 25 2023 applied
#test case, V.1.1 release (Consolidated Field Mapping for ecs-*)

#Moon-154 Test Case
class Test_ecs_index(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    value = "last"
    num = "5"
    year = "y"
    index_name = "ecs-zeek-*"
    fieldname = "sensor.name"
    field = "dm-01"
    datasource2 = "destination"
    datasource = "source"
   # field = "destination"
    sensor = "sensor.name"
    KQL = "sensor.filename: \"part-2-IcedID-C2-then-Cobalt-Strike-carved-and-sanitized.pcap\" AND source.ip: \"10.1.18.101\""
    sen_file = "sensor.filename"
    source = "source.ip"
    sen_name = "dm-01"
    suricata_index = "ecs-suricata"
    sen_name = "sensor.name"
    field2 = "DD-03"
    # KQL2 = "sensor.filename: \"DD-03-220119.cap\""
    sen_name_data = "dm-01"
    sen_filename = "Hancitor-with-Ficker-Stealer-and-Cobalt-Strike.pcap"
    source_data = "source"
    decoder = "decoders-*"
    KQL2 = "sensor.name: \"fj-46a\" AND sensor.filename: \"fj-46a-190131.cap\""
    sen_name_data2 = "fj-35"
    dest = "destination"
    sen_filename = "fj-35-190131.cap"
    decod = "decoders"
    source_ip = "67.22.216.121"

    @classmethod
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


    def test_ecsIndex(self):
        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(5)
        Ip.clickdefault()
        time.sleep(3)

        hp = homePage(self.driver)
        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.openIndexMenu()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.dateDropdown(self.value)
        time.sleep(2)
        dp.numofyear(self.num)
        time.sleep(2)
        dp.selectFiveYear()
        time.sleep(2)
        dp.Addfilter()
        time.sleep(2)
        dp.loadingCheck()
        dp.clickarrowIcon()
        time.sleep(2)
        dp.enterField(self.fieldname)
        time.sleep(2)
        dp.select_sensorName_addfilter()
        time.sleep(1)
        dp.clickarrow_addfilter()
        time.sleep(2)
        dp.selectIsMenu()
        time.sleep(4)
        dp.enter_addfilterField(self.field)
        time.sleep(8)
        dp.clickSave()
        time.sleep(3)
        dp.searchfield(self.datasource)
        time.sleep(4)
        dp.verifySearchResults()
        dp.clearSearchField()
        time.sleep(2)
        dp.searchfield2(self.datasource2)
        time.sleep(2)
        dp.verifydestinationQuery()
        dp.clearSearchField()
        time.sleep(2)
        dp.add_sensor(self.sensor)
        time.sleep(3)
        dp.clickPlusIcon()
        dp.verifySensorQuery()
        dp.enterQuery(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(4)
        dp.clearSearchField()
        time.sleep(2)
        dp.addSensorFilename(self.sen_file)
        time.sleep(3)
        dp.clickPlusIcon()
        time.sleep(3)
        dp.clearSearchField()
        time.sleep(2)
        dp.enterSourceIP(self.source)
        time.sleep(3)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.verifySensorName()
        dp.verifySensorfile()
        dp.verifysensorIP(self.source_ip)
        dp.openIndex()
        time.sleep(2)
        dp.indexSearchbox(self.suricata_index)
        time.sleep(2)
        dp.removeFilter()
        time.sleep(4)
        dp.Addfilter()
        time.sleep(2)
        dp.clickarrowIcon()
        time.sleep(2)
        dp.enterSensorName(self.sen_name)
        time.sleep(2)
        dp.select_sensorName_addfilter()
        dp.clickarrowIcon()
        time.sleep(3)
        dp.selectIsMenu()
        time.sleep(2)
        dp.enter_addfilterField2(self.field2)
        time.sleep(2)
        dp.clickSave()
        time.sleep(3)
        dp.verifySensorName()
        dp.enterQuery_1(self.KQL2)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(4)
        dp.Verify_sensorNameData(self.sen_name_data)
        dp.verify_senFile(self.sen_filename)
        dp.verifySource(self.source_data)
        dp.clearSearchField()
        time.sleep(2)
        dp.searchfield2(self.datasource2)
        time.sleep(2)
        dp.verifydestinationQuery()
        dp.openIndex()
        time.sleep(2)
        dp.selectDecorderIndex(self.decod)
        time.sleep(2)
        dp.removeFilter()
        time.sleep(4)
        dp.enterKQL2(self.KQL2)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.verifySenName(self.sen_name)
        dp.verifySenFile(self.sen_filename)
        dp.searchSource()
        time.sleep(2)
        dp.verifySource2(self.source_data)
        dp.clearSearchField()
        time.sleep(2)
        dp.searchfield2(self.datasource2)
        time.sleep(2)
        dp.verifySearch_Dest(self.dest)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
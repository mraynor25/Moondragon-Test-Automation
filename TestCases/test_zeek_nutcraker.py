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

# Test passed Dec 7 2023

class Test_ElasticSearchMapping(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    index = "ecs-zeek-*"
    sensor = "sensor.filename"
    fieldname = "arkime"
    fieldname2 = "nutcracker"
    valueofnutcracker = "Nutcracker Pivot"
    valueofArkime = "Arkime Filename Pivot"
    KQL = "nutcracker_pivot : * AND sensor.filename : *pcap"
    KQL2 = "nutcracker_pivot : * AND sensor.filename : *log AND not _index: \"*v1.7.8*\""
    KQL3 = "nutcracker_pivot : * AND sensor.filename : *cap AND not _index: \"*v1.7.8*\""
    # KQL4 = "not _index: \"*v1.7.7*\" and arkime_filename_pivot : * and sensor.filename : \"*json\""


    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(5)


    def test_elastic_mapping(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(2)
        Ip.clickLogin()
        time.sleep(12)
        Ip.clickdefault2()
        time.sleep(10)

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
        time.sleep(1)
        dp.selectZeek_index()
        time.sleep(2)
        dp.enterKQL(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(2)
        dp.add_sensor(self.sensor)
        time.sleep(3)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.addfilter_fieldname(self.fieldname)
        time.sleep(2)
        dp.clickPlusIcon4Arkimefield()
        time.sleep(2)
        dp.clearSearchField()
        time.sleep(2)
        dp.addfilter_fieldname2(self.fieldname2)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(1)
        dp.verify_nutcraker_value(self.valueofnutcracker)
        time.sleep(2)
        dp.verify_arkime_value(self.valueofArkime)
        time.sleep(2)


        dp.clear_KQLfield()
        time.sleep(1)
        dp.enterKQL2(self.KQL2)
        time.sleep(1)
        dp.clickUpdateButton()
        time.sleep(2)
        dp.verify_searchReturnisNot_displayed()
        time.sleep(1)
        dp.clear_KQLfield()
        time.sleep(1)
        dp.enterKQL3(self.KQL3)
        time.sleep(1)
        dp.clickUpdateButton()
        time.sleep(3)
        dp.verify_nutcraker_value(self.valueofnutcracker)
        time.sleep(2)
        dp.verify_arkime_value(self.valueofArkime)
        time.sleep(2)







    def tearDown(self):


        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.dataTags_pg import DatatagPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner


#Test Case moon-569

class Test_imbeddedTag_adddelete(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"
    tag_name = "sample ecs tag"
#     fieldname = "source.ip"
#     field = "10.4.19.138"
#     bulkTag_name = "sample bulk query"
#     bulkTag_name2 = "sample bulk"
#     bulkTag_desc = "This is my sample bulk query"
#     user = "analyst2"
#     toast_msg = """Tag
# sample bulk query
# Added Successfully"""
#     field1 = "analyst_tags"
#     KQL = "analyst_tag = sample bulk query AND analyst_tag = sample bulk"
#     analyst_tag_name = "sample bulk query, sample bulk"



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
        print(cls.driver.title)
        time.sleep(5)

    def test_imbedded_datatag(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(2)
        Ip.clickdefault()
        time.sleep(3)

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
        dp.loadingCheck()
        dp.expand_record()
        time.sleep(1)
        dp.TableTab()
        time.sleep(1)
        get_id = dp.FieldToRef_id()

        dtp = DatatagPage(self.driver)
        dtp.DataTagTab()
        time.sleep(1)
        dtp.create_imbeddedTag()
        time.sleep(1)
        dtp.verify_createHeaderExist()
        time.sleep(1)
        dtp.checkToggleOn()
        time.sleep(1)
        dtp.enter_tagName(self.tag_name)
        time.sleep(1)

        # dp.Addfilter()
        # time.sleep(2)
        # dp.enterField(self.fieldname)
        # time.sleep(1)
        # dp.selectField2()
        # time.sleep(1)
        # dp.loadingCheck()
        # dp.clickarrow_addfilter()
        # time.sleep(1)
        # dp.selectIsMenu()
        # time.sleep(1)
        # dp.loadingCheck()
        # dp.enter_addfilterField(self.field)
        # time.sleep(2)
        # dp.clickSave()
        # time.sleep(2)
        # countdoc = dp.countDocHits()
        # dp.check4DocHitsOverlimit(countdoc)
        # time.sleep(2)
        # dp.click_inspect()
        # time.sleep(1)
        # dp.click_viewInspect()
        # time.sleep(2)

        # bp = bulkQueryPage(self.driver)
        # bp.click_addBulkMenu()
        # time.sleep(1)
        # bp.wait4bulkTagPagetoLoad()
        # bp.click_createTag()
        # time.sleep(1)
        # bp.enter_tagname(self.bulkTag_name)
        # time.sleep(1)
        # bp.enter_tagDescription(self.bulkTag_desc)
        # time.sleep(1)
        # bp.enter_additionalUser(self.user)
        # time.sleep(2)
        # bp.click_submit()
        # time.sleep(1)
        # bp.verify_confirmTag(self.bulkTag_name, self.bulkTag_desc, self.user)
        # bp.click_looksgood()
        # time.sleep(2)



    def tearDown(self):




        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.dashboard_pg import dashboardPage
from PageObject.discover_pg import discoverPage
from PageObject.bulkTag_pg import bulkQueryPage
from PageObject.dataTags_pg import DatatagPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner

# test passed aug 10 2023 completed test scripts

class Test_bulkTag_adddelete(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-suricata-*"
    KQL = "sensor.name : \"dm-01\" AND source.ip : \"20.42.72.131\""
    query_name = "sensor_query"
    toast_msg = "Your query \"sensor_query\" was saved"
    bulkTag_name = "sensor tag"
    bulkTag_desc = "This is my sample bulk query"
    user = "analyst2"
    field1 = "analyst_tags"
    analyst_tag_name = "sensor tag"



    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(5)


    def test_bulkTag_additionalUser(self):

        Ip = loginPage(self.driver)
        Ip.elasticLogin()
        Ip.waituntilUsername_appear()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(2)
        Ip.clickdefault()
        time.sleep(1)

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
        time.sleep(2)
        dp.selectSuricata_index()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.selectYear()
        time.sleep(1)
        dp.loadingCheck()
        dp.enterKQL(self.KQL)
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(4)
        countdoc = dp.countDocHits()
        dp.check4DocHitsOverlimit(countdoc)

        dap = dashboardPage(self.driver)
        dap.openSaveQuery()
        time.sleep(2)
        dap.saveCurrentquery()
        time.sleep(2)
        dap.enterQueryName(self.query_name)
        time.sleep(1)
        dap.SaveQuery()
        time.sleep(1)
        dap.toastMsg2(self.toast_msg)
        time.sleep(2)

        dp.click_inspect()
        time.sleep(1)
        dp.click_viewInspect()
        time.sleep(2)

        bp = bulkQueryPage(self.driver)
        bp.click_addBulkMenu()
        time.sleep(1)
        bp.wait4bulkTagPagetoLoad()
        bp.click_createTag()
        time.sleep(1)
        bp.enter_tagname(self.bulkTag_name)
        time.sleep(1)
        bp.enter_tagDescription(self.bulkTag_desc)
        time.sleep(1)
        bp.enter_additionalUser(self.user)
        time.sleep(2)
        bp.click_submit()
        time.sleep(1)
        bp.verify_confirmTag(self.bulkTag_name, self.bulkTag_desc, self.user)
        bp.click_looksgood()
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.confirmToastMsg(self.toast_msg)
        time.sleep(2)

        bp.click_bulkAddTag()
        time.sleep(1)
        bp.waituntilAddExistingTag_popup()
        bp.enterTagName2(self.bulkTag_name)
        time.sleep(2)
        bp.click_addExistingPopup()
        time.sleep(1)
        bp.click_submit()
        time.sleep(1)
        bp.click_addTagButton()
        time.sleep(1)
        bp.verifyAddedTag2(self.bulkTag_name)
        time.sleep(1)
        bp.click_close()
        time.sleep(1)
        bp.close_inspector()

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername2(self.username2)
        time.sleep(1)
        Ip.setPassword2(self.password2)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(5)
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()

        dp.discover_pg_loads()
        dp.open_index_dropdown()
        time.sleep(1)
        dp.enter_ECSIndex(self.index)
        time.sleep(2)
        dp.selectSuricata_index()
        time.sleep(2)

        dap.openSave_query()
        time.sleep(2)
        dap.verifySavedQuery2()
        time.sleep(2)
        dp.clickUpdateButton()
        time.sleep(2)
        countdoc = dp.countDocHits()
        dp.check4DocHitsOverlimit(countdoc)

        dp.search_searchfield(self.field1)
        time.sleep(2)
        dp.clickPlusIcon()
        time.sleep(2)
        dp.click_refresh()
        time.sleep(3)

        dp.click_inspect()
        time.sleep(1)
        dp.click_viewInspect()
        time.sleep(2)

        bp.click_addBulkMenu()
        time.sleep(1)
        bp.wait4bulkTagPagetoLoad()
        bp.click_deleteTag()
        time.sleep(1)
        bp.enterTagName2(self.bulkTag_name)
        bp.click_deleteExistingPopup()
        time.sleep(1)
        bp.click_submit()
        time.sleep(2)
        bp.click_delete_Tags()
        time.sleep(2)
        bp.click_close()
        time.sleep(1)
        bp.close_inspector()
        time.sleep(1)

        dp.click_refresh()
        time.sleep(2)
        dp.verify_analystTagsNotExist(self.analyst_tag_name)
        time.sleep(2)

        dp.click_inspect()
        time.sleep(1)
        dp.click_viewInspect()
        time.sleep(2)
        bp.click_addBulkMenu()
        time.sleep(1)
        bp.wait4bulkTagPagetoLoad()
        bp.click_bulkAddTag()
        time.sleep(1)
        bp.waituntilAddExistingTag_popup()
        bp.enterTagName2(self.bulkTag_name)
        time.sleep(2)
        bp.click_addExistingPopup()
        time.sleep(1)
        bp.click_submit()
        time.sleep(1)
        bp.click_addTagButton()
        time.sleep(1)
        bp.verifyAddedTag2(self.bulkTag_name)
        time.sleep(1)
        bp.click_close()
        time.sleep(1)
        bp.close_inspector()
        time.sleep(1)

        dp.click_refresh()
        time.sleep(2)
        dp.verify_analyst_tags(self.analyst_tag_name)
        time.sleep(1)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(2)

        dtp = DatatagPage(self.driver)
        dtp.DataTagTab()
        time.sleep(1)
        dtp.searchTags_dataMgnt(self.bulkTag_name)
        time.sleep(1)
        dtp.waitSearchbutton_display()
        time.sleep(3)
        dtp.click_SearchButton()
        time.sleep(1)
        dtp.verify_tagname(self.bulkTag_name)
        time.sleep(2)
        dtp.click_settingIcon()
        time.sleep(1)
        dtp.verifyButtons4AdditionalUser()
        time.sleep(2)
        dtp.click_viewButton()
        time.sleep(1)
        dtp.verify_viewTag()
        time.sleep(1)
        dtp.close_modal()
        time.sleep(1)

        Ip.logout()
        time.sleep(7)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.waituntilUsername_appear()
        Ip.setUsername(self.username)
        time.sleep(1)
        Ip.setPassword(self.password)
        time.sleep(1)
        Ip.clickLogin()
        time.sleep(2)
        Ip.clickdefault()
        time.sleep(1)

        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickWorkspace_Menu()
        time.sleep(2)

        dtp = DatatagPage(self.driver)
        dtp.DataTagTab()
        time.sleep(2)
        dtp.searchTags_dataMgnt(self.bulkTag_name)
        time.sleep(2)
        dtp.waitSearchbutton_display()
        dtp.click_SearchButton()
        time.sleep(1)
        dtp.click_settingIcon()
        time.sleep(1)
        dtp.click_deleteButton()
        time.sleep(1)
        dtp.togglecheck_completeDelete()
        time.sleep(2)


        hp.clickHambergerMenu()
        time.sleep(1)
        hp.clickDiscover()
        time.sleep(2)

        dp.click_inspect()
        time.sleep(1)
        dp.click_viewInspect()
        time.sleep(2)

        bp = bulkQueryPage(self.driver)
        bp.click_addBulkMenu()
        time.sleep(1)
        bp.click_bulkAddTag()
        time.sleep(1)
        bp.wait4bulkTagPagetoLoad()
        bp.verify_tagNameNotExist(self.bulkTag_name)
        time.sleep(1)
        bp.click_close()
        time.sleep(1)
        bp.click_deleteTag()
        time.sleep(1)
        bp.verify_tagNameNotExist(self.bulkTag_name)
        time.sleep(1)
        bp.click_close()
        time.sleep(1)
        bp.close_inspector()
        time.sleep(1)


    def tearDown(self):
        dap = dashboardPage(self.driver)
        dap.openSaveQuery()
        time.sleep(2)
        dap.deleteIcon2()



        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



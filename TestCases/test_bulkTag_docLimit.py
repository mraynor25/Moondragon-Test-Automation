import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from PageObject.login_pg import loginPage
from PageObject.home_pg import homePage
from PageObject.discover_pg import discoverPage
from PageObject.bulkTag_pg import bulkQueryPage
from PageObject.dataTags_pg import DatatagPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import HtmlTestRunner
# Test passed oct 19 23 modified
# Test Case Moon-610 Document counts over 200,000 hit for Bulk Add Tag

class Test_bulkTag_adddelete(unittest.TestCase):
    username = "analyst"
    password = "Welcome2020!"
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "armoredsaint-*"
    value = "last"
    num = "10"
    year = "y"
    bulkTag_name = "Tag for over 20,000 doc"
    bulkTag_desc = "This is sample test tag for doc count hits over 20,000."
    msg = "Documents returned exceed 200,000. Please change the query so that less documents are returned."
    user = "analyst2"



    def setUp(cls):
        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.get('https://kibana2.moondragon.lan/')
        cls.driver.implicitly_wait(5)


    def test_bulkTag_docLimit(self):


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
        time.sleep(4)

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
        dp.selectArmoresaint_index()
        time.sleep(2)
        dp.OpenDate()
        time.sleep(1)
        dp.dateDropdown(self.value)
        time.sleep(1)
        dp.numofyear(self.num)
        time.sleep(2)
        dp.selectYear2(self.year)
        time.sleep(2)
        dp.clickApply()
        time.sleep(1)
        dp.loadingCheck()
        dp.clickUpdateButton()
        time.sleep(4)
        countdoc = dp.countDocHits()
        dp.check4DocHitsMore(countdoc)


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
        bp.click_bulkAddTag()
        time.sleep(1)
        bp.waituntilAddExistingTag_popup()
        bp.enterTagName3(self.bulkTag_name)
        time.sleep(2)
        bp.click_addExistingPopup()
        time.sleep(1)
        bp.click_submit()
        time.sleep(1)
        bp.verify_IssueAddingHeaderTag_Msg()
        bp.verify_IssueTag_Msg(self.msg)
        bp.click_close()
        time.sleep(2)
        bp.click_deleteTag()
        time.sleep(3)
        bp.enterTagName3(self.bulkTag_name)
        time.sleep(2)
        bp.click_deleteExistingPopup()
        time.sleep(1)
        bp.click_submit()
        time.sleep(1)
        bp.verify_IssueDeletingHeaderTag_Msg()
        bp.verify_IssueTag_Msg(self.msg)
        bp.click_close()
        time.sleep(2)

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
        time.sleep(5)




    def tearDown(self):



        self.driver.close()
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()



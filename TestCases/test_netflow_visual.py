from typing import List
import unittest
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragon")
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import HtmlTestRunner

#Moon-92-1 test case

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUp(cls):

        options = Options()
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--ignore-certificate-errors')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver.maximize_window()
        cls.driver.get('https://kibana.moondragon.lan/')
        cls.driver.implicitly_wait(25)
        time.sleep(3)

    def test_netflow_visualization(self):

        EnterUsername = self.driver.find_element_by_class_name("euiFieldText")
        EnterUsername.clear()
        EnterUsername.send_keys("analyst")

        EnterPassword = self.driver.find_element_by_name('password')
        EnterPassword.clear()
        EnterPassword.send_keys("Welcome2020!")

        PressLogin = self.driver.find_elements_by_xpath("//span[contains(text(),'Log in')]")
        PressLogin[0].click()
        time.sleep(2)

        if len(self.driver.find_elements_by_xpath("//a[contains(text(),'Default')]")) > 0:
            clickDefault = self.driver.find_elements_by_xpath("//a[contains(text(),'Default')]")
            clickDefault[0].click()
            time.sleep(3)

        Homebutton = self.driver.find_elements_by_xpath("//div[@id='globalHeaderBars']/div[2]/div[1]/div[1]/button[1]")[0].click()
        time.sleep(1)

        ClickDashboard = self.driver.find_elements_by_xpath("//span[contains(text(),'Dashboard')]")
        ClickDashboard[0].click()

        SearchDashboard = self.driver.find_elements_by_xpath("//input[contains(@class, '-fullWidth euiFieldSearch-isClearable')]")
        SearchDashboard[0].send_keys("netflow")
        time.sleep(1)

        HTTPLink = self.driver.find_elements_by_xpath("//a[contains(text(),'Netflow')]")
        HTTPLink[0].click()
        time.sleep(2)

        # OpenDate2 = self.driver.find_elements_by_xpath("//*[@id='QuickSelectPopover']/div[1]/button[1]/span[1]/*[1]")
        # OpenDate2[0].click()
        # time.sleep(2)
        #
        # SelectYear = self.driver.find_elements_by_xpath("//button[contains(text(),'Last 1 year')]")
        # SelectYear[0].click()
        # time.sleep(2)

        enterKQL = self.driver.find_elements_by_xpath("//div[contains(@class, 'kbnQueryBar__textareaWrap')]/textarea")
        if enterKQL[0].text != "sensor.name : * AND source.port: 443":
            enterKQL[0].send_keys(Keys.CONTROL + "a")
            enterKQL[0].send_keys(Keys.DELETE)
            KQL = "sensor.name : * AND source.port: 443"
            enterKQL[0].send_keys(KQL)
            time.sleep(2)

        # first_filter = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]")[0].text
        if len(self.driver.find_elements_by_xpath("//*/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]")) > 0:
            Remove_filter1 = self.driver.find_elements_by_xpath("//*/div[1]/span[1]/span[1]/button[2]/*[1]")
            Remove_filter1[0].click()
            time.sleep(2)

        if len(self.driver.find_elements_by_xpath("//*/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]")) > 0:
            Remove_filter1 = self.driver.find_elements_by_xpath("//*/div[1]/span[1]/span[1]/button[2]/*[1]")
            Remove_filter1[0].click()
            time.sleep(15)

        if len(self.driver.find_elements_by_xpath("//*/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]")) > 0:
            Remove_filter1 = self.driver.find_elements_by_xpath("//*/div[1]/span[1]/span[1]/button[2]/*[1]")
            Remove_filter1[0].click()
            time.sleep(2)

        clickAddFilter = self.driver.find_element_by_xpath( "//*/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]")
        clickAddFilter.click()
        time.sleep(2)

        clickArrow_dropdown = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
        clickArrow_dropdown[0].click()
        time.sleep(2)

        TypeField = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        TypeField[0].send_keys("destination.ip.keyword")
        time.sleep(2)
        pressEnter_option = self.driver.find_elements_by_class_name('euiComboBoxOption__content')
        pressEnter_option[0].click()
        time.sleep(2)
        arrow = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
        arrow[0].click()
        time.sleep(1)
        select_is = self.driver.find_elements_by_xpath("//span[@class='euiComboBoxOption__content']")
        select_is[0].click()
        time.sleep(1)

        enter_valueFilter = self.driver.find_elements_by_xpath("//*/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        enter_valueFilter[0].send_keys("65.254.219.206")
        time.sleep(2)
        clickSave = self.driver.find_elements_by_xpath("//span[contains(text(),'Save')]")
        clickSave[0].click()
        time.sleep(2)

        click_update = self.driver.find_elements_by_xpath("//span[contains(text(),'Update')]")
        click_update[0].click()
        time.sleep(4)

        dest_ip_value = "65.254.219.206"
        dest_ip = self.driver.find_elements_by_xpath("//tbody[1]/tr/td[1]/div[2]/div[1]/div[1]")
        for desip in dest_ip:
            self.assertEqual(desip.text, dest_ip_value, "Test failed, Destination IP value is not returned correctly")

        source_port_value = "443"
        source_port = self.driver.find_elements_by_xpath("//tbody[1]/tr/td[2]/div[2]/div[1]/div[1]")
        for sourcePort in source_port:
            self.assertEqual(sourcePort.text, source_port_value, "Test failed, source port is not matched in the table")

        # clickAddFilter = self.driver.find_element_by_xpath("//*/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]")
        # clickAddFilter.click()
        # time.sleep(3)
        #
        # clickArrow_dropdown = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
        # clickArrow_dropdown[0].click()
        # time.sleep(3)
        #
        # TypeField = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        # TypeField[0].send_keys("destination.port")
        # time.sleep(2)
        # pressEnter_option = self.driver.find_elements_by_class_name('euiComboBoxOption__content')
        # pressEnter_option[0].click()
        # time.sleep(2)
        # arrow = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
        # arrow[0].click()
        # time.sleep(1)
        # select_is = self.driver.find_elements_by_xpath("//span[@class='euiComboBoxOption__content']")
        # select_is[0].click()
        # time.sleep(3)
        #
        # enter_valueFilter2 = self.driver.find_elements_by_xpath("//*/div[6]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
        # enter_valueFilter2[0].send_keys("32,619")
        # time.sleep(2)
        # clickSave = self.driver.find_elements_by_xpath("//span[contains(text(),'Save')]")
        # clickSave[0].click()
        # time.sleep(2)

            # clickOperatorArrow = self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]/*[1]")
            # clickOperatorArrow[0].click()
            # time.sleep(2)
            #
            # SelectOperator = self.driver.find_elements_by_xpath("//*/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]")
            # SelectOperator[0].click()
            # time.sleep(15)

       # if len(self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/span[1]/span[1]/button[1]/span[1]")) > 0:




    def tearDown(cls):


        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



#if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))






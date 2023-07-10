from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
sys.path.append("C:/Users/mraynor/PycharmProjects/MoonDragonTest")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
    username2 = "analyst2"
    password2 = "Welcome2020!"
    index = "ecs-*"

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


    def test_IOC_list(self):
        IOC_title = "ABC list"
        field_data = "source.ip"
        selectors_data = "98.175.230.2"

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
        time.sleep(2)

        dp = discoverPage(self.driver)
        dp.open_index_dropdown()
        time.sleep(2)
        dp.enter_ECSIndex(self.index)
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//*/span[1]/span[1]/span[1]/mark[1]").click()
        time.sleep(2)

        # Open Date
        OpenDate2 = self.driver.find_elements(By.XPATH, "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]")
        OpenDate2[0].click()
        time.sleep(1)

        SelectYear = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Last 1 year')]")
        SelectYear[0].click()
        time.sleep(2)

        IOClist = self.driver.find_elements(By.XPATH, "//span[text()='IOC Lists']")
        IOClist[0].click()
        time.sleep(2)

        create_IOCList = self.driver.find_elements(By.XPATH, "//span[text()='Create IOC List']")
        create_IOCList[0].click()
        time.sleep(2)

        enter_list_title = self.driver.find_elements(By.XPATH, "//input[@aria-label='Use aria labels when no actual label is in use']")
        enter_list_title[0].send_keys(IOC_title)

        select_file = self.driver.find_elements(By.XPATH, "//input[@class='euiFilePicker__input']")
        select_file[0].send_keys("C:/Users/mraynor/TestData/ip list.csv")
        #"C:/Users/mraynor/TestData/ip list"
        time.sleep(4)

        click_generate_list = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Generate')]")
        click_generate_list[0].click()
        time.sleep(2)

        toastMsg = self.driver.find_elements(By.XPATH, "//div[@data-test-subj='globalToastList']")[0].text

        if toastMsg == "List Not Saved: List name already exists, try another name":
            assert False

        click_copyFilter = self.driver.find_elements(By.XPATH, "//span[text()='Copy Filter']")
        click_copyFilter[0].click()
        time.sleep(2)

        click_saveList = self.driver.find_elements(By.XPATH, "//*/div[3]/div[1]/div[1]/div[5]/div[1]/div[1]/button[1]")
        click_saveList[0].click()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@data-test-subj='globalToastList']"), "IOC List Created Successfully"))

        close_ioclist = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='euiFlyoutCloseButton']")
        close_ioclist[0].click()
        time.sleep(2)

        # add filter xpath

        click_addFilter = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='addFilter']/span[1]/span[1]")
        click_addFilter[0].click()
        time.sleep(2)

        click_editasQuery = self.driver.find_elements(By.XPATH, "//span[text()='Edit as Query DSL']")
        click_editasQuery[0].click()
        time.sleep(3)

        editasQuery_form = self.driver.find_elements(By.XPATH, "//textarea[@aria-label='Editor content;Press Alt+F1 for Accessibility Options.']")

        editasQuery_form[0].send_keys(Keys.CONTROL, 'a')
        editasQuery_form[0].send_keys(Keys.DELETE)
        editasQuery_form[0].send_keys(Keys.CONTROL, 'v')
        time.sleep(5)

        save_Query = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='saveFilter']/span[1]/span[1]")
        save_Query[0].click()
        time.sleep(2)

        IOClist = self.driver.find_elements(By.XPATH, "//span[text()='IOC Lists']")
        IOClist[0].click()
        time.sleep(2)

        IOClistName = len(self.driver.find_elements(By.XPATH, "//*/tr/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]"))
        # print(IOClistName[0].text)

        for iln in range(1, IOClistName + 1):
            IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
            if IOCName == IOC_title:
                dailyIOC = self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln) + "]/td[2]/div[2]/button[1]")[0].click()
                time.sleep(1)
                more = self.driver.find_elements(By.XPATH, "//button[@aria-label='More']")[0].click()
                time.sleep(2)
                EditList = self.driver.find_elements(By.XPATH, "//span[text()='Edit List']")
                EditList[0].click()
                time.sleep(2)
                add_sectors = self.driver.find_elements(By.XPATH, "//span[text()='Add selectors']")
                add_sectors[0].click()
                time.sleep(2)
                field_textbox = self.driver.find_elements(By.XPATH, "//*/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
                field_textbox[0].send_keys(field_data)
                time.sleep(2)
                enter_selectors = self.driver.find_elements(By.XPATH, "//*/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
                enter_selectors[0].send_keys(selectors_data)
                time.sleep(3)
                save_selectors = self.driver.find_elements(By.XPATH, "//span[text()='Save Selectors']")
                save_selectors[0].click()
                time.sleep(2)
                save_main = self.driver.find_elements(By.XPATH, "//*/div[1]/div[1]/div[3]/div[4]/button[1]/span[1]/span[1]")
                save_main[0].click()
                time.sleep(2)
                save_list = self.driver.find_elements(By.XPATH, "//span[text()='Save List']")
                save_list[0].click()
                wait = WebDriverWait(self.driver, 10)
                wait.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//div[@data-test-subj='globalToastList']"), "List Saved"))
                exit_button = self.driver.find_elements(By.XPATH, "//div[@aria-labelledby='ABC list']/button[1]")
                exit_button[0].click()
                time.sleep(2)
                copy_clipboard = self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln) + "]/td[3]/div[2]/button[1] ")
                copy_clipboard[0].click()
                time.sleep(3)
                close_ioclist = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='euiFlyoutCloseButton']")
                close_ioclist[0].click()
                time.sleep(3)
                break

        click_addFilter = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='addFilter']/span[1]/span[1]")
        click_addFilter[0].click()
        time.sleep(2)

        click_editasQuery = self.driver.find_elements(By.XPATH, "//span[text()='Edit as Query DSL']")
        click_editasQuery[0].click()
        time.sleep(3)

        editasQuery_form = self.driver.find_elements(By.XPATH, "//textarea[@aria-label='Editor content;Press Alt+F1 for Accessibility Options.']")

        editasQuery_form[0].send_keys(Keys.CONTROL, 'a')
        editasQuery_form[0].send_keys(Keys.DELETE)
        editasQuery_form[0].send_keys(Keys.CONTROL, 'v')
        time.sleep(5)

        create_custom_label = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='createCustomLabel']")
        create_custom_label[0].click()
        time.sleep(2)

        enter_custom_label = self.driver.find_elements(By.XPATH, "//*/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/input[1]")
        enter_custom_label[0].send_keys("abc listing")
        time.sleep(3)

        save_Query = self.driver.find_elements(By.XPATH, "//button[@data-test-subj='saveFilter']/span[1]/span[1]")
        save_Query[0].click()
        time.sleep(2)

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername2(self.username2)
        Ip.setPassword2(self.password2)
        Ip.clickLogin()
        time.sleep(7)
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        IOClist = self.driver.find_elements(By.XPATH, "//span[text()='IOC Lists']")
        IOClist[0].click()
        time.sleep(10)

        IOClistName2 = len(
            self.driver.find_elements(By.XPATH, "//*/tr/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]"))

        for iln2 in range(1, IOClistName2 + 1):
            IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln2) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
            if IOCName == IOC_title:
                dailyIOC = \
                self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln2) + "]/td[2]/div[2]/button[1]")[0].click()
                time.sleep(1)
                more = self.driver.find_elements(By.XPATH, "//button[@aria-label='More']")[0].click()
                time.sleep(5)
                if len(self.driver.find_elements(By.XPATH, "//span[text()='Delete List']")) > 0:
                    assert False
                if len(self.driver.find_elements(By.XPATH, "//span[text()='Download List']")) > 0:
                    assert True
                if len(self.driver.find_elements(By.XPATH, "//span[text()='Edit List']")) > 0:
                    assert False

        Ip.logout()
        time.sleep(11)
        Ip.elasticLogin()
        time.sleep(1)
        Ip.setUsername(self.username)
        Ip.setPassword(self.password)
        Ip.clickLogin()
        time.sleep(7)
        Ip.clickdefault()
        time.sleep(5)

        hp.clickHambergerMenu()
        time.sleep(2)
        hp.clickDiscover()
        time.sleep(2)

        IOClist = self.driver.find_elements(By.XPATH, "//span[text()='IOC Lists']")
        IOClist[0].click()
        time.sleep(2)


def tearDown(self):
    IOC_title = "ABC list"
    IOClistName = len(self.driver.find_elements(By.XPATH, "//*/tr/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]"))

    for iln in range(1, IOClistName + 1):
        IOCName = self.driver.find_elements(By.XPATH, "//*/tr[" + str(iln) + "]/td[1]/div[2]/span[1]/span[1]/span[1]/li[1]/span[1]/span[1]")[0].text
        if IOCName == IOC_title:
            dailyIOC = \
            self.driver.find_elements(By.XPATH, "//table[1]/tbody[1]/tr[" + str(iln) + "]/td[2]/div[2]/button[1]")[0].click()
            time.sleep(1)
            more = self.driver.find_elements(By.XPATH, "//button[@aria-label='More']")[0].click()
            time.sleep(2)
            delete_list = self.driver.find_elements(By.XPATH, "//span[text()='Delete List']")
            delete_list[0].click()
            time.sleep(2)
            delete_list_popup = self.driver.find_elements(By.XPATH,
                                                          "//*/div[3]/div[1]/div[1]/div[3]/button[2]/span[1]/span[1]")
            delete_list_popup[0].click()
            wait = WebDriverWait(self.driver, 6)
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@data-test-subj='globalToastList']"), "IOC List deleted successfully"))
            IOC_delete_toastMsg = self.driver.find_elements(By.XPATH, "//div[@data-test-subj='globalToastList']")[0].text
            assert IOC_delete_toastMsg == "IOC List deleted successfully"

    self.driver.close()
    self.driver.quit()




if __name__ == '__main__':
    unittest.main()
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class dataViewPage():
    # Locators of all the elements
    enterTextbox_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    tablecol_xpath = "//tbody/tr/td[1]/div[2]"
    homebutton2_xpath = "//div[@id='globalHeaderBars']/div[2]/div[1]/div[1]/button[1]"
    createDataView_xpath = "//span[contains(text(),'Create data view')]"
    enterNameField_xpath = "//input[contains(@class, 'euiFieldText--fullWidth')]"
    toastMsg_fav_xpath = "//span[contains(text(),Saved 'fav*')]"



    def __init__(self,driver):
        self.driver = driver

    def enterSearchField(self, search_val):
        Enter_textbox = self.driver.find_elements(By.XPATH, self.enterTextbox_xpath)
        Enter_textbox[0].send_keys(search_val)
        time.sleep(3)


    def search_favExist(self):
        table_col = len(self.driver.find_elements(By.XPATH, self.tablecol_xpath))

        favexists = False
        for col in range(1, table_col + 1):
            value = self.driver.find_elements(By.XPATH, "//tbody/tr[" + str(col) + "]/td[1]/div[2]")[0].text
            # print(value, end='  ')

            findFav = "favorited-dashboards*"
            if findFav == value:
                # print("fav is available")
                favexists = True
                break

        if favexists:
            Homebutton2 = self.driver.find_elements(By.XPATH, self.homebutton2_xpath)[0].click()
            time.sleep(3)
        else:
            createDataView = self.driver.find_elements(By.XPATH, self.createDataView_xpath)
            createDataView[0].click()
            time.sleep(3)
            enterName = self.driver.find_elements(By.XPATH, self.enterNameField_xpath)
            enterName[0].send_keys("v")
            enterName[0].send_keys(Keys.ARROW_LEFT)
            enterName[0].send_keys("fa")
            time.sleep(2)
            clickCreateDataView = self.driver.find_elements(By.XPATH, self.createDataView_xpath)
            clickCreateDataView[0].click()
            time.sleep(2)
            toastMessage_fav = self.driver.find_elements(By.XPATH, self.toastMsg_fav_xpath)[0].text
            assert toastMessage_fav == "Saved fav*"

            time.sleep(2)
            Homebutton = self.driver.find_elements(By.XPATH, self.homebutton2_xpath)[0].click()










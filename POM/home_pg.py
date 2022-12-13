
class homePage():
    # Locators of all the elements
    button_homeMenu_xpath = "//div[@id='globalHeaderBars']/div[2]/div[1]/div[1]/button[1]"
    button_dashboardMenu_xpath = "//span[contains(text(),'Dashboard')]"
    click_detectionMenu_xpath = "//span[contains(text(),'Detections')]"
    click_discoverMenu_xpath = "//span[contains(text(),'Discover')]"


    def __init__(self,driver):
        self.driver = driver

    def clickMainMenu(self):
        homebutton2 = self.driver.find_elements_by_xpath(self.button_homeMenu_xpath)[0].click()

    def clickDashMenu(self):
        ClickDashboard = self.driver.find_elements_by_xpath(self.button_dashboardMenu_xpath)
        ClickDashboard[0].click()

    def ScrolltoDetections(self):
        flag = self.driver.find_elements_by_xpath(self.click_detectionMenu_xpath)
        flag[0].location_once_scrolled_into_view

    def clickDetections(self):
        ClickDetect2 = self.driver.find_elements_by_xpath(self.click_detectionMenu_xpath)
        ClickDetect2[0].click()

    def clickDiscover(self):
        ClickDiscover = self.driver.find_elements_by_xpath(self.click_discoverMenu_xpath)
        ClickDiscover[0].click()


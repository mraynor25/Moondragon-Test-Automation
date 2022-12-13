
class dashboardMainPage():
    # Locators of all the elements

    textbox_searchDashboard_xpath = "//input[contains(@class, '-fullWidth euiFieldSearch-isClearable')]"
    link_result_suricata_xpath = "//a[contains(text(),'Suricata [MOONDRAGON]')]"
    Welcomelink_linktext = "*Welcome [MOONDRAGON]"

    def __init__(self, driver):
        self.driver = driver


    def searchDash(self, dashboard):
        SearchDashboard = self.driver.find_elements_by_xpath(self.textbox_searchDashboard_xpath)
        SearchDashboard[0].send_keys(dashboard)


    def clickSearchResult(self):
        Welcome = self.driver.find_elements_by_xpath(self.link_result_suricata_xpath)
        Welcome[0].click()

    def clickWelcomelink(self):
        Welcomepage = self.driver.find_elements_by_link_text(self.Welcomelink_linktext)
        Welcomepage[0].click()



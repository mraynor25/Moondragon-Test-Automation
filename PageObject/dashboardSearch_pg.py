import time
from selenium.webdriver.common.by import By

class dashboardSearchPage():
    # Locators of all the elements

    searchbox_dashboard_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    link_suricata_xpath = "//a[contains(text(),'Suricata [MOONDRAGON]')]"
    welcomeDashLinktext = "*Welcome [MOONDRAGON]"
    httpLinkXpath = "//a[contains(text(),'HTTP [MOONDRAGON]')]"
    SMBLinkXpath = "//a[contains(text(),'SMB [Moondragon]')]"
    SMTPLinkText = "SMTP [MOONDRAGON]"
    FTPlinkLinkText = "FTP [MOONDRAGON]"


    def __init__(self, driver):
        self.driver = driver

    def enterSearchDashboard(self, dashboard_name):
        SearchDashboard = self.driver.find_elements(By.XPATH, self.searchbox_dashboard_xpath)
        SearchDashboard[0].send_keys(dashboard_name)
        time.sleep(1)

    def click_netflowLink(self):
        NetflowLink = self.driver.find_elements(By.XPATH, "//a[text()='Netflow']")
        NetflowLink[0].click()


    def click_filesLink(self):
        FilesLink = self.driver.find_elements(By.LINK_TEXT, "Files [MOONDRAGON]")
        FilesLink[0].click()


    def clickSuricatalink(self):
        SuricataLink = self.driver.find_elements(By.XPATH, self.link_suricata_xpath)
        SuricataLink[0].click()
        time.sleep(2)

    def clickdecoderlink(self):
        DecoderLink = self.driver.find_elements(By.LINK_TEXT, "Decoder")
        DecoderLink[0].click()
        time.sleep(2)

    def clickHTTPlink(self):
        HTTPLink = self.driver.find_elements(By.XPATH, self.httpLinkXpath)
        HTTPLink[0].click()

    def welcomeDashboard(self):
        Welcomepage = self.driver.find_elements(By.LINK_TEXT, self.welcomeDashLinktext)
        Welcomepage[0].click()

    def enterSearchDashboard2(self, dashboard_name2):
        SearchDashboard = self.driver.find_elements(By.XPATH, self.searchbox_dashboard_xpath)
        SearchDashboard[0].send_keys(dashboard_name2)


    def enterSearchDashboard3(self, dashboard_name3):
        SearchDashboard = self.driver.find_elements(By.XPATH, self.searchbox_dashboard_xpath)
        SearchDashboard[0].send_keys(dashboard_name3)


    def clickSMBlink(self):
        clickSMB = self.driver.find_elements(By.XPATH, self.SMBLinkXpath)
        clickSMB[0].click()

    def clicksmtplink(self):
        smtpLink = self.driver.find_elements(By.LINK_TEXT, self.SMTPLinkText)
        smtpLink[0].click()

    def clickFTPlink(self):
        ftp_link = self.driver.find_elements(By.LINK_TEXT, self.FTPlinkLinkText)
        ftp_link[0].click()


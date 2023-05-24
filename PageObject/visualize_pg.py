import time
from selenium.webdriver.common.by import By




class visualizePage():
    # Locators of all the elements
    selectPie_Xpath = "//div[@data-test-subj='lnsSuggestion-asDonut']/button[1]"
    plusiconToDrop_Xpath = "//span[contains(text(),'Add or drag-and-drop a field')]"
    enterField_Xpath = "//input[@data-test-subj='comboBoxSearchInput']"
    selectVersion_Xpath = "//mark[@class='euiMark']"
    saveButton_Xpath = "//span[contains(text(),'Save')]"
    saveLenVis_Xpath = "//div[contains(text(),'Save Lens visualization')]"
    enterTitle_Xpath = "//input[@class='euiFieldText euiFieldText--fullWidth']"
    textbox_dash_Xpath = "//*/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    select_suricata_Xpath = "//mark[contains(text(),'Suricata [MOONDRAGON]')"
    select_suricata_xpath = "//*/button[1]/span[1]/span[1]/span[1]/span[1]"
    saveTogotoDash_Xpath = "//span[contains(text(),'Save and go to Dashboard')]"


    def __init__(self,driver):
        self.driver = driver

    def selectPieChart(self):
        choosePie = self.driver.find_elements(By.XPATH, self.selectPie_Xpath)
        choosePie[0].location_once_scrolled_into_view
        time.sleep(3)
        choosePie[0].click()

    def clickPlusIconTodrop(self):
        PlusicontoDrop = self.driver.find_elements(By.XPATH, self.plusiconToDrop_Xpath)
        PlusicontoDrop[0].click()


    def enterFieldtoVisual(self, field):
        enterField = self.driver.find_elements(By.XPATH, self.enterField_Xpath)
        enterField[0].send_keys(field)

    def clickSelectVersion(self):
        selectVersion = self.driver.find_elements(By.XPATH, self.selectVersion_Xpath)
        selectVersion[0].click()

    def clickSave(self):
        SaveButton = self.driver.find_elements(By.XPATH, self.saveButton_Xpath)
        SaveButton[0].click()

    def get_saveLenVis(self):
        saveLensVis = self.driver.find_elements(By.XPATH, self.saveLenVis_Xpath)[0].text
        return saveLensVis

    def enter_visual_title(self, title):
        enterTitle = self.driver.find_elements(By.XPATH, self.enterTitle_Xpath)
        enterTitle[0].send_keys(title)


    def textboxDash(self, dashboard_name):
        textbox_dash = self.driver.find_elements(By.XPATH, self.textbox_dash_Xpath )
        textbox_dash[0].send_keys(dashboard_name)

    def select_suricata(self):
        select_option_suricata = self.driver.find_elements(By.XPATH, self.select_suricata_xpath)
        select_option_suricata[0].click()

    def saveTogoDashboard(self):
        clickSave = self.driver.find_elements(By.XPATH, self.saveTogotoDash_Xpath)
        clickSave[0].click()



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class homePage():
    # Locators of all the elements
    link_homebutton_xpath = "//button[@data-test-subj='toggleNavButton']"
    link_discoverMenu_xpath = "//span[contains(text(),'Discover')]"
    link_dashboardMenu_xpath = "//span[contains(text(),'Dashboard')]"
    menu_security_xpath = "//a[contains(text(),'Security')]"
    menu_stackMgnt_xpath = "//span[contains(text(),'Stack Management')]"
    menu_visualizeLibery_xpath = "//*[@id='savedQueryPopover']/div[1]/button[1]/span[1]/span[1]/*[2]"
    open_workspaceMenu_xpath = "//*[contains(@class, 'euiAccordion__iconButton-isOpen')]"
    workspaceMenu_xpath = "//*/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]"
    Expand_workspaceMenu_xpath = "//*/div[3]/nav[1]/div[4]/div[1]/div[1]/button[2]"
    workspace_linkXpath = "//h3[contains(@class, 'euiCollapsibleNavGroup__title')"
    dataView_xpath = "//span[contains(text(),'Data Views')]"
    rulesMenu_xpath = "//span[contains(text(),'Rules')]"
    dashboardMenu_xpath = "//button[contains(text(),'Dashboard')]"


    def __init__(self,driver):
        self.driver = driver

    def clickHambergerMenu(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, self.link_homebutton_xpath))
                   )
        Homebutton = self.driver.find_elements(By.XPATH, self.link_homebutton_xpath)
        Homebutton[0].click()


    def clickDiscover(self):
        ClickDiscover = self.driver.find_elements(By.XPATH, self.link_discoverMenu_xpath)
        ClickDiscover[0].click()

    def clickDashboard(self):
        ClickDashboard = self.driver.find_elements(By.XPATH, self.link_dashboardMenu_xpath)
        ClickDashboard[0].click()

    def clickDashboardMenu(self):
        dashboard_menu = self.driver.find_elements(By.XPATH, self.dashboardMenu_xpath)
        dashboard_menu[0].click()


    def clickSecurityMenu(self):
        security = self.driver.find_elements(By.XPATH, self.menu_security_xpath)
        security[0].click()




    def clickStackMgntMenu(self):
        NavToManagement = self.driver.find_elements(By.XPATH, self.menu_stackMgnt_xpath)
        NavToManagement[0].location_once_scrolled_into_view
        NavToManagement[0].click()


    def VisualizeLiburyMenu(self):
        OpenSaveIcon = self.driver.find_elements(By.XPATH, self.menu_visualizeLibery_xpath)
        OpenSaveIcon[0].click()



    def clickWorkspace_Menu(self):
        if len(self.driver.find_elements(By.XPATH, self.open_workspaceMenu_xpath)) > 0:
            clickWorkspace = self.driver.find_elements(By.XPATH, self.workspaceMenu_xpath)
            clickWorkspace[0].click()
        else:
            self.driver.find_elements(By.XPATH, self.Expand_workspaceMenu_xpath)[0].click()
            Workspacelink = self.driver.find_elements(By.XPATH, self.workspace_linkXpath)
            Workspacelink[0].click()

    def clickDataView(self):
        NavToDataView = self.driver.find_elements(By.XPATH, self.dataView_xpath)
        NavToDataView[0].location_once_scrolled_into_view
        time.sleep(2)
        NavToDataView[0].click()

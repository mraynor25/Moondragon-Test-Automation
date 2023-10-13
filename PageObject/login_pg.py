import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class loginPage():
    # Locators of all the elements
    link_elasticSearch_xpath = "//p[contains(text(),'Log in with Elasticsearch')]"
    textbox_username_className = "euiFieldText"
    textbox_username_name = "username"
    textbox_username_xpath = "//input[@data-test-subj='loginUsername']"
    textbox_password_name = "password"
    textbox_password_name2_xpath = "//input[@data-test-subj='loginPassword']"
    button_login_xpath = "//span[contains(text(),'Log in')]"
    WelcomeText_xpath = "//h1[contains(text(),'Welcome to Elastic')]"
    LogoutMsg_xpath = "//span[contains(text(),'logged out of Elastic.')]"
    defaultlink_xpath = "//a[contains(text(),'Default')]"
    logoutMenuXpath = "//div[contains(@class, 'euiAvatar')]/span[1]"
    logoutXpath = "//span[contains(text(),'Log out')]"


    def __init__(self,driver):
        self.driver = driver



    def elasticLogin(self):
        if len(self.driver.find_elements(By.XPATH, self.link_elasticSearch_xpath)) > 0:
            click_Elastic_login = self.driver.find_elements(By.XPATH, self.link_elasticSearch_xpath)
            click_Elastic_login[0].click()

    def setUsername(self, username):
        if len(self.driver.find_elements(By.CLASS_NAME, self.textbox_username_className)) > 0:
            EnterUsername2 = self.driver.find_element(By.CLASS_NAME, self.textbox_username_className)
            if EnterUsername2.is_displayed():
                EnterUsername2.clear()
                EnterUsername2.send_keys(username)


    def setPassword(self, password):
        if len(self.driver.find_elements(By.NAME, self.textbox_password_name)) > 0:
            EnterPassword = self.driver.find_element(By.NAME, self.textbox_password_name)
            EnterPassword.clear()
            EnterPassword.send_keys(password)

    def clickLogin(self):
        if len(self.driver.find_elements(By.XPATH, self.button_login_xpath)) > 0:
            PressLogin = self.driver.find_elements(By.XPATH, self.button_login_xpath)
            PressLogin[0].click()

    def clickdefault(self):
        # if len(self.driver.find_elements(By.XPATH, self.defaultlink_xpath)) > 0:
        clickDefault = self.driver.find_elements(By.XPATH, self.defaultlink_xpath)
        clickDefault[0].click()

    def clickdefault2(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.XPATH, self.defaultlink_xpath))
                   )
        clickDefault = self.driver.find_elements(By.XPATH, self.defaultlink_xpath)
        clickDefault[0].click()


    def GetWelcomeText(self):
        Welcometext2 = self.driver.find_elements_by_xpath(self.WelcomeText_xpath)
        return (Welcometext2)


    def VerifyLogoutText(self):
        GetLogoutMsg = self.driver.find_elements_by_xpath(self.LogoutMsg_xpath)[0].text
        return (GetLogoutMsg)

    def waituntilUsername_appear(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath))
                   )


    def setUsername2(self, username2):
        if len(self.driver.find_elements(By.XPATH, self.textbox_username_xpath)) > 0:
            EnterUsername2 = self.driver.find_elements(By.XPATH, self.textbox_username_xpath)
            EnterUsername2[0].clear()
            EnterUsername2[0].send_keys(username2)


    def setPassword2(self, password2):
        if len(self.driver.find_elements(By.XPATH, self.textbox_password_name2_xpath)) > 0:
            EnterPassword2 = self.driver.find_element(By.XPATH, self.textbox_password_name2_xpath)
            EnterPassword2.clear()
            EnterPassword2.send_keys(password2)




    def logout(self):
        Logoutmenu = self.driver.find_elements(By.XPATH, self.logoutMenuXpath)
        Logoutmenu[0].click()
        time.sleep(2)
        Logoutlink = self.driver.find_elements(By.XPATH, self.logoutXpath)
        Logoutlink[0].click()

    def logout4user(self):
        Logoutmenu = self.driver.find_elements(By.XPATH, self.logoutMenuXpath)
        Logoutmenu[0].click()
        time.sleep(1)
        Logoutlink = self.driver.find_elements(By.XPATH, self.logoutXpath)
        Logoutlink[0].click()


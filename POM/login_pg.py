
class loginPage():
    # Locators of all the elements
    textbox_username_className = "euiFieldText"
    textbox_password_name = "password"
    button_login_xpath = "//span[contains(text(),'Log in')]"
    WelcomeText_xpath = "//h1[contains(text(),'Welcome to Elastic')]"
    LogoutMsg_xpath = "//span[contains(text(),'logged out of Elastic.')]"

    def __init__(self,driver):
        self.driver = driver


    def setUsername(self, username):
        EnterUsername2 = self.driver.find_element_by_class_name(self.textbox_username_className)
        EnterUsername2.clear()
        EnterUsername2.send_keys(username)

    def setPassword(self, password):

        EnterPassword = self.driver.find_element_by_name(self.textbox_password_name)
        EnterPassword.clear()
        EnterPassword.send_keys(password)

    def clickLogin(self):

        PressLogin = self.driver.find_elements_by_xpath(self.button_login_xpath)
        PressLogin[0].click()


    def GetWelcomeText(self):
        Welcometext2 = self.driver.find_elements_by_xpath(self.WelcomeText_xpath)
        return (Welcometext2)
        #if Welcometext2[0].is_displayed():

    def VerifyLogoutText(self):
        GetLogoutMsg = self.driver.find_elements_by_xpath(self.LogoutMsg_xpath)[0].text
        return (GetLogoutMsg)


    def setUsername2(self, username2):
        EnterUsername2 = self.driver.find_element_by_class_name(self.textbox_username_className)
        EnterUsername2.clear()
        EnterUsername2.send_keys(username2)

    def setPassword2(self, password2):
        EnterPassword = self.driver.find_element_by_name(self.textbox_password_name)
        EnterPassword.clear()
        EnterPassword.send_keys(password2)











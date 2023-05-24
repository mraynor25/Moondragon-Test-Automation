from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class workspacePage():
    # Locators of all the elements
    firstDashboard_xpath = "//*/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[4]/div[2]/ul[1]/li"
    favDashButton_xpath = "//*/ul[1]/li/div[1]/div[2]/button[1]"
    timeFilter_xpath = "//*/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]"
    added2nduser_xpath = "//*/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[4]/div[2]/ul[1]/li"
    workspaceLink_xpath = "//h3[contains(@class, 'euiCollapsibleNavGroup__title')]"
    addedWorkspaceSuricata_xpath = "//strong[contains(text(),'Suricata [MOONDRAGON]')]"
    firstUser_dashXpath = "//*/div[2]/ul[1]/li/div[1]/div[1]/div[1]/span[1]/strong[1]"
    http_dashboardXpath = "//strong[contains(text(),'HTTP [MOONDRAGON]')]"
    welcome_dashboardXpath = "//strong[contains(text(),'*Welcome [MOONDRAGON]')]"
    open_workspaceMenu_xpath = "//*[contains(@class, 'euiAccordion__iconButton-isOpen')]"
    workspaceMenu_xpath = "//*/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]"
    Expand_workspaceMenu_xpath = "//*/div[3]/nav[1]/div[4]/div[1]/div[1]/button[2]"
    check_addedDashboard_xpath = "//*/div[2]/ul[1]/li/div[1]/div[1]/div[1]/span[1]/strong[1]"
    SMB_xpath = "//strong[contains(text(),'SMB [Moondragon]')]"
  #  SMTP_xpath = "//strong[contains(text(),'SMTP [Moondragon]')]"
    SMTP_xpath = "//strong[contains(text(),'SMTP [MOONDRAGON]')]"
    mydataTagsXpath = "//*/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/span[1]"
    remove_dashMsg_xpath = "//h1[contains(text(),'Remove This Dashboard')]"
    rowlistXpath = "//*/tbody[1]/tr[1]/td[1]/div[1]/span[1]"
    remove_dashYesButton_xpath = "//span[contains(text(),'Yes')]"
    updatedDashRec_xpath = "//*/div[2]/ul[1]/li/div[1]/div[1]/div[1]/span[1]/strong[1]"
    fav_button_xpath = "//*/ul[1]/li/div[1]/div[2]/button[1]"
    find_tag_xpath = "//*/table[1]/tbody[1]/tr/th[1]/div[2]/span[1]"
    toastMsg_deleteXpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]"
    pagin_exists_xpath = "//*/tbody[1]/tr[1]/td[1]/div[1]/span[1]"
    select_pagin_xpath = "//*/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]"
    row100_xpath = "//*/div[2]/div[1]/div[1]/div[1]/button[4]/span[1]/span[1]"

    def __init__(self, driver):
        self.driver = driver

    def navigateToFirstUserDashboard(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        first_userDashboard = self.driver.find_elements(By.XPATH, self.firstDashboard_xpath)

    def Verify_HTTPdashboard(self):
        if len(self.driver.find_elements(By.XPATH, self.http_dashboardXpath)) > 0:
            VerifyHTTP_dashboard = self.driver.find_elements(By.XPATH, self.http_dashboardXpath)[0].text
            self.assertEqual("HTTP [MOONDRAGON]", VerifyHTTP_dashboard, "Test failed, HTTP dashboard is not found")
        else:
            print("Test failed. HTTP dashboard locator is not found")

    def clickDashboard(self):
        ClickDashboard = self.driver.find_elements(By.XPATH, self.link_dashboardMunu_xpath)
        ClickDashboard[0].click()

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
            Workspacelink = self.driver.find_elements(By.XPATH, self.workspaceLink_xpath)
            Workspacelink[0].click()

    def addSeconduser(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        addedDashboard_2user = self.driver.find_elements(By.XPATH, self.added2nduser_xpath)

    def verify_dashExist(self, added_dash):
        workspace_addedDashboard = self.driver.find_elements(By.XPATH, self.addedWorkspaceSuricata_xpath)[0].text
        assert workspace_addedDashboard == added_dash

    def lastWorkspace(self):
        fav_dash_button = len(self.driver.find_elements(By.XPATH, self.favDashButton_xpath))

        last_workspace_button = self.driver.find_elements(By.XPATH, "//*/ul[1]/li[" + str(fav_dash_button) + "]/div[1]/div[2]/button[1]")
        last_workspace_button[0].click()

    def verifyTime_filter(self, GetTimeFrame_value):
        GetTimeFrame = GetTimeFrame_value

        time_filter = self.driver.find_elements(By.XPATH, self.timeFilter_xpath)[0].text
        assert GetTimeFrame == time_filter

    def firstUser_dashboard(self):
        first_userDashboard = len(self.driver.find_elements(By.XPATH, self.firstUser_dashXpath))
        return first_userDashboard

    def verifyHTTP_dash(self):
        VerifyHTTP_dashboard = self.driver.find_elements(By.XPATH, self.http_dashboardXpath)[0].text
        assert VerifyHTTP_dashboard == "HTTP [MOONDRAGON]"

    def verifyWelcome_dash(self):
        # if len(self.driver.find_elements_by_xpath(self.welcome_dashboardXpath)) > 0:
        VerifyWelcome_dashboard = self.driver.find_elements(By.XPATH, self.welcome_dashboardXpath)[0].text
        assert VerifyWelcome_dashboard == "*Welcome [MOONDRAGON]"

    def verify_addedDashboard(self, FirstUser_dash):
        userDashboard_1 = FirstUser_dash
        check_addedDashboard = len(self.driver.find_elements(By.XPATH, self.check_addedDashboard_xpath))
        assert check_addedDashboard != userDashboard_1


    def verifySMB_dash(self):
        VerifySMB_dashboard = self.driver.find_elements(By.XPATH, self.SMB_xpath)[0].text
        assert VerifySMB_dashboard == "SMB [Moondragon]"

    def verifySMTP_dash(self):
        VerifySMTP_dashboard = self.driver.find_elements(By.XPATH, self.SMTP_xpath)[0].text
        assert VerifySMTP_dashboard == "SMTP [MOONDRAGON]"

    def countTotal_dashboard(self):
        addedDashboard = self.driver.find_elements(By.XPATH, self.check_addedDashboard_xpath)
        total_dash = len(addedDashboard)
        return total_dash

    def delete_workspace(self, count_dash):
        total_dash = count_dash
        delete_dash = self.driver.find_elements(By.XPATH, "//*/div[1]/div[3]/div[2]/ul[1]/li[" + str(total_dash) + "]/div[1]/div[2]/button[2]")
        delete_dash[0].click()

    def remove_ws_msg(self):
        RemoveDash_msg = self.driver.find_elements(By.XPATH, self.remove_dashMsg_xpath)[0].text
        return RemoveDash_msg

    def remove_dashYes(self):
        clickRemoveDashYes = self.driver.find_elements(By.XPATH, self.remove_dashYesButton_xpath)
        clickRemoveDashYes[0].click()

    def updatedDash_Rec(self):
        UpdatedDashboardRec = self.driver.find_elements(By.XPATH, self.updatedDashRec_xpath)
        return UpdatedDashboardRec

    def added2ndUser_workspace(self):
        addedDashboard_2user = self.driver.find_elements(By.XPATH, self.check_addedDashboard_xpath)
        return addedDashboard_2user

    def last_favorite(self):
        fav_dash_button = len(self.driver.find_elements(By.XPATH, self.fav_button_xpath))
        last_workspace_button = self.driver.find_elements(By.XPATH, "//*/ul[1]/li[" + str(fav_dash_button) + "]/div[1]/div[2]/button[1]")
        last_workspace_button[0].click()

    def getMyTimefilter(self):
        time_filter = self.driver.find_elements(By.XPATH, self.timeFilter_xpath)[0].text
        return time_filter

    def click_myDataTagTab(self):
        mydataTags = self.driver.find_elements(By.XPATH, self.mydataTagsXpath)
        mydataTags[0].click()

    def click_row100(self):
        # if no item found
        if len(self.driver.find_elements(By.XPATH, self.rowlistXpath)) > 0:
            assert True
        else:
            select_pagin = self.driver.find_elements(By.XPATH, self.select_pagin_xpath)
            select_pagin[0].click()
            time.sleep(2)
            row100 = self.driver.find_elements(By.XPATH, self.row100_xpath)
            row100[0].click()

    def find_tagsfromList(self, tag_1, tag_2):
        findTag = len(self.driver.find_elements(By.XPATH, self.find_tag_xpath))

        for tag in range(1, findTag + 1):
            tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/th[1]/div[2]/span[1]")[
                0].text
            if tag_1 == tagName:
                assert False

        findTag = len(self.driver.find_elements(By.XPATH, self.find_tag_xpath))

        for tag in range(1, findTag + 1):
            tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/th[1]/div[2]/span[1]")[
                0].text
            if tag_2 == tagName:
                assert False

    def nofind_deleted_tag(self, tag_1, tag_2):
        if len(self.driver.find_elements(By.XPATH, self.pagin_exists_xpath)) > 0:
            assert True
        else:
            select_pagin = self.driver.find_elements(By.XPATH, self.select_pagin_xpath)
            select_pagin[0].click()
            time.sleep(2)
            row100 = self.driver.find_elements(By.XPATH, self.row100_xpath)
            row100[0].click()
            time.sleep(3)

            findTag = len(self.driver.find_elements(By.XPATH, self.find_tag_xpath))

            for tag in range(1, findTag + 1):
                tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/th[1]/div[2]/span[1]")[0].text
                if tag_1 == tagName:
                    assert False

            findTag = len(self.driver.find_elements(By.XPATH, self.find_tag_xpath))

            for tag in range(1, findTag + 1):
                tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/th[1]/div[2]/span[1]")[0].text
                if tag_2 == tagName:
                    assert False

    def deleteTags(self, tag_1, tag_2):
        if len(self.driver.find_elements(By.XPATH, self.rowlistXpath)) > 0:
            assert False
        else:
            select_pagin = self.driver.find_elements(By.XPATH, self.select_pagin_xpath)
            select_pagin[0].click()
            time.sleep(1)
            row100 = self.driver.find_elements(By.XPATH, self.row100_xpath)
            row100[0].click()
            time.sleep(4)

            findTag = len(self.driver.find_elements(By.XPATH, self.find_tag_xpath))

            for tg in range(1, findTag + 1):
                tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tg) + "]/th[1]/div[2]/span[1]")[0].text
                if tag_1 == tagName:
                    assert True
                    deleteTag = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tg) + "]/td[11]/div[1]/span[1]/button[1]")
                    deleteTag[0].click()
                    time.sleep(3)
                    toastMsg_delete = self.driver.find_elements(By.XPATH, self.toastMsg_deleteXpath)[0].text
                    assert toastMsg_delete == "Data tag deleted successfully"
                    time.sleep(4)
                    break
            self.driver.execute_script("window.scrollBy(0, 500)", "")

            for tag in range(1, findTag + 1):
                tagName = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/th[1]/div[2]/span[1]")[0].text
                if tag_2 == tagName:
                    assert True
                    deleteTag = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(tag) + "]/td[11]/div[1]/span[1]/button[1]")
                    deleteTag[0].click()
                    wait = WebDriverWait(self.driver, 6)
                    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@data-test-subj='globalToastList']"), "Data tag deleted successfully"))
                    # toastMsg_delete = \
                    # self.driver.find_elements_by_xpath("//*/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]")[0].text
                    # assert toastMsg_delete == "Data tag deleted successfully"
                    break
















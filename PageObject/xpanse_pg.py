import time
import glob
import unittest


class XpansePage():
    # Locators of all the elements
    loginXp_xpath = "//button[contains(text(), Login)]"
    IP_header_xpath = "//*/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]"

    def __init__(self,driver):
        self.driver = driver

    def switchToXpanse(self, x_username, x_password):

        main_page = self.driver.current_window_handle
        allGUID = self.driver.window_handles

        for handle in allGUID:
                if handle != main_page:
                    self.driver.switch_to.window(handle)
                    self.driver.implicitly_wait(10)
                    Xpanse_username = self.driver.find_elements_by_id("username")
                    Xpanse_username[0].send_keys(x_username)
                    Login_xp = self.driver.find_elements_by_xpath(self.loginXp_xpath)
                    Login_xp[0].click()
                    time.sleep(2)
                    password_xp = self.driver.find_elements_by_id("password")
                    password_xp[0].send_keys(x_password)
                    Login_xp = self.driver.find_elements_by_xpath(self.loginXp_xpath)
                    Login_xp[0].click()
                    self.driver.implicitly_wait(20)

    def verify_sip(self, get_sip):

        source_ip = get_sip

        source_ip_header = \
        self.driver.find_elements_by_xpath(self.IP_header_xpath)[0].text
        assert source_ip == source_ip_header
        self.driver.close()


    def switchToXpase_get_DestIP(self, get_dest_IP):
        main_page = self.driver.current_window_handle
        allGUID = self.driver.window_handles

        dest_ip = get_dest_IP
        for handle in allGUID:
            if handle != main_page:
                self.driver.implicitly_wait(10)
                self.driver.switch_to.window(handle)

                dest_ip_header = self.driver.find_elements_by_xpath(self.IP_header_xpath)[0].text
                assert dest_ip_header == dest_ip
                time.sleep(2)
                self.driver.close()





    def GobackToKibana_screen(self):

            main_page = self.driver.current_window_handle
            all_windowHandle = self.driver.window_handles

            for windowid in all_windowHandle:

                if (windowid != main_page):

                    self.driver.switch_to.window(main_page)


# if __name__ == '__main__':
#     unittest.main()

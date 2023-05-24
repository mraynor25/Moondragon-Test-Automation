import time
import glob
from selenium.webdriver.common.by import By
import unittest



class arkimePage():
    # Locators of all the elements
    dropArrow_xpath = "//*/span[1]/form[1]/div[2]/div[1]/button[1]"
    exportPCAP_xpath = "//*/span[1]/form[1]/div[2]/div[1]/ul[1]/li[1]/a[1]"
    plusIcon_xpath = "//*/tbody[1]/tr[1]/td[1]/a[1]/span[1]"
    downloadPCAP_xpath = "//*/td[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]"
    clear_data_searchbox_xpath = "//*//div[1]/span[1]/span[1]/form[1]/div[2]/div[3]/div[1]/span[3]/button[1]/span[1]"
    session_record_xpath = "//*/tbody[1]/tr/td[1]/a[1]/span[1]"
    tags_exist_xpath = "//*/tr[1]/td[12]/span[1]/span[1]/span[1]/span[1]/div[1]/div[18]/div[1]/div[1]/button[1]"
    particular_filedata_xpath = "//span[contains(text(),'/mnt/pcap/active/am/am-01/22/12/13/am-01-221213.ca')]"
    tags_xpath = "//*/div[2]/div[1]/dl[1]/div[1]/dt[1]/div[1]/button[1]"
    toggleTags_linkText = "Toggle Tags in Info column"
    searchBox_xpath = "//input[normalize-space(@class='form-control search-control')]"
    searchButton_xpath = "//span[contains(text(),'Search')]"
    ip_dst_xpath = "//*/tr/td[6]/span[1]/span[1]/span[1]/span[1]/div[1]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"
    port_data_xpath = "//*/tr/td[7]/span[1]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"
    packets_xpath = "//*/tr/td[11]/span[1]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"
    packets_label_xpath = "/div[3]/table[1]/thead[1]/tr[1]/th/span[1]"
    packet_button_xpath = "//*/form[1]/fieldset[1]/span[1]/div[1]/div[1]/button[1]"
    raw_packetOption_xpath = "//a[contains(text(), 'Show Raw Packets')]"
    actual_file_data_xpath = "//*/dd[11]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"
    count_packets_xpath = "//tbody/tr/td[1]/div[1]/div[3]/div/div[1]/div[1]"
    sen_name_xpath = "//*/tr/td[12]/span[1]/span[1]/span[1]/span[1]/div[1]/div[18]/div[1]/span[1]/span[2]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"
    ops_xpath = "//*/tr/td[12]/span[1]/span[1]/span[1]/span[1]/div[1]/div[18]/div[1]/span[1]/span[1]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]"

    def __init__(self,driver):
        self.driver = driver


    def switchToArkime_pg(self):
        main_page = self.driver.current_window_handle

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)


    def click_dropArrow(self):
        clickdropArrow = self.driver.find_elements(By.XPATH, self.dropArrow_xpath)
        clickdropArrow[0].click()


    def click_ExportPCAP(self):
        clickExportPCAP = self.driver.find_elements(By.XPATH, self.exportPCAP_xpath)
        clickExportPCAP[0].click()


    def click_plusIcon(self):
        clickPlusicon = self.driver.find_elements(By.XPATH, self.plusIcon_xpath)
        clickPlusicon[0].click()


    def verifydetect_downloadPCAP(self):
        start = time.time()

        # this is the time in seconds , we set to zero initially
        elapsed = 0

        # get file list before download
        list_of_files_before_download = glob.glob('C:/Users/mraynor/*.pcap')
        start = time.time()

        clickDownloadPCAP = self.driver.find_elements(By.XPATH, self.downloadPCAP_xpath)
        clickDownloadPCAP[0].click()

        # while elapsed <= 9:
        list_of_files_after_download = glob.glob('C:/Users/mraynor/*.pcap')
        done = time.time()
        elapsed = done - start
        return elapsed

    def verifyActualFile_ToggleTag(self, file_data):

        session_record = len(self.driver.find_elements(By.XPATH, self.session_record_xpath))

        for num_rec in range(1, session_record + 1):
            open_plus = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(num_rec) + "]/td[1]/a[1]/span[1]")
            open_plus[0].click()
            time.sleep(2)

            self.driver.execute_script("window.scrollBy(0,400)", "")
            actual_file_data = self.driver.find_elements(By.XPATH, self.actual_file_data_xpath)[0].text
           # print(actual_file_data)
            assert file_data == actual_file_data
            self.driver.execute_script("window.scrollBy(0,-400)", "")
            open_plus[0].click()
            time.sleep(2)

            # loop will stop after certain record (time filter values changes from 5th record
            if num_rec >= 4:
                break


    def clearSearchbox(self):
        clear_data_searchbox = self.driver.find_elements(By.XPATH, self.clear_data_searchbox_xpath)
        clear_data_searchbox[0].click()

    def enter_searchbox(self, Query):
        searchBox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        searchBox[0].send_keys(Query)
        time.sleep(2)

    def enter_searchbox2(self, Query2):
        searchBox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        searchBox[0].send_keys(Query2)
        time.sleep(2)

    def enter_searchbox3(self, Query3):
        searchBox = self.driver.find_elements(By.XPATH, self.searchBox_xpath)
        searchBox[0].send_keys(Query3)

    def click_searchButton(self):
        search_button = self.driver.find_elements(By.XPATH, self.searchButton_xpath)
        search_button[0].click()



    def verify_ipdst(self, ip_dst):
        ip_dst_data = self.driver.find_elements(By.XPATH, self.ip_dst_xpath)
        for ip_dst_output in ip_dst_data:
            assert ip_dst_output.text == ip_dst


    def verify_portdst(self, port_dst):
        port_data = self.driver.find_elements(By.XPATH, self.port_data_xpath)
        #print(port_data[0].text)

        for port_output in port_data:
            assert port_output.text == port_dst

    def verify_packet(self, pockets):
        packet_field = self.driver.find_elements(By.XPATH, self.packets_label_xpath)

        for p in packet_field:
            if p[0].text == "Packets":
                veri_packet = self.driver.find_elements(By.XPATH, "//*/tr/td["+str(p)+"]/span[1]/span[1]/span[1]/span[1]/span[1]/a[1]/span[1]")
                for packet in veri_packet:
                    assert packet.text == pockets
                break
            else:
                assert False


# Remove verify packets integer
    def verify_packets_integer(self, pockets_integer):
        session_record = len(self.driver.find_elements(By.XPATH, self.session_record_xpath))

        for num_rec in range(1, session_record + 1):
            open_plus = self.driver.find_elements(By.XPATH, "//*/tbody[1]/tr[" + str(num_rec) + "]/td[1]/a[1]/span[1]")
            open_plus[0].click()
            time.sleep(1)

            self.driver.execute_script("window.scrollBy(0,500)", "")
            time.sleep(2)

            packet_button = self.driver.find_elements(By.XPATH, self.packet_button_xpath)
            packet_button[0].click()
            time.sleep(2)

            select_option = self.driver.find_elements(By.XPATH, self.raw_packetOption_xpath)
            select_option[0].click()
            time.sleep(3)

            count_pocket = len(self.driver.find_elements(By.XPATH, self.count_packets_xpath))
            assert count_pocket == pockets_integer
            time.sleep(2)

            self.driver.execute_script("window.scrollBy(0,-500)", "")

            open_plus[0].click()
            time.sleep(2)

            if num_rec >= 2:
                break

    def clickPacket_button(self):
        packet_button = self.driver.find_elements(By.XPATH, self.packet_button_xpath)
        packet_button[0].click()

    def select_raw_packets(self):
        select_option = self.driver.find_elements(By.XPATH, self.raw_packetOption_xpath)
        select_option[0].click()



    def verify_sensor(self, sen_name):
        verify_sen_name = self.driver.find_elements(By.XPATH, self.sen_name_xpath)
        for sen in verify_sen_name:
            assert sen.text == sen_name

    def verify_ops(self, ops_check):
        verify_ops = self.driver.find_elements(By.XPATH, self.ops_xpath)
        for ops in verify_ops:
            assert ops.text == ops_check


    def GobackToKibana_screen(self):

            main_page = self.driver.current_window_handle
            all_windowHandle = self.driver.window_handles

            for windowid in all_windowHandle:

                if (windowid != main_page):

                    self.driver.switch_to.window(main_page)


# if __name__ == '__main__':
#     unittest.main()
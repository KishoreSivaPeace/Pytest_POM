import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Contact_Module import Contact_Locators


class FTPTab():
    def __init__(self, driver):
        self.driver = driver
        
    def ftp_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_tab).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.add_ftp_button).click()
        time.sleep(1)
        Format = self.driver.find_element(By.XPATH, Contact_Locators.ftp_format_dropdown)
        select1 = Select(Format)
        select1.select_by_visible_text("XML")
        Status = self.driver.find_element(By.XPATH, Contact_Locators.ftp_status_dropdown)
        select2 = Select(Status)
        select2.select_by_visible_text("Invoice")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_hostname_field).send_keys("KishoreSiva")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_username_field).send_keys("PeaceArt")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_password_field).send_keys("1103")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_path_field).send_keys("Automation")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_port_field).send_keys("12.498.156")
        Protocol = self.driver.find_element(By.XPATH, Contact_Locators.ftp_protocol_dropdown)
        select2 = Select(Protocol)
        select2.select_by_visible_text("FTP")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_save_button).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.add_ftp_button).click()
        time.sleep(1)
        Format = self.driver.find_element(By.XPATH, Contact_Locators.ftp_format_dropdown)
        select1 = Select(Format)
        select1.select_by_visible_text("CSV")
        Status = self.driver.find_element(By.XPATH, Contact_Locators.ftp_status_dropdown)
        select2 = Select(Status)
        select2.select_by_visible_text("Delivery Manifest")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_hostname_field).send_keys("KishoreSiva1")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_username_field).send_keys("PeaceArt1")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_password_field).send_keys("1103")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_path_field).send_keys("Automation1")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_port_field).send_keys("12.498.156.2")
        Protocol = self.driver.find_element(By.XPATH, Contact_Locators.ftp_protocol_dropdown)
        select2 = Select(Protocol)
        select2.select_by_visible_text("SFTP")
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_save_button).click()
        time.sleep(4)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.ftp_delete_icon)).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.ftp_delete_ok).click()
import time

from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class DocumentTab():
    def __init__(self, driver):
        self.driver = driver

    def document_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.document_tab).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.add_document_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.document_description_field).send_keys("Automation")
        self.driver.find_element(By.XPATH, Contact_Locators.document_attachment_button).send_keys(
            "C:/Users/Shift 1/Downloads/Automation.docx")
        self.driver.find_element(By.XPATH, Contact_Locators.document_save_button).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.add_document_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.document_description_field).send_keys("Automation")
        self.driver.find_element(By.XPATH, Contact_Locators.document_attachment_button).send_keys(
            "C:/Users/Shift 1/Downloads/Automation.docx")
        self.driver.find_element(By.XPATH, Contact_Locators.document_complete_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.document_complete_option).click()
        self.driver.find_element(By.XPATH, Contact_Locators.document_save_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.document_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.document_3dot_option).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.document_3dot_delete).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.document_3dot_delete_ok).click()

import time

from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators


class AlternativeDeliveryAddress():
    def __init__(self, driver):
        self.driver = driver

    def alternative_delivery_address(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_tab_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_show_more_but_id).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_appointment_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_appointment_field_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_appointment_contact_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_invoice_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_invoice_field_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_invoice_contact_id).click()
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_add_new_contact_id).click()
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_new_firstname_text_id).send_keys("Peace")
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_new_lastname_text_id).send_keys("Art")
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_new_contact_save_button_id).click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_invoice_field_id).click()
        # self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_invoice_contact_2_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.alter_deli_save_button_id).click()

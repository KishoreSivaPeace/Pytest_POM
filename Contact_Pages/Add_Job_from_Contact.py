import time

from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators
from Locators.Job_Form import Job_Form_Locators


class AddJobFromContact():
    def __init__(self, driver):
        self.driver = driver

    def add_job_from_contact(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_3dot).click()
        self.driver.find_element(By.XPATH, Contact_Locators.add_job_option).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, Job_Form_Locators.customer_ref_field).send_keys("Automation Customer")
        self.driver.find_element(By.XPATH, Job_Form_Locators.additional_ref_textbox_id).send_keys("Automation Testing")
        self.driver.find_element(By.XPATH, Job_Form_Locators.status_ref_field).send_keys("Automation")
        self.driver.find_element(By.XPATH, Job_Form_Locators.save_job_button_id).click()

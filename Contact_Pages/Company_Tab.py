import time

from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators
from Locators.Contact_Module import Contact_Locators


class CompanyTab():
    def __init__(self, driver):
        self.driver = driver

    def company_tab(self):
        time.sleep(9)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_from_3dot_options_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_form_3dot_view_account_id).click()
        time.sleep(2)
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        next_window_handle = window_handles[(window_handles.index(current_window_handle) + 1) % len(window_handles)]
        self.driver.switch_to.window(next_window_handle)
        time.sleep(10)
        self.driver.find_element(By.XPATH, Contact_Locators.company_tab).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.company_acc_ref_field).send_keys("ACC005")
        self.driver.find_element(By.XPATH, Contact_Locators.company_source_field).click()
        self.driver.find_element(By.XPATH, Contact_Locators.company_source_search).send_keys("FB")
        self.driver.find_element(By.XPATH, Contact_Locators.company_source_option).click()
        self.driver.find_element(By.XPATH, Contact_Locators.company_phone_field).send_keys("234589")
        self.driver.find_element(By.XPATH, Contact_Locators.company_email_field).send_keys("kishoresiva@gmail.com")
        self.driver.find_element(By.XPATH, Contact_Locators.company_website_field).send_keys("www.kishoresiva.com")
        self.driver.find_element(By.XPATH, Contact_Locators.company_fax_field).send_keys("785612")
        self.driver.find_element(By.XPATH, Contact_Locators.company_save_button).click()

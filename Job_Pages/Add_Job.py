import time
from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators


class AddJob():
    def __init__(self, driver):
        self.driver = driver

    def new_add_job(self):
        time.sleep(7)
        self.driver.find_element(By.XPATH, Job_Form_Locators.global_add_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_job_button_id).click()
        # self.driver.find_element(By.CSS_SELECTOR, self.company_name).send_keys("PeaceArt")
        time.sleep(8)
        self.driver.find_element(By.CSS_SELECTOR, Job_Form_Locators.first_name_textbox_id).send_keys("Kishore")
        self.driver.find_element(By.CSS_SELECTOR, Job_Form_Locators.last_name_textbox_id).send_keys("Siva")
        self.driver.find_element(By.XPATH, Job_Form_Locators.additional_ref_textbox_id).send_keys("Automation Testing")
        self.driver.find_element(By.XPATH, Job_Form_Locators.save_job_button_id).click()

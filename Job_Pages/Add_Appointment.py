import time

from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators


class AddAppointment():
    def __init__(self, driver):
        self.driver = driver

    def add_appointment(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_tab_id).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_appointment_id).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Job_Form_Locators.allday_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.allday_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_type_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_type_name_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.staff_id).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.staff_name_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Job_Form_Locators.travel_time_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_status_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_status_name_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_description_id).send_keys("Test Automation")
        self.driver.find_element(By.XPATH, Job_Form_Locators.appointment_save_button_id).click()



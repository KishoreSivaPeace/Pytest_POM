import time

from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators

class Checklist():
    def __init__(self, driver):
        self.driver = driver

    def checklist(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.checklist_tab_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.checklist_01_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.checklist_02_id).click()

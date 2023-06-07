import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Job_Form import Job_Form_Locators

class AddNotes():
    def __init__(self, driver):
        self.driver = driver

    def add_notes(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.notes_tab_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_notes_id).click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.notes_type_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("For Test")
        self.driver.find_element(By.XPATH, Job_Form_Locators.notes_description_text_id).send_keys(
            "For Automation Testing")
        self.driver.find_element(By.XPATH, Job_Form_Locators.notes_save_button_id).click()
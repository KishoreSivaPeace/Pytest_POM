import time

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Job_Form import Job_Form_Locators


class JobCopyEditDelete():
    def __init__(self, driver):
        self.driver = driver

    def job_copy_edit_delete(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_3dot_id ).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_copy_id).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_cost_price_id).click()
        pyautogui.press('tab')
        pyautogui.press('backspace')
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_cost_price_textbox_id).send_keys("4000")
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_override_id).send_keys(Keys.ENTER, Keys.ARROW_UP, Keys.ENTER)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_override_textbox_id).send_keys("5000")
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_save_button_id).click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_All_select_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_from_3dot_options_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.Job_from_3dot_copy_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_from_3dot_options_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.Job_from_3dot_paste_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_3dot_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_delete_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_delete_ok_id).click()
        time.sleep(5)
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.job_status_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("Order")
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.order_status_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("In Progress")
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.job_status_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("Invoiced")
        self.driver.find_element(By.XPATH, Job_Form_Locators.save_job_button_id).click()


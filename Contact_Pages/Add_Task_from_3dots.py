import time

import pyautogui
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class AddTaskFrom3Dots():
    def __init__(self, driver):
        self.driver = driver

    def add_task_from_3dots(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.lead_customer_name).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row_3dot).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_add_task_option).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_date_field).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_date_field).send_keys("1245PM")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_button).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_type).click()
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_every_field).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_every_field).send_keys("4")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_end_field).click()
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_repeat_save_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_description_field).send_keys("Automation Test")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_task_save_button).click()

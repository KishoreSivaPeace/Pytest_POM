import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class AddTaskFromContactTab():
    def __init__(self, driver):
        self.driver = driver
        
    def add_task_from_contact_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row).click()
        time.sleep(9)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_cancel_button).click()
        time.sleep(10)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_add_task_icon)).click().perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_date_field).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_date_field).send_keys("1245PM")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_button).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_type).click()
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_every_field).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_every_field).send_keys( "4")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_end_field).click()
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_repeat_save_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_description_field).send_keys("Automation Test")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_task_save_button).click()
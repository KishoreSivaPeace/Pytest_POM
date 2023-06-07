import time
import pyautogui
from selenium.webdriver.common.by import By
from Locators.Job_Form import Job_Form_Locators


class AddTask():
    def __init__(self, driver):
        self.driver = driver

    def add_task(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.task_tab_id).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_task_id).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.task_time_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.task_time_id).send_keys("1245PM")
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_toggle_id).click()
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_option_id).click()
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_every_id).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_every_id).send_keys("4")
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_end_id).click()
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Job_Form_Locators.repeat_save_id).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Job_Form_Locators.task_description_id).send_keys("Automation Test")
        self.driver.find_element(By.XPATH, Job_Form_Locators.task_save_button_id).click()

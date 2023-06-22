import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class AddAppointmentFrom3dots():
    def __init__(self, driver):
        self.driver = driver
        
    def add_appointment_from_3dots(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row_3dot).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_add_appointment_option).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_allday_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_repeat_button).click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_repeat_option)).click().perform()
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_repeat_every_field).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_repeat_every_field).send_keys("4")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_repeat_save_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_type).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_type_option).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_staff).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_staff_option).click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_traveltime).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_status).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_status_option).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_description_field).send_keys("Automation Test")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_appointment_save_button).click()
        
import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AddAppointmentFromContactTab():
    def __init__(self, driver):
        self.driver = driver
        
    def add_appointment_from_contact_tab(self):
        time.sleep(6)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[2]")).click().perform()
        time.sleep(8)
        self.driver.find_element(By.XPATH, "//*[@id='formID2']/div/div[2]/div[1]/div/div/label/div/label/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='repeatflag']/div/div/label/div").click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[1]/div/input")).click().perform()
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[2]/table/tbody/tr/td/div/input[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[2]/table/tbody/tr/td/div/input[1]").send_keys("4")
        self.driver.find_element(By.XPATH, "//*[@id='scheduleEditForm']/div[1]/div/div[2]/button[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Appointment type ']/following::mat-select[1]").click()
        self.driver.find_element(By.XPATH, "//*[text()='Measurer']").click()
        self.driver.find_element(By.XPATH, "//*[@id='employee']/div/div[1]/span").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@id='employee']/div/div[2]/ul[1]/li[1]/div").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='formID2']/div/div[5]/div/div[1]/div/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[text()='Appointment Status ']/following::div[1]").click()
        self.driver.find_element(By.XPATH, "//*[text()=' Confirmed ']").click()
        self.driver.find_element(By.XPATH, "//*[@id='jobDescription']").send_keys("Automation Test")
        self.driver.find_element(By.XPATH, "//*[@id='schedule_dialog_wrapper']/div[3]/button[2]").click()
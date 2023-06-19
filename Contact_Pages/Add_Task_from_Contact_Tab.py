import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AddTaskFromContactTab():
    def __init__(self, driver):
        self.driver = driver
        
    def add_task_from_contact_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/span/span/a").click()
        time.sleep(9)
        self.driver.find_element(By.XPATH, "//*[@id='leadcustform']/div[2]/button[2]").click()
        time.sleep(10)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[3]")).click().perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//*[text()='Add Task'])[2]/following::input[2]").click()
        self.driver.find_element(By.XPATH, "(//*[text()='Add Task'])[2]/following::input[2]").send_keys("1245PM")
        self.driver.find_element(By.XPATH, "(//*[@id='addtaskbody']/div[1]/div/div[4]/div[2]/div/div/label/div)[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[1]/div").click()
        time.sleep(2)
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH,  "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]").send_keys( "4")
        self.driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[5]/div[2]/span").click()
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/div/button[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//*[@id='taskdescription'])[2]").send_keys("Automation Test")
        self.driver.find_element(By.XPATH, "(//*[@id='addtaskform']/div[4]/input)[2]").click()
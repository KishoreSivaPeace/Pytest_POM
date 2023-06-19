import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddContactFromContactTab():
    def __init__(self, driver):
        self.driver = driver
        
    def add_contact_from_contact_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "//*[text()='Add New Contact']").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, "//*[@placeholder='Role']").send_keys("Tester")
        self.driver.find_element(By.XPATH, "(//*[@id='First Name'])[2]").send_keys("Peace")
        self.driver.find_element(By.XPATH, "(//*[@id='Last Name'])[2]").send_keys("Art")
        self.driver.find_element(By.XPATH, "(//*[text()='Phone'])[4]/following::input[1]").send_keys("234556")
        self.driver.find_element(By.XPATH, "(//*[@placeholder='Mobile'])[2]").send_keys("784512132")
        self.driver.find_element(By.XPATH, "(//*[text()='Email'])[2]/following::input[1]").send_keys("automation@gmail.com")
        self.driver.find_element(By.XPATH, "(//*[text()='Default Contact']/following::input[1])[2]").click()
        self.driver.find_element(By.XPATH, "(//*[text()='Account Ref'])[2]/following::input[1]").send_keys("Acc44")
        AddressType = self.driver.find_element(By.XPATH, "//*[@id='custform']/div[1]/div/div[4]/div/div[1]/div/div[2]/app-dynamic-field/select")
        select = Select(AddressType)
        select.select_by_visible_text("Delivery Address")
        self.driver.find_element(By.XPATH, "//*[@id='contact_zipcodepostcode']").send_keys("MK13")
        self.driver.find_element(By.XPATH, "//*[@id='contactDynamicform']/span/i").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").clear()
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").send_keys("Temple Tower")
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").clear()
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").send_keys("Anna Salai")
        self.driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[2]").clear()
        self.driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[2]").send_keys("Chennai")
        self.driver.find_element(By.XPATH, "//*[@id='custform']/div[1]/div/div[4]/div/div[5]/div/div[2]/app-dynamic-field/div/input").clear()
        self.driver.find_element(By.XPATH, "//*[@id='custform']/div[1]/div/div[4]/div/div[5]/div/div[2]/app-dynamic-field/div/input").send_keys("Tamil Nadu")
        self.driver.find_element(By.XPATH, "(//*[@name='ismarketingemails'])[1]").click()
        pyautogui.scroll(-1500)
        self.driver.find_element(By.XPATH, "(//*[@name='ismarketingemails'])[1]").click()
        self.driver.find_element(By.XPATH, "(//*[@name='isdocumentreceived'])[1]").click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='yes1']/following::i")).click().perform()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic0']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic1']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic2']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic3']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic4']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic5']").click()
        self.driver.find_element(By.XPATH, "//*[@id='custform']/div[2]/button[1]").click()
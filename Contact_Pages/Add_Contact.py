import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddContact():
    def __init__(self, driver):
        self.driver = driver

    def add_contact(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@class='nav-head']/mat-toolbar-row/div/div[1]/div/a[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@class='header']/div[2]/div/div[4]/button").click()
        self.driver.find_element(By.XPATH, "//*[@class='header']/div[2]/div/div[4]/div/a[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='contacttypemodel']/div/div/form/div/div/div[2]/mat-form-field").click()
        self.driver.find_element(By.XPATH, "(//*[@id='contact_choose-panel']/div/mat-option)[4]").click()
        self.driver.find_element(By.XPATH, "//*[@id='contacttypemodel']/div/div/form/div[3]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@placeholder='Role']").send_keys("Tester")
        self.driver.find_element(By.XPATH, "//*[@id='First Name']").send_keys("Peace")
        self.driver.find_element(By.XPATH, "//*[@id='Last Name']").send_keys("Art")
        self.driver.find_element(By.XPATH, "(//*[text()='Phone'])[4]/following::input[1]").send_keys("235689")
        self.driver.find_element(By.XPATH, "//*[@placeholder='Mobile']").send_keys("9876543210")
        self.driver.find_element(By.XPATH, "(//*[text()='Email'])[2]/following::input[1]").send_keys(
            "kishoresiva95@gmail.com")
        self.driver.find_element(By.XPATH, "(//*[text()='Default Contact']/following::input[1])[1]").click()
        self.driver.find_element(By.XPATH, "(//*[text()='Account Ref'])[2]/following::input[1]").send_keys("ACC004")
        pyautogui.scroll(-1500)
        self.driver.find_element(By.XPATH, "//*[text()='Company Name ']/following::input[1]").send_keys("11One Piece")
        self.driver.find_element(By.XPATH, "(//*[text()='Source'])[2]/following::div[1]").click()
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[3]").click()
        AddressType = self.driver.find_element(By.XPATH,
                                          "//*[@id='custform']/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/app-dynamic-field/select")
        select = Select(AddressType)
        select.select_by_visible_text("Invoice Address")
        self.driver.find_element(By.XPATH, "//*[@id='contact_zipcodepostcode']").send_keys("MK13")
        self.driver.find_element(By.XPATH, "//*[@id='contactDynamicform']/span/i").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").clear()
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").send_keys("Temple Tower")
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").clear()
        self.driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").send_keys("Anna Salai")
        self.driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[3]").clear()
        self.driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[3]").send_keys("Chennai")
        Country = self.driver.find_element(By.XPATH, "(//*[@id='contactDynamicform']/select)[3]")
        select = Select(Country)
        select.select_by_visible_text("USA")
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                            "//*[@id='contactDynamicform']/div/mat-form-field/div/div[1]/div/mat-select/div/div/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[42]").click()
        self.driver.find_element(By.XPATH, "(//*[@name='ismarketingemails'])[1]").click()
        self.driver.find_element(By.XPATH, "(//*[@name='isdocumentreceived'])[1]").click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, "//*[@id='yes1']/following::i")).perform()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic0']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic1']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic2']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic3']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic4']").click()
        self.driver.find_element(By.XPATH, "//*[@id='dynamic5']").click()
        self.driver.find_element(By.XPATH, "(//*[@name='isonlineportal'])[1]").click()
        action2 = ActionChains(self.driver)
        action2.move_to_element(self.driver.find_element(By.XPATH, "//*[text()='Set Configure ']")).perform()
        self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Name']").send_keys("KishoreSiva1")
        self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Password']").send_keys("1103")
        self.driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Confirm Password']").send_keys("1103")
        self.driver.find_element(By.XPATH, "//*[@id='custform']/div[2]/button[1]").click()

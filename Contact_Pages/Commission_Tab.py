import time

import pyautogui
from selenium.webdriver.common.by import By


class CommissionTab():
    def __init__(self,driver):
        self.driver = driver
    
    def commission_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[5]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='commission']").send_keys("45.89")
        self.driver.find_element(By.XPATH, "(//*[text()='Sales Consultant'])[2]/following::mat-form-field[1]/div").click()
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/mat-option[3]").click()
        self.driver.find_element(By.XPATH, "(//*[text()='Product'])[2]/following::mat-form-field[1]/div").click()
        self.driver.find_element(By.XPATH, "//*[@id='selectProduct']/following::mat-option[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='selectProduct']/following::mat-option[3]").click()
        self.driver.find_element(By.XPATH, "//*[@id='selectProduct']/following::mat-option[4]").click()
        pyautogui.press('tab')
        self.driver.find_element(By.XPATH, "//*[@class='greenbtn ng-star-inserted Newsavebtn Newsavebtn_Onchange']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='commission']").send_keys("25.89")
        self.driver.find_element(By.XPATH, "(//*[text()='Sales Consultant'])[2]/following::mat-form-field[1]/div").click()
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/mat-option[2]").click()
        self.driver.find_element(By.XPATH, "(//*[text()='Product'])[2]/following::mat-form-field[1]/div").click()
        self.driver.find_element(By.XPATH, "//*[@id='selectProduct']/following::mat-option[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='selectProduct']/following::mat-option[3]").click()
        pyautogui.press('tab')
        self.driver.find_element(By.XPATH, "//*[@class='greenbtn ng-star-inserted Newsavebtn Newsavebtn_Onchange']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='commision']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div[1]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='commision']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[5]/div[3]/span/i").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                            "//*[@id='commision']/div/div[6]/div/div[2]/div/app-commissionheader/div/div[3]/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[text()=' Send Emails to The Consultant When Placed Orders Through Trade Online Portal ']/span").click()
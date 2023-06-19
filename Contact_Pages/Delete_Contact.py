import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DeleteContact():
    def __init__(self, driver):
        self.driver = driver
        
    def delete_contact(self):
        time.sleep(6)
        # From Contact Tab
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                   "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[1]")).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
        time.sleep(5)
        # From 3dots
        self.driver.find_element(By.XPATH, "html/body/app-root/main/section/app-customer/div[1]/ul/li[1]/span").click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/button/i").click()
        self.driver.find_element(By.XPATH, "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[5]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
        time.sleep(9)
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class OnlinePortalTab():
    def __init__(self, driver):
        self.driver = driver
        
    def online_portal_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[10]").click()
        time.sleep(4)
        Alljobs = self.driver.find_element(By.XPATH, "//*[@id='alljobview']")
        select1 = Select(Alljobs)
        select1.select_by_visible_text("Default View")
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@id='discountorder']").clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='discountorder']").send_keys("15")
        pyautogui.press('tab')
        time.sleep(3)
        Language = self.driver.find_element(By.XPATH, "//*[@id='orderlanguage']")
        select2 = Select(Language)
        select2.select_by_visible_text("English")
        time.sleep(3)
        Notification = self.driver.find_element(By.XPATH, "//*[@id='Notification']")
        select3 = Select(Notification)
        select3.select_by_visible_text("Acknowledge Template")
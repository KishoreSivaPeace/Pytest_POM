import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FTPTab():
    def __init__(self, driver):
        self.driver = driver
        
    def ftp_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[11]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(1)
        Format = self.driver.find_element(By.XPATH, "//*[@id='for_mat']")
        select1 = Select(Format)
        select1.select_by_visible_text("XML")
        Status = self.driver.find_element(By.XPATH, "//*[@id='status']")
        select2 = Select(Status)
        select2.select_by_visible_text("Invoice")
        self.driver.find_element(By.XPATH, "//*[@id='hostname']").send_keys("KishoreSiva")
        self.driver.find_element(By.XPATH, "//*[@id='username1']").send_keys("PeaceArt")
        self.driver.find_element(By.XPATH, "//*[@id='password1']").send_keys("1103")
        self.driver.find_element(By.XPATH, "//*[@id='path']").send_keys("Automation")
        self.driver.find_element(By.XPATH, "//*[@id='port']").send_keys("12.498.156")
        Protocol = self.driver.find_element(By.XPATH, "//*[@id='protocol']")
        select2 = Select(Protocol)
        select2.select_by_visible_text("FTP")
        self.driver.find_element(By.XPATH, "//*[@id='ftppopup']/div/div/form/div[3]/button[1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(1)
        Format = self.driver.find_element(By.XPATH, "//*[@id='for_mat']")
        select1 = Select(Format)
        select1.select_by_visible_text("CSV")
        Status = self.driver.find_element(By.XPATH, "//*[@id='status']")
        select2 = Select(Status)
        select2.select_by_visible_text("Delivery Manifest")
        self.driver.find_element(By.XPATH, "//*[@id='hostname']").send_keys("KishoreSiva1")
        self.driver.find_element(By.XPATH, "//*[@id='username1']").send_keys("PeaceArt1")
        self.driver.find_element(By.XPATH, "//*[@id='password1']").send_keys("1103")
        self.driver.find_element(By.XPATH, "//*[@id='path']").send_keys("Automation1")
        self.driver.find_element(By.XPATH, "//*[@id='port']").send_keys("12.498.156.2")
        Protocol = self.driver.find_element(By.XPATH, "//*[@id='protocol']")
        select2 = Select(Protocol)
        select2.select_by_visible_text("SFTP")
        self.driver.find_element(By.XPATH, "//*[@id='ftppopup']/div/div/form/div[3]/button[1]").click()
        time.sleep(4)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH,
                                                   "//*[@id='ftpdetails']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]/app-ftpdelete")).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
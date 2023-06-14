import time

from selenium.webdriver.common.by import By


class DocumentTab():
    def __init__(self, driver):
        self.driver = driver
        
    def document_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[8]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@name='text']").send_keys("Automation")
        self.driver.find_element(By.XPATH, "//*[@id='addnotesdocform']/div[2]/div/div[2]/div/div[2]/div/input").send_keys(
            "C:/Users/Shift 1/Downloads/Automation.docx")
        self.driver.find_element(By.XPATH, "//*[@id='addnotesdocform']/div[3]/button[1]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[@class='Newaddbtn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@name='text']").send_keys("Automation")
        self.driver.find_element(By.XPATH, "//*[@id='addnotesdocform']/div[2]/div/div[2]/div/div[2]/div/input").send_keys(
            "C:/Users/Shift 1/Downloads/Automation.docx")
        self.driver.find_element(By.XPATH,
                            "//*[@id='addnotesdocform']/div[2]/div/div[3]/div/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[text()=' No']").click()
        self.driver.find_element(By.XPATH, "//*[@id='addnotesdocform']/div[3]/button[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='note']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='note']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[10]/div[3]/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                            "//*[@id='note']/div/div[6]/div/div[2]/div/app-noteheader/div/div[3]/span").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
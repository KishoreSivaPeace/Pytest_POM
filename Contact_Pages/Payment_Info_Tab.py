import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PaymentInfoTab():
    def __init__(self, driver):
        self.driver =driver
        
    def payment_info_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[4]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "(//*[@class='radiomark'])[1]").click()
        time.sleep(3)
        FilterDate = self.driver.find_element(By.XPATH, "(//*[@class='radiomark'])[2]/following::select[1]")
        select = Select(FilterDate)
        select.select_by_visible_text("Last 30 Days")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]/editor-cell/input").send_keys(
            "4.89")
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[9]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]").click()
        self.driver.find_element(By.XPATH, "(//*[@col-id='paiddate'])[2]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//*[@class='radiomark'])[2]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[text()='Bulk Payments']").click()
        time.sleep(3)
        PayMethod = self.driver.find_element(By.XPATH, "//*[@id='payment_method']")
        select1 = Select(PayMethod)
        select1.select_by_visible_text("Paypal")
        PayType = self.driver.find_element(By.XPATH, "//*[@name='paymenttype']")
        select2 = Select(PayType)
        select2.select_by_visible_text("Intermediate")
        JobStatusBulk = self.driver.find_element(By.XPATH, "//*[@name='jobStatus']")
        select3 = Select(JobStatusBulk)
        select3.select_by_visible_text("Invoiced")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='BulkUpdateModal']/div/div/form/div[2]/div[3]/ag-grid-angular/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/input").click()
        self.driver.find_element(By.XPATH, "//*[@name='amount']").send_keys("15.78")
        self.driver.find_element(By.XPATH, "//*[@id='BulkUpdateModal']/div/div/form/div[3]/button[1]").click()
        time.sleep(4)
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[3]/div[2]/div")).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[text()='Add Credit']/following::input[1]").send_keys("420")
        self.driver.find_element(By.XPATH, "//*[text()='Add Credit']/following::button[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[3]/div[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//*[@class='radiomark'])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]/editor-cell/input").send_keys(
            "5.89")
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[9]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]").click()
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        self.driver.find_element(By.XPATH, "(//*[@col-id='paiddate'])[2]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='radiomark'])[2]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[text()='Bulk Payments']").click()
        time.sleep(3)
        PayMethod = self.driver.find_element(By.XPATH, "//*[@id='payment_method']")
        select11 = Select(PayMethod)
        select11.select_by_visible_text("Paypal")
        PayType = self.driver.find_element(By.XPATH, "//*[@name='paymenttype']")
        select22 = Select(PayType)
        select22.select_by_visible_text("Redeem Credit Note")
        JobStatusBulk = self.driver.find_element(By.XPATH, "//*[@name='jobStatus']")
        select33 = Select(JobStatusBulk)
        select33.select_by_visible_text("Invoiced")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                            "//*[@id='BulkUpdateModal']/div/div/form/div[2]/div[3]/ag-grid-angular/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/input").click()
        self.driver.find_element(By.XPATH, "//*[@name='amount']").send_keys("15.78")
        self.driver.find_element(By.XPATH, "//*[@id='BulkUpdateModal']/div/div/form/div[3]/button[1]").click()
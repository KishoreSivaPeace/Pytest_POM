import time
from datetime import datetime

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

# Login
# driver.get("https://curtainmatrix.co.uk/finaltesting")
# driver.find_element(By.XPATH, "//*[@id='companyname']").send_keys("KISHORESIVADB")
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1103")
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
# time.sleep(5)

# # Add Contact
# driver.find_element(By.XPATH, "//*[@class='nav-head']/mat-toolbar-row/div/div[1]/div/a[6]").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@class='header']/div[2]/div/div[4]/button").click()
# driver.find_element(By.XPATH, "//*[@class='header']/div[2]/div/div[4]/div/a[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='contacttypemodel']/div/div/form/div/div/div[2]/mat-form-field").click()
# driver.find_element(By.XPATH, "(//*[@id='contact_choose-panel']/div/mat-option)[4]").click()
# driver.find_element(By.XPATH, "//*[@id='contacttypemodel']/div/div/form/div[3]/button[1]").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@placeholder='Role']").send_keys("Tester")
# driver.find_element(By.XPATH, "//*[@id='First Name']").send_keys("Peace")
# driver.find_element(By.XPATH, "//*[@id='Last Name']").send_keys("Art")
# driver.find_element(By.XPATH, "(//*[text()='Phone'])[4]/following::input[1]").send_keys("235689")
# # (//*[@id="custform"]/div[1]/div/div)[2]/div[1]/div[5]/div/div[2]
# driver.find_element(By.XPATH, "//*[@placeholder='Mobile']").send_keys("9876543210")
# driver.find_element(By.XPATH, "(//*[text()='Email'])[2]/following::input[1]").send_keys("kishoresiva95@gmail.com")
# driver.find_element(By.XPATH, "(//*[text()='Default Contact']/following::input[1])[1]").click()
# driver.find_element(By.XPATH, "(//*[text()='Account Ref'])[2]/following::input[1]").send_keys("ACC004")
# pyautogui.scroll(-1500)
# driver.find_element(By.XPATH, "//*[text()='Company Name ']/following::input[1]").send_keys("11One Piece")
# driver.find_element(By.XPATH, "(//*[text()='Source'])[2]/following::div[1]").click()
# driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[3]").click()
# AddressType = driver.find_element(By.XPATH, "//*[@id='custform']/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/app-dynamic-field/select")
# select = Select(AddressType)
# select.select_by_visible_text("Invoice Address")
# driver.find_element(By.XPATH, "//*[@id='contact_zipcodepostcode']").send_keys("MK13")
# driver.find_element(By.XPATH, "//*[@id='contactDynamicform']/span/i").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").clear()
# driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[1]").send_keys("Temple Tower")
# driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").clear()
# driver.find_element(By.XPATH, "//*[text()='Contact Info ']/following::textarea[2]").send_keys("Anna Salai")
# driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[3]").clear()
# driver.find_element(By.XPATH, "(//*[text()='Town / City']/following::input[1])[3]").send_keys("Chennai")
# Country = driver.find_element(By.XPATH, "(//*[@id='contactDynamicform']/select)[3]")
# select = Select(Country)
# select.select_by_visible_text("USA")
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='contactDynamicform']/div/mat-form-field/div/div[1]/div/mat-select/div/div/span").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[42]").click()
# driver.find_element(By.XPATH, "(//*[@name='ismarketingemails'])[1]").click()
# driver.find_element(By.XPATH, "(//*[@name='isdocumentreceived'])[1]").click()
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.XPATH, "//*[@id='yes1']/following::i")).perform()
# driver.find_element(By.XPATH, "//*[@id='dynamic0']").click()
# driver.find_element(By.XPATH, "//*[@id='dynamic1']").click()
# driver.find_element(By.XPATH, "//*[@id='dynamic2']").click()
# driver.find_element(By.XPATH, "//*[@id='dynamic3']").click()
# driver.find_element(By.XPATH, "//*[@id='dynamic4']").click()
# driver.find_element(By.XPATH, "//*[@id='dynamic5']").click()
# driver.find_element(By.XPATH, "(//*[@name='isonlineportal'])[1]").click()
# action2 = ActionChains(driver)
# action2.move_to_element(driver.find_element(By.XPATH, "//*[text()='Set Configure ']")).perform()
# driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Name']").send_keys("KishoreSiva1")
# driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Password']").send_keys("1103")
# driver.find_element(By.XPATH, "//*[@placeholder='Enter Your Confirm Password']").send_keys("1103")
# driver.find_element(By.XPATH, "//*[@id='custform']/div[2]/button[1]").click()

# Add Job from Contact
driver.find_element(By.XPATH, "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div/div/div/span").click()
driver.find_element(By.XPATH, "(//*[text()=' Add Job'])[1]").click()
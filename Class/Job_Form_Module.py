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
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)


# login
# driver.get("https://curtainmatrix.co.uk/finaltesting")
# driver.find_element(By.XPATH, "//*[@id='companyname']").send_keys("KISHORESIVADB")
# driver.find_element(By.CSS_SELECTOR, "#username").send_keys("admin")
# driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1103")
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[4]/button[1]").click()
# time.sleep(5)

# Global add and add job
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-dashboard-new/app-navbar/div/mat-toolbar-row/div/div[2]/a[1]").click()
# driver.find_element(By.XPATH,"//*[@class='cdk-overlay-pane']/div/div/li[1]").click()
# time.sleep(8)
# # driver.find_element(By.CSS_SELECTOR,"#Company\ Name").send_keys("PeaceArt")
# driver.find_element(By.CSS_SELECTOR,"#First\ Name").send_keys("Kishore")
# driver.find_element(By.CSS_SELECTOR,"#Last\ Name").send_keys("Siva")
# driver.find_element(By.XPATH, "//*[text()='Additional Ref']/following::input[1]").send_keys("Automation Testing")
# driver.find_element(By.XPATH,"/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[2]/button[1]").click()

# Add Job Item
# time.sleep(5)
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.XPATH, "//*[@id='dropdownMenuLink']")).perform()
# driver.find_element(By.XPATH, "//*[@id='selectProductcustom']").send_keys("Roller")
# action.move_to_element(driver.find_element(By.XPATH, "(//*[text()='Roller'])[1]")).click().perform()
# time.sleep(10)
# driver.find_element(By.XPATH, "//*[text()='Room']/following::input[1]").send_keys("Hall")
# driver.find_element(By.XPATH, "//*[text()='Blind or Recess']/following::input[1]").click()
# driver.find_element(By.XPATH, "//*[text()='Blind']").click()
# time.sleep(2)
# pyautogui.press('down')
# pyautogui.press('space')
# pyautogui.press('enter')
# driver.find_element(By.XPATH, "(//*[text()='Width'])[2]/following::input[1]").send_keys("1500")
# driver.find_element(By.XPATH, "(//*[text()='Drop'])[2]/following::input[1]").send_keys("2000")
# time.sleep(2)
# dropdown = driver.find_element(By.XPATH, "(//*[text()='Product Type'])[2]/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("FB Band A")
# time.sleep(2)
# driver.find_element(By.XPATH, "(//*[text()='Fabric'])[2]/following::input[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[contains(text(), 'Kaila')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[text()='Color']/following::input[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[text()='Smoke']").click()
# driver.find_element(By.XPATH, "//*[@id=\"sampleModal1\"]/div/div/div[2]/div/div[2]/div[2]/button[1]").click()

# Appointment
# time.sleep(10)
# driver.find_element(By.XPATH, "//*[@id='datessection']/mat-tab-header/div[2]/div/div/div[2]").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id='datessection']/div/mat-tab-body[2]/div/div/div/button").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id='formID2']/div/div[2]/div[1]/div/div/label/div/label/span").click()
# driver.find_element(By.XPATH, "//*[text()='Appointment type ']/following::mat-select[1]").click()
# driver.find_element(By.XPATH, "//*[text()='Measurer']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='employee']/div/div[1]/span").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[text()='Select All']").click()
# driver.find_element(By.XPATH, "//*[@id='formID2']/div/div[5]/div/div[1]/div/div[1]").click()
# driver.find_element(By.XPATH, "//*[text()='Appointment Status ']/following::div[1]").click()
# driver.find_element(By.XPATH, "//*[text()=' Confirmed ']").click()
# driver.find_element(By.XPATH, "//*[@id='jobDescription']").send_keys("Test Automation")
# driver.find_element(By.XPATH, "//*[@id='schedule_dialog_wrapper']/div[3]/button[2]").click()

# Task
# driver.find_element(By.XPATH, "//*[@id='datessection']/mat-tab-header/div[2]/div/div/div[3]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='datessection']/div/mat-tab-body[3]/div/div/div/button").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "(//*[text()='Add Task'])[2]/following::input[2]").click()
# driver.find_element(By.XPATH, "(//*[text()='Add Task'])[2]/following::input[2]").send_keys("1245PM")
# driver.find_element(By.XPATH, "(//*[@id='addtaskbody']/div[1]/div/div[4]/div[2]/div/div/label/div)[2]").click()
# driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[1]/div").click()
# pyautogui.press('down')
# pyautogui.press('enter')
# driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]").send_keys("4")
# driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[5]/div[2]/span").click()
# pyautogui.press('down')
# pyautogui.press('enter')
# time.sleep(1)
# driver.find_element(By.XPATH, "//*[@id='RecurrenceEditor']/div/button[1]").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "(//*[@id='taskdescription'])[2]").send_keys("Automation Test")
# driver.find_element(By.XPATH, "(//*[@id='addtaskform']/div[4]/input)[2]").click()

# Edit and Copy Job Item
# driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/app-moreoptionsrender/div/button/i").click()
# driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/app-moreoptionsrender/div/div/a[1]").click()
# time.sleep(10)
# current_date = datetime.now()
# date_string = current_date.strftime('%d-%m-%Y')
# driver.find_element(By.XPATH, "//*[@id='collapseOne']/div/form/div/div[4]/igx-date-picker/igx-input-group/div[1]/div/input").send_keys(date_string)
# driver.find_element(By.XPATH, "(//*[text()='Cost Price'])[2]/following::div[2]").click()
# pyautogui.press('tab')
# pyautogui.press('backspace')
# driver.find_element(By.XPATH, "(//*[text()='Cost Price'])[2]/following::input[2]").send_keys("4000")
# driver.find_element(By.XPATH, "//*[@id='pricecalc']").send_keys(Keys.ENTER,Keys.ARROW_UP,Keys.ENTER)
# driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[5]/input").send_keys("5000")
# driver.find_element(By.XPATH, "//*[@id='sampleModal1']/div/div/div[2]/div/div[2]/div[2]/button[1]").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/button[5]").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/button[6]").click()
# driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/app-moreoptionsrender/div/button/i").click()
# driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/app-moreoptionsrender/div/div/a[3]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]").click()
# time.sleep(5)
# dropdown = driver.find_element(By.XPATH, "(//*[text()='Job Status'])[3]/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("Order")
# dropdown = driver.find_element(By.XPATH, "(//*[text()='Order Status'])[3]/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("In Progress")
# driver.find_element(By.XPATH,"/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[2]/button[1]").click()

# Payments
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id='pricedet']/mat-tab-header/div[2]/div/div/div[2]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='pricedet']/div/mat-tab-body[2]/div/div/div/button").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[text()=' Amount ']/following::input[1]").send_keys("43.89")
# dropdown = driver.find_element(By.XPATH, "//*[text()=' Payment Method']/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("Credit Card")
# dropdown = driver.find_element(By.XPATH, "//*[text()=' Payment Type']/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("Deposit")
# driver.find_element(By.XPATH, "//*[text()=' Notes']/following::textarea[1]").send_keys("For Automation Testing")
# driver.find_element(By.XPATH, "//*[@id='addpaymentModal']/div/div/form/div[3]/button[1]").click()

# CheckList
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id='pricedet']/mat-tab-header/div[2]/div/div/div[3]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='pricedet']/div/mat-tab-body[3]/div/div[1]/div[1]/div[1]/input").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='pricedet']/div/mat-tab-body[3]/div/div[1]/div[2]/div[1]/input").click()

# Notes
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/mat-tab-header/div[2]/div/div/div[2]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/div/mat-tab-body[2]/div/div/div/div/button").click()
# time.sleep(3)
# dropdown = driver.find_element(By.XPATH, "//*[text()='Type ']/following::select[1]")
# select = Select(dropdown)
# select.select_by_visible_text("For Test")
# driver.find_element(By.XPATH, "(//*[text()=' Description']/following::textarea[1])[1]").send_keys("For Automation Testing")
# driver.find_element(By.XPATH, "//*[@id='addNotesModal']/div/div/form/div[3]/button[1]").click()

# Further Info
# time.sleep(5)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/mat-tab-header/div[2]/div/div/div[3]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/div/mat-tab-body[3]/div/div/div/button").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[text()=' Terms Name ']/following::input[1]").send_keys("Automation")
# driver.find_element(By.XPATH, "//*[text()=' Is Report Show']/following::input[1]").click()
# driver.find_element(By.XPATH, "//*[@id='furtherinfoModal']/div/div/form/div[2]/div/div[3]/div/div/div/angular-editor/div/div/div").send_keys("For Automation Testing")
# driver.find_element(By.XPATH, "//*[@id='furtherinfoModal']/div/div/form/div[3]/button[1]").click()

# Alternative Delivery Address
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/mat-tab-header/div[2]/div/div/div[1]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//*[@id='notesshowmore']/div/mat-tab-body[1]/div/div/div[2]/button").click()
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[1]/div/div/div/label/span").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[1]/div/div/div/span/div").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[1]/div/div/div/span/div/div/div/a").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/label/span").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/span/div").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/span/div/div/div/a").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/span/div/div/a").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "(//*[text()='First Name'])[4]/following::input[1]").send_keys("Peace")
# driver.find_element(By.XPATH, "(//*[text()='Last Name'])[2]/following::input[1]").send_keys("Art")
# driver.find_element(By.XPATH, "//*[@id='custform']/div[2]/button[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/span/div").click()
# driver.find_element(By.XPATH, "(//*[@id='alterForm']/div[2]/div/div/div[2]/div/div/div/span/div/div/div/a)[2]").click()
# driver.find_element(By.XPATH, "//*[@id='alterForm']/div[3]/button[1]").click()

# LogOut
# driver.find_element(By.XPATH, "//*[@class='nav-head']/mat-toolbar-row/div/div[2]/a[3]/a").click()
# driver.find_element(By.XPATH, "//*[text()='Log out ']").click()

# Check Account
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button").click()
# driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/button[2]").click()
# time.sleep(2)
# current_window_handle = driver.current_window_handle
# window_handles = driver.window_handles
# next_window_handle = window_handles[(window_handles.index(current_window_handle) + 1) % len(window_handles)]
# driver.switch_to.window(next_window_handle)
# time.sleep(5)
# driver.find_element(By.XPATH, "(//*[text()='Phone'])[3]/following::input[1]").send_keys("123456789")


# CreatedDate = driver.find_element(By.XPATH, "(//*[@id='jobinput']/igx-input-group/div[1]/div/input)[1]").get_attribute("value")
# OrderDate = driver.find_element(By.XPATH, "(//*[@id='jobinput']/igx-input-group/div[1]/div/input)[2]").get_attribute("value")
# DueDate = driver.find_element(By.XPATH, "(//*[@id='jobinput']/igx-input-group/div[1]/div/input)[3]").get_attribute("value")
# InvoiceDate = driver.find_element(By.XPATH, "(//*[@id='jobinput']/igx-input-group/div[1]/div/input)[4]").get_attribute("value")
# CompletedDate = driver.find_element(By.XPATH, "(//*[@id='jobinput']/igx-input-group/div[1]/div/input)[5]").get_attribute("value")
# print("Created Date :", CreatedDate)
# print("Order Date :", OrderDate)
# print("Due Date :", DueDate)
# print("Invoice Date :", InvoiceDate)
# print("Completed Date :", CompletedDate)
#
# JobRefNo = driver.find_element(By.XPATH,  "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[1]/form/div/div[3]/div/div[2]/div/input").get_attribute("value")
# InvoiceNo = driver.find_element(By.XPATH, "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[1]/form/div/div[6]/div/div[2]/div/input").get_attribute("value")
# TotalCostPrice = driver.find_element(By.XPATH, "(//*[@id='pricedet']/div/mat-tab-body[1]/div/form/div/div/div[1]/div[3])[1]/input").get_attribute("value")
# print("Job Ref No :", JobRefNo)
# print("Invoice No :", InvoiceNo)
# print("Total Cost Price", TotalCostPrice)
#
# dropdown = driver.find_element(By.XPATH, "(//*[text()='Job Status'])[3]/following::select[1]")
# select = Select(dropdown)
# JobStatus = select.first_selected_option
# print("Job Status :", JobStatus.text)
#
# dropdown = driver.find_element(By.XPATH, "(//*[text()='Order Status'])[3]/following::select[1]")
# select1 = Select(dropdown)
# OrderStatus = select1.first_selected_option
# print("Order Status :", OrderStatus.text)
#
# CreatedDate_OI = driver.find_element(By.XPATH, "//*[@id='collapseOne']/div/form/div/div[2]/igx-date-picker/igx-input-group/div[1]/div/input").get_attribute("value")
# ProductionDate_OI = driver.find_element(By.XPATH, "//*[@id='collapseOne']/div/form/div/div[4]/igx-date-picker/igx-input-group/div[1]/div/input").get_attribute("value")
# CostPrice_OI = driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[3]/input[1]").get_attribute("value")
# OverridePrice_OI = driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[5]/input[1]").get_attribute("value")
# NetPrice_OI = driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[7]/input[1]").get_attribute("value")
# VAT_OI = driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[9]/input[1]").get_attribute("value")
# GrossPrice_OI = driver.find_element(By.XPATH, "//*[@id='collapseTwo']/div/form/div/div[11]/input[1]").get_attribute("value")
# print("Order Item Created Date :", CreatedDate_OI)
# print("Order Item Production Date :", ProductionDate_OI)
# print("Order Item Cost Price :", CostPrice_OI)
# print("Order Item Override Price :", OverridePrice_OI)
# print("Order Item Net Price :", NetPrice_OI)
# print("Order Item VAT Price :", VAT_OI)
# print("Order Item Gross Price :", GrossPrice_OI)

# OrderItemQty_Row = driver.find_element(By.XPATH, "(//*[@col-id='qty'])[2]").text
# OrderItemItem_Row = driver.find_element(By.XPATH, "(//*[@col-id='costprice'])[2]").text
# OrderItemNet_Row = driver.find_element(By.XPATH, "(//*[@col-id='netprice'])[2]").text
# OrderItemVAT_Row = driver.find_element(By.XPATH, "(//*[@col-id='vat'])[2]").text
# OrderItemGross_Row = driver.find_element(By.XPATH, "(//*[@col-id='grossprice'])[2]").text
# OrderItemOverride_Row = driver.find_element(By.XPATH, "(//*[@col-id='overridenetprice'])[2]").text
# print("Qty :", OrderItemQty_Row)
# print("Item :", OrderItemItem_Row)
# print("Net :", OrderItemNet_Row)
# print("VAT :", OrderItemVAT_Row)
# print("Gross :", OrderItemGross_Row)
# print("Override :", OrderItemOverride_Row)


# TotalQty = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[3]").text
# TotalItemCost = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[4]").text
# TotalNet = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[5]").text
# TotalVAT = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[6]").text
# TotalGross = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[7]").text
# TotalOverride = driver.find_element(By.XPATH, "//*[@id='jobproduct_grid']/div/div[2]/div[2]/div[4]/div[2]/div/div/div[8]").text
# print("Total Qty :", TotalQty)
# print("Total Item Cost :", TotalItemCost)
# print("Total Net :", TotalNet)
# print("Total VAT :", TotalVAT)
# print("Total Gross :", TotalGross)
# print("Total Override :", TotalOverride)
#
# text1 = TotalItemCost
# text2 = TotalCostPrice
# if text1 == text2:
#     print("Total Item Cost and Cost Price are equal")
# else:
#     print("Total Item Cost and Cost Price are not equal")
#
# current_date = datetime.now().strftime("%d-%m-%Y")
# if (CreatedDate == current_date) and (OrderDate == current_date) and (InvoiceDate == current_date) and (CompletedDate == current_date):
#     print("Date is Correct")
# else:
#     print("Date are Incorrect")

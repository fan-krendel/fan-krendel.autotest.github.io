import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\First test
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account = driver.find_element_by_id("menu-item-50").click()
time.sleep(3)
email_reg = driver.find_element_by_id("reg_email").send_keys("stive@gmail.com")
pass_reg = driver.find_element_by_id("reg_password").send_keys("1stivemailtest!$")
time.sleep(3)
reg_btn = driver.find_element_by_name("register").click()
time.sleep(3)
driver.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Second test
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account_log = driver.find_element_by_id("menu-item-50").click()
time.sleep(3)
email_log = driver.find_element_by_id("username").send_keys("stive@gmail.com")
pass_log = driver.find_element_by_id("password").send_keys("1stivemailtest!$")
time.sleep(3)
log_btn = driver.find_element_by_name("login").click()
time.sleep(3)

logout = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")
check_log = logout.text
assert check_log == "Logout"
time.sleep(3)
driver.quit()
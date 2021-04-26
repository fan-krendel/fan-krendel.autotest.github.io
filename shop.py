import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\First test
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account_log = driver.find_element_by_id("menu-item-50").click()
time.sleep(3)
email_log = driver.find_element_by_id("username").send_keys("stive@gmail.com")
pass_log = driver.find_element_by_id("password").send_keys("1stivemailtest!$")
time.sleep(3)
log_btn = driver.find_element_by_name("login").click()
time.sleep(3)

shop_btn = driver.find_element_by_id("menu-item-40").click()
time.sleep(3)

html_book = driver.find_element_by_class_name("post-181").click()
time.sleep(3)

book_h1 = driver.find_element_by_class_name("entry-title")
check_h1 = book_h1.text
assert check_h1 == "HTML5 Forms"
time.sleep(3)
driver.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Second test
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account_log1 = driver.find_element_by_id("menu-item-50").click()
time.sleep(3)
email_log1 = driver.find_element_by_id("username").send_keys("stive@gmail.com")
pass_log1 = driver.find_element_by_id("password").send_keys("1stivemailtest!$")
time.sleep(3)
log_btn1 = driver.find_element_by_name("login").click()
time.sleep(3)

shop_btn1 = driver.find_element_by_id("menu-item-40").click()
time.sleep(3)

html_btn = driver.find_element_by_css_selector(".cat-item-19>a").click()
time.sleep(3)

items_html = driver.find_elements_by_class_name("product")

assert len(items_html) == 3
time.sleep(3)
driver.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Third test
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account_log = driver.find_element_by_id("menu-item-50").click()
time.sleep(3)
email_log = driver.find_element_by_id("username").send_keys("stive@gmail.com")
pass_log = driver.find_element_by_id("password").send_keys("1stivemailtest!$")
time.sleep(3)
log_btn = driver.find_element_by_name("login").click()
time.sleep(3)

shop_btn = driver.find_element_by_id("menu-item-40").click()
time.sleep(3)

order = driver.find_element_by_css_selector("option:nth-child(1)")
order_by = order.get_attribute("value")
assert order_by == "menu_order"
time.sleep(3)

sort_by = driver.find_element_by_name("orderby")
select = Select(sort_by)
select.select_by_value("price-desc")
time.sleep(3)

sort_by = driver.find_element_by_css_selector("option:nth-child(6)")
sort = sort_by.get_attribute("value")
assert sort == "price-desc"
time.sleep(3)
driver.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Fourth test
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")
time.sleep(3)
account_log = driver.find_element_by_id("menu-item-50").click()
time.sleep(5)
email_log = driver.find_element_by_id("username").send_keys("stive@gmail.com")
pass_log = driver.find_element_by_id("password").send_keys("1stivemailtest!$")
time.sleep(3)
log_btn = driver.find_element_by_name("login").click()
time.sleep(3)

shop_btn = driver.find_element_by_id("menu-item-40").click()
time.sleep(5)

android_book = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".post-169.product")))
android_book.click()
time.sleep(5)

old_price = driver.find_element_by_tag_name("del")
text_old = old_price.text
assert text_old == "₹600.00"

new_price = driver.find_element_by_css_selector("[class='price']>ins")
text_new = new_price.text
assert text_new == "₹450.00"

img_click = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".zoom")))
img_click.click()

img_close = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
img_close.click()
time.sleep(3)
driver.quit()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Fifth test

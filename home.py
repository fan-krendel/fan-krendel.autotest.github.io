import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
ruby_btn = driver.find_element_by_partial_link_text("Ruby").click()
time.sleep(3)
rev_btn = driver.find_element_by_class_name("reviews_tab").click()
time.sleep(3)
star_btn = driver.find_element_by_class_name("star-5").click()
review = driver.find_element_by_id("comment").send_keys("Nice book!")
name = driver.find_element_by_id("author").send_keys("Stive")
email = driver.find_element_by_id("email").send_keys("stive@gmail.com")
time.sleep(3)
submit_btn = driver.find_element_by_id("submit").click()
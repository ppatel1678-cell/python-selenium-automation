from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)
driver.find_element(By.CSS_SELECTOR,'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'#ap_email')
driver.find_element(By.CSS_SELECTOR,'#ap_password')
driver.find_element(By.CSS_SELECTOR,'div.a-alert-content')
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'#continue')
driver.find_element(By.CSS_SELECTOR,"[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?i']")
driver.find_element(By.CSS_SELECTOR,"a.a-link-emphasis")

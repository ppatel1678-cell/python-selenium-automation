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

# open the url
driver.get('https://www.target.com')

sleep(2)
#verify if sign in button works
driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
sleep(2)

#verify if side navigation "sign in" button works
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()
sleep(2)

#SignIn button is shown
driver.find_element(By.ID,"login").click()












from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com')
    sleep(3)


@when('Click on cart button')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[data-test='@web/CartLink']").click()
    sleep(5)


@then('Your cart is empty message displays')
def message_empty(context):
    context.driver.find_element(By.CSS_SELECTOR,"h1.sc-fe064f5c-0")
    sleep(3)


@when('Click on sign on button')
def click_sign(context):
    context.driver.find_element(By.CSS_SELECTOR,"span.sc-58ad44c0-3").click()
    sleep(3)


@when('Click sign in from side navigation')
def message_signin(context):
    context.driver.find_element(By.CSS_SELECTOR,"button[data-test='accountNav-signIn']").click()
    sleep(3)

@then('Sign in message displays')
def sign_in_message(context):
    context.driver.find_element(By.CSS_SELECTOR,".sc-fe064f5c-0")


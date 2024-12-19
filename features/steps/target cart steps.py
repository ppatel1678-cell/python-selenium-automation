from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on product of choice')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[src='https://target.scene7.com/is/image/Target/GUEST_b99b87c5-8b59-42ce-a51e-336ccc789a01']").click()


@when('Click on add to cart button')
def click_add(context):
    context.driver.find_element(By.CSS_SELECTOR,"[aria-label='Add to cart for The Official Taylor Swift | The Eras Tour Book (Target Exclusive)']")


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('Verify product is in cart')
def verify_product(context):

    expected_result = '$39.99 subtotal'
    actual_cart = context.driver.find_element(By.XPATH, "//span[text()='$39.99 subtotal']").text

    assert expected_result == actual_cart,f'{expected_result} is not in {actual_cart}'




from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com')
sleep(3)


@when('search for a {product}')
def search_product(context,product):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/Search/SearchInput']").click()
sleep(5)


@then('verify search for results are shown for {product}')
def results_for_product(context,product):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text

    assert product in actual_result,f'Expected result {product} not in {actual_result}'
sleep(3)








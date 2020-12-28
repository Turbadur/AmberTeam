from behave import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="C:chromedriver.exe")  # inicjalizacja zmiennej driver


@given('browser open with exercise 1')
def open_exercise1(context):
    driver.get('https://antycaptcha.amberteam.pl')
    driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/a').click()
    driver.maximize_window()
    assert context.failed is False


@when('exercise 1 is solved')
def exercise1_solving(context):
    step1 = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[2]/code').text
    button1 = driver.find_element_by_id('btnButton1')
    button2 = driver.find_element_by_id('btnButton2')
    if step1 == 'B1':
        button1.click()
    else:
        button2.click()

    step2 = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/code').text
    if step2 == 'B1':
        button1.click()
    else:
        button2.click()

    step3 = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td[2]/code').text
    if step3 == 'B1':
        button1.click()
    else:
        button2.click()

    driver.find_element_by_id('solution').click()
    assert context.failed is False


@then('check exercise 1 answer')
def exercise1_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 2')
def open_exercise2(context):
    driver.get('https://antycaptcha.amberteam.pl')
    driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/a').click()
    assert context.failed is False


@when('exercise 2 is solved')
def exercise2_solving(context):
    text = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[2]/code[1]').text
    text_line = driver.find_element_by_id('t14')
    text_line.clear()
    text_line.send_keys(text)
    driver.find_element_by_id('btnButton1').click()
    driver.find_element_by_id('solution').click()
    assert context.failed is False


@then('check exercise 2 answer')
def exercise2_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 3')
def open_exercise3(context):
    driver.get('https://antycaptcha.amberteam.pl')
    driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/a').click()
    assert context.failed is False


@when('exercise 3 is solved')
def exercise3_solving(context):
    option = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[3]/code').text
    option_value = option[4:]
    select = Select(driver.find_element_by_id('s13'))
    select.select_by_value(option_value)
    driver.find_element_by_id('solution').click()
    assert context.failed is False


@then('check exercise 3 answer')
def exercise3_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 4')
def open_exercise4(context):
    driver.get('https://antycaptcha.amberteam.pl')
    driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/a').click()
    assert context.failed is False


@when('exercise 4 is solved')
def exercise4_solving(context):
    steps = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td[3]/code').text
    step1v = 'v' + steps[1] + '0'
    step2v = 'v' + steps[4] + '1'
    step3v = 'v' + steps[7] + '2'
    step4v = 'v' + steps[10] + '3'
    driver.find_element_by_xpath("//input[@value='" + step1v + "']").click()
    driver.find_element_by_xpath("//input[@value='" + step2v + "']").click()
    driver.find_element_by_xpath("//input[@value='" + step3v + "']").click()
    driver.find_element_by_xpath("//input[@value='" + step4v + "']").click()
    driver.find_element_by_id('solution').click()
    assert context.failed is False


@then('check exercise 4 answer')
def exercise4_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True
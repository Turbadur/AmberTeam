from behave import *
from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="C:/Users/Dzieci/PycharmProjects/AmberTeam/driver/chromedriver.exe")  # inicjalizacja zmiennej driver


@given('browser open with exercise 1')
def open_exercise1(context):
    driver.get('https://antycaptcha.amberteam.pl/exercises/exercise1?seed=ba1a91d4-9c2a-48e3-a58b-73d9a48c58cd')
    driver.maximize_window()
    assert context.failed is False


@when('exercise 1 is solved')
def exercise1_solving(context):
    button1 = driver.find_element_by_id('btnButton1')
    button1.click()
    time.sleep(1)
    button2 = driver.find_element_by_id('btnButton2')
    button2.click()
    time.sleep(1)
    button1.click()
    driver.find_element_by_id('solution').click()
    time.sleep(1)
    assert context.failed is False


@then('check exercise 1 answer')
def exercise1_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 2')
def open_exercise2(context):
    driver.get('https://antycaptcha.amberteam.pl/exercises/exercise2?seed=ba1a91d4-9c2a-48e3-a58b-73d9a48c58cd')
    assert context.failed is False


@when('exercise 2 is solved')
def exercise2_solving(context):
    text = driver.find_element_by_css_selector('body > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > '
                                               'code:nth-child(1)').text
    text_line = driver.find_element_by_id('t14')
    text_line.clear()
    text_line.send_keys(text)
    driver.find_element_by_id('btnButton1').click()
    time.sleep(1)
    driver.find_element_by_id('solution').click()
    time.sleep(1)
    assert context.failed is False


@then('check exercise 2 answer')
def exercise2_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 3')
def open_exercise3(context):
    driver.get('https://antycaptcha.amberteam.pl/exercises/exercise3?seed=ba1a91d4-9c2a-48e3-a58b-73d9a48c58cd')
    assert context.failed is False


@when('exercise 3 is solved')
def exercise3_solving(context):
    driver.find_element_by_css_selector('#s13 > option:nth-child(2)').click()
    time.sleep(1)
    driver.find_element_by_id('solution').click()
    time.sleep(1)
    assert context.failed is False


@then('check exercise 3 answer')
def exercise3_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True


@given('browser open with exercise 4')
def open_exercise4(context):
    driver.get('https://antycaptcha.amberteam.pl/exercises/exercise4?seed=ba1a91d4-9c2a-48e3-a58b-73d9a48c58cd')
    assert context.failed is False


@when('exercise 4 is solved')
def exercise4_solving(context):
    driver.find_element_by_css_selector('body > div > div:nth-child(4) > input[type=radio]:nth-child(2)').click()
    driver.find_element_by_css_selector('body > div > div:nth-child(5) > input[type=radio]:nth-child(14)').click()
    driver.find_element_by_css_selector('body > div > div:nth-child(6) > input[type=radio]:nth-child(4)').click()
    driver.find_element_by_css_selector('body > div > div:nth-child(7) > input[type=radio]:nth-child(12)').click()
    driver.find_element_by_id('solution').click()
    time.sleep(1)
    assert context.failed is False


@then('check exercise 4 answer')
def exercise4_answer_check(context):
    answer = driver.find_element_by_class_name('wrap').text
    if answer == 'OK. Good answer':
        answer = True
    assert answer is True



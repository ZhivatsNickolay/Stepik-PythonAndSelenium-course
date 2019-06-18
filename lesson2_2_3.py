from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def summary(a, b):
    return str(a + b)

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

number_one = browser.find_element_by_id('num1')
number_one_value = int(number_one.text)

number_two = browser.find_element_by_id('num2')
number_two_value = int(number_two.text)

sum_of = summary(number_one_value, number_two_value)

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(sum_of)

confirm_button = browser.find_element_by_css_selector('.btn')
confirm_button.click()


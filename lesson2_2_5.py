from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

number = browser.find_element_by_css_selector('.form-group .nowrap:nth-child(2)')
number_value = number.text
needed_answer = calc(number_value)

answer = browser.find_element_by_css_selector('.form-group .form-control')
answer.send_keys(needed_answer)

i_robot = browser.find_element_by_css_selector('#robotCheckbox')
i_robot.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

robot_rules = browser.find_element_by_css_selector("#robotsRule")
robot_rules.click()

button.click()
assert True
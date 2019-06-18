from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('.form-group  .nowrap:nth-child(2)')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)
i_am_robot = browser.find_element_by_css_selector('#robotCheckbox')
i_am_robot.click()
robots_rule = browser.find_element_by_css_selector('#robotsRule')
robots_rule.click()
submit_button = browser.find_element_by_css_selector('.btn')
submit_button.click()
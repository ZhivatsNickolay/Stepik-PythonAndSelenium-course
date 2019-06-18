from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

chest_element = browser.find_element_by_css_selector('#treasure')
treasure_in_chest = chest_element.get_attribute('valuex')
calculated = calc(treasure_in_chest)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(calculated)
i_am_robot = browser.find_element_by_css_selector('#robotCheckbox')
i_am_robot.click()
robots_rule = browser.find_element_by_css_selector('#robotsRule')
robots_rule.click()
submit_button = browser.find_element_by_css_selector('.btn')
submit_button.click()
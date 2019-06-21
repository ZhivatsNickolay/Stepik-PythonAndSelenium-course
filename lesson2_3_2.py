from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = ('http://suninjuly.github.io/alert_accept.html')
browser = webdriver.Chrome()
browser.get(link)

magic_trip = browser.find_element_by_css_selector(".container .btn")
magic_trip.click()

want_to_alert = browser.switch_to.alert
want_to_alert.accept()

value_element = browser.find_element_by_css_selector("#input_value")
value = value_element.text

answer = calc(value)

answer_input = browser.find_element_by_css_selector(".form-group .form-control")
answer_input.send_keys(answer)

submit_button = browser.find_element_by_css_selector(".btn")
submit_button.click()

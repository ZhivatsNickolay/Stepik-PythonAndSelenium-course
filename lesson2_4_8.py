from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))
#assert price == '10000 RUR'

button = browser.find_element_by_id("book")
button.click()

value_element = browser.find_element_by_css_selector("#input_value")
value = value_element.text

answer = calc(value)

answer_input = browser.find_element_by_css_selector(
    ".form-group .form-control")
answer_input.send_keys(answer)

submit_button = browser.find_element_by_id("solve")
submit_button.click()

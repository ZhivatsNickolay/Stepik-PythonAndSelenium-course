from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_css_selector('.form-group [name = "firstname"]')
firstname.send_keys('Nik')

lastname = browser.find_element_by_css_selector('.form-group [name = "lastname"]')
lastname.send_keys('Zhiv')

email = browser.find_element_by_css_selector('.form-group [name = "email"]')
email.send_keys('aaa@bbb.com')

send_file = browser.find_element_by_css_selector('#file')
send_file.send_keys(file_path)

confirm_button = browser.find_element_by_css_selector('.btn')
confirm_button.click()
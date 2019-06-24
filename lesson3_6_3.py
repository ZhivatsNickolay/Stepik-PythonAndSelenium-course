import pytest
from selenium import webdriver
import time
import math

@pytest.mark.parametrize('page_link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_different_links_same_answer(page_link):
    answer = math.log(int(time.time()))
    link = page_link
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    input_area = browser.find_element_by_css_selector('.textarea[placeholder = "Type your answer here..."]')
    input_area.send_keys(str(answer))

    confirm_button = browser.find_element_by_css_selector(".submit-submission")
    confirm_button.click()

    answer_result = browser.find_element_by_css_selector(".smart-hints__feedback").text
    #actual_result = answer_result.text

    assert answer_result == "Correct!", f"Актуальный результат: {answer_result}"


#@pytest.mark.parametrize('page_link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])

#def test_open_different_links(browser, page_link):
    #answer_input = browser.find_element_by_css_selector('.textarea').send_keys(answer)
    

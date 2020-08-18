from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("[id=\"input_value\"]")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

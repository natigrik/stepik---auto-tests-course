from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_css_selector("[id=\"book\"]")
    button.click()

    x_element = browser.find_element_by_css_selector("[id=\"input_value\"]")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector("[id=\"solve\"]")
    button2.click()


finally:
    time.sleep(10)
    browser.quit()

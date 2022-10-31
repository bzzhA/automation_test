from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip as pc

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

click_btn = browser.find_element(By.CLASS_NAME, 'btn')
click_btn.click()

window_alert = browser.switch_to.alert
window_alert.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

find_x = browser.find_element(By.ID, 'input_value').text
x = find_x
y = calc(x)
send_answer = browser.find_element(By.ID, 'answer')
send_answer.send_keys(y)

click_submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
click_submit.click()

pc.copy(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(5)
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import pyperclip as pc

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

get_rent = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
browser.find_element(By.ID, 'book').click()

btn_click = browser.find_element(By.ID, 'book')
browser.execute_script("arguments[0].scrollIntoView(true);", btn_click)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

find_x = browser.find_element(By.ID, 'input_value').text
x = find_x
y = calc(x)
send_answer = browser.find_element(By.ID, 'answer')
send_answer.send_keys(y)
browser.find_element(By.ID, 'solve').click()

pc.copy(browser.switch_to.alert.text.split(': ')[-1])

time.sleep(5)
browser.quit()
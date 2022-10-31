from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, 'input.first')
    input_first_name.send_keys('Name')
    input_last_name = browser.find_element(By.CSS_SELECTOR, 'input.second')
    input_last_name.send_keys('Surname')
    input_email = browser.find_element(By.CSS_SELECTOR, 'input.third')
    input_email.send_keys('namesurname@gmail.com')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    find_text = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = find_text.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
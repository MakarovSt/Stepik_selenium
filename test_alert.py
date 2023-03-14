from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button1.click()
    # подтверждаем всплывающее окно
    confirm = browser.switch_to.alert
    confirm.accept()
    # решаем пример по формуле
    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    y = calc(x)
    # вставляем ответ и жмем сабмит
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:

# успеваем скопировать код за 5 секунд
    time.sleep(5)
# закрываем браузер после всех манипуляций
    browser.quit()
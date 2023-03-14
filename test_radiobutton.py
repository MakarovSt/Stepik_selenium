from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    # ищем на стринце значение х
    x_element = browser.find_element(By.ID, "treasure")
    x_value = x_element.get_attribute("valuex")
    x = x_value
    # подставляем значение в формулу в начале кода
    y = calc(x)
    # ищем поле для ответа
    y_element = browser.find_element (By.ID, "answer")
    # вставляем в поле для ответа полученное значение
    y_element.send_keys(y)
    # Кликаем на чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    # кликаем на радиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    # кликаем на сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
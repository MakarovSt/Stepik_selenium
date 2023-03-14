from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    # ищем на странице число 1
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    # переводим значение в текстовый формат
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    # складываем полученные значения, переведя в int
    z = int(x) + int(y)
    # открываем выпадающий список
    input1 = browser.find_element(By.CSS_SELECTOR, "select#dropdown")
    # пуляем туда значение суммы двух чисел найденных ранее
    input1.send_keys(z)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
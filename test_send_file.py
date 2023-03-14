from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # Находим поле и вводим имя
    first_name = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[1]")
    first_name.send_keys("Станислав")
    # находим поле и вводим фамилию
    second_name = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[2]")
    second_name.send_keys("Макаров")
    # находим поле и вводим емейл
    e_mail = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[3]")
    e_mail.send_keys("mail@mail.ru")
    # код для того что бы показать что файл txt лежи в той же директории что и скрипт
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test_file.txt"
    file_path = os.path.join(current_dir, file_name)
    # загружаем этот файл на сайт
    upload = browser.find_element(By.XPATH, "//*[@id='file']")
    upload.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:

# успеваем скопировать код за 5 секунд
    time.sleep(5)
# закрываем браузер после всех манипуляций
    browser.quit()
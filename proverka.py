from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер и переходим на сайт
driver = webdriver.Chrome()
driver.get("https://piter-online.net/")


search_box = driver.find_element(By.ID, "id_поля_ввода")
if search_box is not None:
    search_box.send_keys("Тестовая линия, дом 1")
else:
    print("Элемент не найден")

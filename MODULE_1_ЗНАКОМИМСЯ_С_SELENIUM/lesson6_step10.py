from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    # 1 Вариант решения через CSS SELECTOR
    input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    input3.send_keys("oxo.exe@yandex.ru")

    # 2 Вариант решения через XPATH
    #input1 = browser.find_element(By.XPATH, "//div[contains(@class, 'first_block')]//input[contains(@class, 'first')]")
    #input1.send_keys("Ivan")
    #time.sleep(2)
    #input2 = browser.find_element(By.XPATH, "//div[contains(@class, 'first_block')]//input[contains(@class, 'second')]")
    #input2.send_keys("Petrov")
    #time.sleep(2)
    #input3 = browser.find_element(By.XPATH, "//div[contains(@class, 'first_block')]//input[contains(@class, 'third')]")
    #input3.send_keys("Smolensk@ivan.ru")
    #time.sleep(2)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
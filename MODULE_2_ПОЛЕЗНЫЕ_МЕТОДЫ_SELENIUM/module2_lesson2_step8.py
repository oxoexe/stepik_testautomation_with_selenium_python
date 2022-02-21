from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'empty_txt_file.txt')           # добавляем к этому пути имя файла 

try: 

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys("Joka")
  
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys("Boka")
    
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys("email@email.com")
    
    input4 = browser.find_element(By.CSS_SELECTOR, 'input[name="file"]')
    input4.send_keys(file_path)
    
    
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
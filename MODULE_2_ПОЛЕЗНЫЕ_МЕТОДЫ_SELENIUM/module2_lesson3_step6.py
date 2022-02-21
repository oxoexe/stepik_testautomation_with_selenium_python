from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    # указываем номер окна
    new_window = browser.window_handles[1]
    # переключаемся на необходимое окно
    browser.switch_to.window(new_window)
    
    
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
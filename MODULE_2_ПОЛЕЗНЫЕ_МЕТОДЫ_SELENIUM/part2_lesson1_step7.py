from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    x_element = browser.find_element(By.ID, "treasure")
    chest_hidden_number = x_element.get_attribute("valuex")
    y = calc(chest_hidden_number)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)


    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
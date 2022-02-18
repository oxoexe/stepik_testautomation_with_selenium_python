from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


try: 

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    print(x)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)
    print(y)
    
    sum_xy = x + y
    print(sum_xy)

    css_sel = "[value='" + str(sum_xy) + "']"

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(css_sel).click()
    #browser.find_element_by_tag_name("select").click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
import pytest
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_registration_report(url: str) -> str:
    text = "text"
    with webdriver.Chrome() as browser:
        browser.get(url)
        elements = (
            browser.find_element(By.CSS_SELECTOR, ".first.form-control[required='']"),
            browser.find_element(By.CSS_SELECTOR, ".second.form-control[required='']"),
            browser.find_element(By.CSS_SELECTOR, ".third.form-control[required='']")
        )

        for element in elements:
            element.send_keys(text)

        browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
        time.sleep(2)

        return browser.find_element(By.CSS_SELECTOR, "h1").text


class test_TextMyTest(unittest.TestCase):
    url1 = "http://suninjuly.github.io/registration1.html"
    url2 = "http://suninjuly.github.io/registration2.html"
    expected_text = "Congratulations! You have successfully registered! Поздравляем! Вы успешно зарегистировались!"

    def test_url1(self):
        result_text = get_registration_report(self.url1)
        assert result_text in self.expected_text, \
            f"Oops! {self.expected_text} was expected, got {result_text} instead"

    def test_url2(self):
        result_text = get_registration_report(self.url2)
        assert result_text in self.expected_text, \
            f"Oops! {self.expected_text} was expected, got {result_text} instead"

if __name__ == "__main__":
    pytest.main()
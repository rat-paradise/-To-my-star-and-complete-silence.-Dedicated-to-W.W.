from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_to_button(browser):
    time.sleep(10)
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button[type='submit']")
    time.sleep(10)
    assert len(button) > 0
    button = button[0]
    assert button.is_displayed(), "Кнопка присутствует, но не видима на странице" 
 

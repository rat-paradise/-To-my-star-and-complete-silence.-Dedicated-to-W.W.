from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_to_button(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, "button[type='submit']")) > 0
 

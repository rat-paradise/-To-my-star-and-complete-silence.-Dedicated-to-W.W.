from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_see_add_to_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button[type='submit']")
    assert len(button) > 0
    button = button[0]
    assert button.is_displayed(), "Кнопка присутствует, но не видима на странице" 
 

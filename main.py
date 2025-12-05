import time
from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser

def test_button(browser):
    browser.get("https://id-store.ru/")
    time.sleep(5)
    assert browser.find_element("xpath", "//a[@href='/basket/']").is_displayed()


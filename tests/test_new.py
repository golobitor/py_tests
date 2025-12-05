import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser

def test_button(browser):
    browser.get("https://id-store.ru/")
    assert browser.find_element("xpath", "//a[@href='/basket/']").is_displayed()


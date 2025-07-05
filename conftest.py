import pytest
from selenium import webdriver
from data import main_page_url

@pytest.fixture
def driver_main_page():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(main_page_url)
    yield driver
    driver.quit()


# file to collect all fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from config import Links
# from tests.test_data import TestData
# from pages.start_page import StartPage


@pytest.fixture(autouse=True)
def browser():
    """fixture to open Chrome browser before running tests, and to quit browser after that;
    automatically & implicitly started (by "autouse" parameter)
    for every test where this fixture is mentioned as a parameter of test"""
    browser = webdriver.Chrome(service=Service(executable_path='.chromedriver'))
    yield browser
    browser.quit()


# @pytest.fixture()
# def login(browser):
#     """fixture to login in with /// credentials;
#     starts from opening login page and finishes ///"""
#     login_page = LoginPage(browser, Links.login_page)
#     login_page.open_page()
#     login_page.login(TestData.valid_login_credentials)








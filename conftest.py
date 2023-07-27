# file to collect all fixtures

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Links
from tests.test_data import TestData
from pages.start_page import StartPage
import datetime
import os


@pytest.fixture(autouse=True)
def browser():
    """fixture to open Chrome browser before running tests, and to quit browser after that;
    automatically & implicitly started (by "autouse" parameter)
    for every test where this fixture is mentioned as a parameter of test"""
    browser = webdriver.Chrome()
    yield browser
    filename = os.path.abspath(os.getcwd()) + f'/{datetime.datetime.now()}.png'
    print(filename)
    browser.save_screenshot(filename)
    browser.quit()


@pytest.fixture()
def msk_login(browser):
    """fixture to login in as a user registered with MSK phone number;
    starts from opening start page and finishes on My orders page"""
    start_page = StartPage(browser, Links.start_page)
    start_page.open_page()
    start_page.login(TestData.valid_login_credentials_msk_user[0])


@pytest.fixture()
def spb_login(browser):
    """fixture to login in as a user registered with SPB phone number;
    starts from opening start page and finishes on My orders page"""
    start_page = StartPage(browser, Links.start_page)
    start_page.open_page()
    start_page.login(TestData.valid_login_credentials_spb_user[0])

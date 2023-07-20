# file to collect test created for start page

import pytest
from tests.test_data import TestData
from pages.start_page import StartPage
from config import Links
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStartPage:

    @pytest.mark.parametrize("login_credentials", TestData.valid_login_credentials_msk_user)
    def test_valid_login(self, browser, login_credentials):
        start_page = StartPage(browser, Links.start_page)
        start_page.open_page()
        start_page.login(login_credentials)
        wait = WebDriverWait(browser, 10)
        assert (wait.until(EC.url_to_be(Links.my_orders_page)))

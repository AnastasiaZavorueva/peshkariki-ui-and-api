#  basic class for every page in the project
#  methods of base page will be inherited by every child class (=any page of the website that extends BasePage)
# ! we should provide browser and URL as parameters when creating an instance of that class

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import allure


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @allure.step(f"Open specific page")
    def open_page(self):
        self.browser.get(self.url)

    @allure.step("Clear input field selected (from default value)")
    def clear_text_field(self, element):
        while (element.get_attribute("value") == "") is False:
            element.send_keys(Keys.BACKSPACE)

    @allure.step("Get URL of current page")
    def get_current_url(self):
        time.sleep(1)
        return self.browser.current_url

    def scroll_page_to_the_bottom(self):
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


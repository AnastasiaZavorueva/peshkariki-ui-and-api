#  basic class for every page in the project
#  methods of base page will be inherited by every child class (=any page of the website that extends BasePage)
# ! we should provide browser and URL as parameters when creating an instance of that class

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def clear_text_field(self, element):
        while (element.get_attribute("value") == "") is False:
            element.send_keys(Keys.BACKSPACE)


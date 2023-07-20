from pages.base_page import BasePage
from locators.start_page_locators import StartPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure


class StartPage(BasePage):

    @allure.step("On the start page log in with credentials provided")
    def login(self, login_credentials):
        wait = WebDriverWait(self.browser, 10)

        open_login_window_button = wait.until(ec.visibility_of_element_located(StartPageLocators.OPEN_LOGIN_WINDOW_BUTTON))
        open_login_window_button.click()

        phone_or_email_field = wait.until(ec.visibility_of_element_located(StartPageLocators.PHONE_OR_EMAIL_FIELD))
        password_field = wait.until(ec.visibility_of_element_located(StartPageLocators.PASSWORD_FIELD))
        # method keys() is used to retrieve all keys from some dictionary
        #  where key - is phone/email, and value - password for login
        for login in login_credentials.keys():
            phone_or_email_field.send_keys(login)
            password_field.send_keys(login_credentials[login])

        login_submit_button = self.browser.find_element(*StartPageLocators.SUBMIT_LOGIN_BUTTON)
        login_submit_button.click()


    @allure.step("From the start page navigate to 'Восстановление пароля'/'Password recovery'form")
    def navigate_to_forgot_password(self):
        wait = WebDriverWait(self.browser, 10)
        open_login_window_button = wait.until(ec.visibility_of_element_located(StartPageLocators.OPEN_LOGIN_WINDOW_BUTTON))
        open_login_window_button.click()

        forgot_password_link = wait.until(ec.visibility_of_element_located(StartPageLocators.FORGOT_PASSWORD_LINK))
        forgot_password_link.click()










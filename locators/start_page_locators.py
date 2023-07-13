from selenium.webdriver.common.by import By


class StartPageLocators:
    OPEN_LOGIN_WINDOW_BUTTON = (By.XPATH, "//a[@data-modal='auth']")
    CLOSE_LOGIN_WINDOW_BUTTON = (By.XPATH, "//i[@class='close']")

    # to use these locators login window should be opened (using locator above)
    PHONE_OR_EMAIL_FIELD = (By.XPATH, "//input[@name='phone']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[@class='send btn-single']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@class='forgot-password-btn']")


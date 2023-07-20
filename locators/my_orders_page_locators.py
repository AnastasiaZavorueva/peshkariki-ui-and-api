from selenium.webdriver.common.by import By


class MyOrdersPageLocators:
    CREATE_NEW_ORDER_BUTTON = (By.XPATH, "//header//a[contains(text(), 'Создать заказ')]")
    GOODS_AND_DOCS_DELIVERY_BUTTON = (By.XPATH, "//div[contains(text(), 'Доставка')]")
    GOODS_REDEMPTION_BUTTON = (By.XPATH, "//div[contains(text(), 'Выкуп товара')]")

    ALL_NUMBERS_OF_ACTIVE_ORDERS = (By.XPATH, "//li[@class='order']//h5/a")
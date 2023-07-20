from selenium.webdriver.common.by import By


class MyOrdersPageLocators:
    CREATE_NEW_ORDER_BUTTON = (By.XPATH, "//header//a[contains(text(), 'Создать заказ')]")
    GOODS_AND_DOCS_DELIVERY_BUTTON = (By.XPATH, "//div[contains(text(), 'Доставка')]")
    GOODS_REDEMPTION_BUTTON = (By.XPATH, "//div[contains(text(), 'Выкуп товара')]")

    ALL_NUMBERS_OF_ACTIVE_ORDERS = (By.XPATH, "//li[@class='order']//h5/a")
    ALL_CARDS_OF_ACTIVE_ORDERS = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order']")

    # the next locators are used to get data from specific order (that should be located before that)
    ORDER_NUMBER_SHOWN = (By.XPATH, "//h5/a")
    ADDRESSES_IN_ORDER_SHOWN = (By.XPATH, "//div[@class='order-data']//span[@class='point-place']") # this locator returns 2 elements, first (under index 0) belongs to sender_address, while the second (under index 1) belongs to sender_address
    WHAT_TO_DELIVER_SHOWN = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order']//li[contains(text(), 'Товар:')]")
    TOTAL_WEIGHT_SHOWN = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order']//li[contains(text(), 'Масса:')]")
    TOTAL_VALUE = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order']//li[contains(text(), 'Цена:')]")
from selenium.webdriver.common.by import By


class MyOrdersPageLocators:
    CREATE_NEW_ORDER_BUTTON = (By.XPATH, "")
    GOODS_AND_DOCS_DELIVERY_BUTTON = (By.XPATH, "//div[contains(text(), 'Доставка')]")
    GOODS_REDEMPTION_BUTTON = (By.XPATH, "//div[contains(text(), 'Выкуп товара')]")

    ALL_NUMBERS_OF_ACTIVE_ORDERS = (By.XPATH, "//li[@class='order'][not(@class='canceled')]//h5/a")
    ALL_CARDS_OF_ACTIVE_ORDERS = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order'][not(@class='canceled')]")

    ALL_NUMBERS_OF_CANCELED_ORDERS = (By.XPATH, "//li[@class='order canceled']//h5/a")
    ALL_CARDS_OF_CANCELED_ORDERS = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order canceled']")

    # the next 2 locators used to get both activated and canceled orders
    ALL_NUMBERS_OF_ALL_ORDERS = (By.XPATH, "//li[@class='order' or @class='order canceled']//h5/a")
    ALL_CARDS_OF_ALL_ORDERS = (By.XPATH, "//ul[@class='main-orders-list']//li[@class='order' or @class='order canceled']")

    # the next locators are used to get data from specific order (that should be located before that)
    ORDER_NUMBER_SHOWN = (By.XPATH, ".//h5/a")
    ADDRESSES_IN_ORDER_SHOWN = (By.XPATH, ".//div[@class='order-data']//span[@class='point-place']")  # this locator returns 2 elements, first (under index 0) belongs to sender_address, while the second (under index 1) belongs to sender_address
    WHAT_TO_DELIVER_SHOWN = (By.XPATH, ".//li[contains(text(), 'Товар:')]")
    TOTAL_WEIGHT_SHOWN = (By.XPATH, ".//li[contains(text(), 'Масса:')]")
    TOTAL_VALUE_SHOWN = (By.XPATH, ".//li[contains(text(), 'Цена:')]")
    CANCEL_ORDER_BUTTON = (By.XPATH, ".//div[@class='order-data']//button[contains(text(), 'Отменить')]")
    CANCEL_ORDER_CONFIRMATION_WINDOW = (By.XPATH, ".//div[@class='title']//ancestor::div[@class='modal-content-container']")
    PARCEL_NOT_READY_OPTION_IN_CANCEL_ORDER = (By.XPATH, ".//input[@id = 'Груз не готов']")
    CONFIRM_ORDER_CANCELLATION_BUTTON = (By.XPATH, ".//div[@class='actions']//button[contains(text(), 'Подтвердить')]")

    CANCELED_ORDER_INDICATOR = (By.XPATH, ".//div[@class='order-header']//span[contains(text(), 'Отменен')]")
from selenium.webdriver.common.by import By


class MyOrdersPageLocators:
    CREATE_NEW_ORDER_BUTTON = (By.XPATH, "//header//a[contains(text(), 'Создать заказ')]")
    GOODS_AND_DOCS_DELIVERY_BUTTON = (By.XPATH, "//div[contains(text(), 'Доставка')]")
    GOODS_REDEMPTION_BUTTON = (By.XPATH, "//div[contains(text(), 'Выкуп товара')]")

    ON_FOOT_DELIVERY_TYPE_BUTTON = ""
    PASSENGER_CAR_DELIVERY_TYPE_BUTTON = ""
    # locator for delivery type 'Универсал'
    VAN_DELIVERY_TYPE_BUTTON = ""
    # locator for delivery type 'Газель'
    TRUCK_DELIVERY_TYPE_BUTTON = ""

    SENDER_ADDRESS_FIELD = (By.XPATH, '')
    # elements for the next 3 locators becomes visible only after making some input in the field above
    SENDER_ENTRANCE_FIELD =
    SENDER_FLOOR_FIELD =
    SENDER_APT_OR_OFFICE_FIELD =

    SENDER_PHONE_FIELD =

    DATE_OF_PICK_UP =
    START_TIME_OF_PICK_UP_FIELD =
    END_TIME_OF_PICK_UP_FIELD =

    SENDER_NAME_FIELD =
    COMMENT_TO_SENDER_ADDRESS_FIELD =

    RECIPIENT_ADDRESS_FIELD =
    # elements for the next 3 locators becomes visible only after making some input in the field above
    RECIPIENT_ENTRANCE_FIELD =
    RECIPIENT_FLOOR_FIELD =
    RECIPIENT_APT_OR_OFFICE_FIELD =

    RECIPIENT_PHONE_FIELD =

    DATE_OF_RECEIVING_FIELD =
    START_TIME_OF_RECEIVING_FIELD =
    END_TIME_OF_RECEIVING_FIELD =

    GET_PAYMENT_FOR_GOODS_CHECKBOX =

    RECIPIENT_NAME_FIELD =
    COMMENT_TO_RECIPIENT_ADDRESS_FIELD =

    WHAT_TO_DELIVER_FIELD =
    # the next 4 locators used to fill out the field above by predefined values
    # (either 'Documents/Документы', 'Surprise/Сюрприз', 'Fragile/Хрупкий груз', or 'Huge size/Груз  100 см'
    DOCUMENTS_TYPE =
    SURPRISE_TYPE =
    FRAGILE_TYPE =
    HUGE_SIZE_TYPE =
    # the next locator is used to make any other input in the field
    ANOTHER_TYPE =

    VALUE_FIELD =
    WEIGHT_FIELD =
    QUANTITY =

    # the next locators used only if before checkbox GET_PAYMENT_FOR_GOODS_CHECKBOX was selected
    RETURN_PAYMENT_TO_CARD_OPTION =
    RETURN_PAYMENT_TO_Y_MONEY_OPTION =
    RETURN_MONEY_TO_QIWI_OPTION =


    # the next locators used in the section 'Order Details/Детали заказа'
    PAYMENT_RETURN_EXCEPT_DELIVERY_PRICE_OPTION =
    SENDER_PAYS_BY_CASH_OPTION = (By.XPATH, "//span[contains(text(), 'Отправитель наличными')]/../input")
    RECIPIENT_PAYS_BY_CASH_OPTION = (By.XPATH, "//span[contains(text(), 'Получатель наличными')]/../input")
    ONLINE_PAYMENT_BY_CARD_OPTION =

    PROMOCODE_FIELD = (By.XPATH, "//div[@class='string promocode']")




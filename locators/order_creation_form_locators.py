from selenium.webdriver.common.by import By


class OrderCreationFormLocators:

    DELIVERY_TYPE_BLOCK = (By.XPATH, "//h2[contains(text(), 'тип доставки')]//ancestor::div[@class='order-block-transparent']")
    SENDER_INFO_BLOCK = (By.XPATH, "//h2[contains(text(), 'Отправитель')]//ancestor::div[@class='order-block']")
    RECIPIENT_INFO_BLOCK = (By.XPATH, "//h2[contains(text(), 'Получатель')]//ancestor::div[@class='order-block']")
    ORDER_DETAILS_BLOCK = (By.XPATH, "//h2[contains(text(), 'Детали заказа')]//ancestor::div[@class='order-block']")
    SERVICES_BLOCK = (By.XPATH, "//h2[contains(text(), 'Выберите необходимые услуги')]//ancestor::div[@class='order-block']")


    ON_FOOT_DELIVERY_TYPE_BUTTON = (By.XPATH, "//span[contains(text(), 'Пешком')]/ancestor::button")
    CAR_DELIVERY_TYPE_BUTTON = (By.XPATH, "//span[contains(text(), 'Легковое авто')]/ancestor::button")
    # locator for delivery type 'Универсал'
    VAN_DELIVERY_TYPE_BUTTON = (By.XPATH, "//span[contains(text(), 'Универсал')]/ancestor::button")
    # locator for delivery type 'Газель'
    TRUCK_DELIVERY_TYPE_BUTTON = (By.XPATH, "//span[contains(text(), 'Газель')]/ancestor::button")

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY SENDER_INFO_BLOCK

    SENDER_ADDRESS_FIELD = (By.XPATH, ".//div[@class='input address']")
    # elements for the next 3 locators becomes visible only after making some input in the field above
    SENDER_ENTRANCE_FIELD = (By.XPATH, ".//div[@class='order-input entrance']")
    SENDER_FLOOR_FIELD = (By.XPATH, ".//div[@class='order-input storey']")
    SENDER_APT_OR_OFFICE_FIELD = (By.XPATH, ".//div[@class='order-input apartment']")

    SENDER_PHONE_FIELD = (By.XPATH, ".//input[@type='tel']")

    # the next locator returns select-object, with 7 options to chose inside (including current day and so on)
    DATE_OF_PICK_UP_SELECT = (By.XPATH, ".//div[@class='order-input day']/select")
    # the next locators return select-object
    START_TIME_OF_PICK_UP_FIELD = (By.XPATH, ".//div[@class='order-input time-from']//select")
    END_TIME_OF_PICK_UP_FIELD = (By.XPATH, ".//div[@class='order-input time-to']//select")

    # the next locator is used to expand additional fields in SENDER_INFO_BLOCK
    ADDITIONAL_SENDER_INFO_BUTTON = (By.XPATH, ".//span[contains(text(), '+ Доп. информация')]")

    # the next 2 locators can be used only if the block with additional info was expanded before
    # (by using the locator above)
    SENDER_NAME_FIELD = (By.XPATH, ".//div[@class='order-input contact-name']/input")
    COMMENT_TO_SENDER_ADDRESS_FIELD = (By.XPATH, ".//div[@class='order-input comment']/textarea")

    ###

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY RECIPIENT_INFO_BLOCK

    RECIPIENT_ADDRESS_FIELD = (By.XPATH, ".//div[@class='input address']")
    # elements for the next 3 locators becomes visible only after making some input in the field above
    RECIPIENT_ENTRANCE_FIELD = (By.XPATH, ".//div[@class='order-input entrance']")
    RECIPIENT_FLOOR_FIELD = (By.XPATH, ".//div[@class='order-input storey']")
    RECIPIENT_APT_OR_OFFICE_FIELD = (By.XPATH, ".//div[@class='order-input apartment']")

    RECIPIENT_PHONE_FIELD = (By.XPATH, ".//input[@type='tel']")

    # the next locator returns select-object, with 6 options to chose inside (including current day and so on)
    DATE_OF_RECEIVING_FIELD = (By.XPATH, ".//div[@class='order-input day']/select")
    # the next locators return select-object
    START_TIME_OF_RECEIVING_FIELD = (By.XPATH, ".//div[@class='order-input time-from']//select")
    END_TIME_OF_RECEIVING_FIELD = (By.XPATH, ".//div[@class='order-input time-to']//select")

    GET_PAYMENT_FOR_GOODS_CHECKBOX = (By.XPATH, ".//div[contains(text(), 'Получить наличные за товар')]/ancestor::label//input")

    # the next locator is used to expand additional fields in RECIPIENT_INFO_BLOCK
    ADDITIONAL_RECIPIENT_INFO_BUTTON = (By.XPATH, ".//span[contains(text(), '+ Доп. информация')]")
    # the next 2 locators can be used only if the block with additional info was expanded before
    # (by using the locator above)
    RECIPIENT_NAME_FIELD = (By.XPATH, ".//div[@class='order-input contact-name']/input")
    COMMENT_TO_RECIPIENT_ADDRESS_FIELD = (By.XPATH, ".//div[@class='order-input comment']/textarea")

    WHAT_TO_DELIVER_FIELD = (By.XPATH, ".//div[@class='order-input details-item-name']")
    # the next 4 locators used to fill out the field above by predefined values
    # (it could be either 'Documents/Документы', 'Surprise/Сюрприз', 'Fragile/Хрупкий груз', or 'Huge size/Груз  100 см')
    # (by selecting "Other/Другое" option the input field is just cleared and activated for making input)
    DOCUMENTS_TYPE = (By.XPATH, ".//span[contains(text(), 'Документы')]")
    SURPRISE_TYPE = (By.XPATH, ".//span[contains(text(), 'Сюрприз')]")
    FRAGILE_TYPE = (By.XPATH, ".//span[contains(text(), 'Хрупкий груз')]/ancestor::div[@class='suggestion-btn']")
    HUGE_SIZE_TYPE = (By.XPATH, ".//span[contains(text(), 'Груз >100')]/ancestor::div[@class='suggestion-btn']")
    # the next locator is used to make any other input in the field
    ANOTHER_TYPE = (By.XPATH, ".//span[contains(text(), 'Другое')]/ancestor::div[@class='suggestion-btn']")

    VALUE_FIELD = (By.XPATH, ".//div[@class='cost order-input-wrapper']")
    # the next 2 locators return select-object
    WEIGHT_FIELD = (By.XPATH, ".//div[@class='order-input-wrapper weight']//select")
    QUANTITY = (By.XPATH, ".//div[@class='order-input-wrapper count']//input[@type='number']")

    ###

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY ORDER_DETAILS_INFO_BLOCK

    # the next locators used only if the checkbox GET_PAYMENT_FOR_GOODS_CHECKBOX was selected before in RECIPIENT_INFO_BLOCK
    RETURN_PAYMENT_TO_CARD_OPTION = (By.XPATH, ".//div[@class='pay-type']//input[@id='Банковская карта']")
    RETURN_PAYMENT_TO_Y_MONEY_OPTION = (By.XPATH, ".//div[@class='pay-type']//input[@id='ЮMoney (Я.Деньги)']")
    RETURN_MONEY_TO_QIWI_OPTION = (By.XPATH, ".//div[@class='pay-type']//input[@id='QIWI']")
    CARD_OR_Y_MONEY_OR_QIWI_NUMBER_FIELD = (By.XPATH, ".//div[@class='order-input cardholder']")

    PAYMENT_RETURN_EXCEPT_DELIVERY_PRICE_OPTION = (By.XPATH, ".//span[contains(text(), 'Возврат за минусом доставки')]/../input")
    SENDER_PAYS_BY_CASH_OPTION = (By.XPATH, ".//span[contains(text(), 'Отправитель наличными')]/../input")
    RECIPIENT_PAYS_BY_CASH_OPTION = (By.XPATH, ".//span[contains(text(), 'Получатель наличными')]/../input")
    ONLINE_PAYMENT_BY_CARD_OPTION = (By.XPATH, ".//span[contains(text(), 'Онлайн банковской картой')]/../input")

    PROMOCODE_FIELD = (By.XPATH, "//div[@class='string promocode']")

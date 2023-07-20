from selenium.webdriver.common.by import By


class OrderCreationFormLocators:

    LOCATIONS_OF_DELIVERY_DROPDOWN = (By.XPATH, "//div[@class='select-city']")
    LOCATIONS_OF_DELIVERY_SELECT = (By.XPATH, "//div[@class='select-city']/select")
    # ALL_LOCATIONS_OF_DELIVERY_OPTIONS = "//div[@class='select-city']/select/option/span")

    DELIVERY_TYPE_BLOCK = "//h2[contains(text(), 'тип доставки')]//ancestor::div[@class='order-block-transparent']"
    SENDER_INFO_BLOCK = "//h2[contains(text(), 'Отправитель')]//ancestor::div[@class='order-block']"
    RECIPIENT_INFO_BLOCK = "//h2[contains(text(), 'Получатель')]//ancestor::div[@class='order-block']"
    ORDER_DETAILS_BLOCK = "//h2[contains(text(), 'Детали заказа')]//ancestor::div[@class='order-block']"
    SERVICES_BLOCK = "//h2[contains(text(), 'Выберите необходимые услуги')]//ancestor::div[@class='block-servises']"


    ON_FOOT_DELIVERY_TYPE_BUTTON = (By.XPATH, f"{DELIVERY_TYPE_BLOCK}//span[contains(text(), 'Пешком')]/ancestor::button")
    CAR_DELIVERY_TYPE_BUTTON = (By.XPATH, f"{DELIVERY_TYPE_BLOCK}//span[contains(text(), 'Легковое авто')]/ancestor::button")
    # locator for delivery type 'Универсал'
    VAN_DELIVERY_TYPE_BUTTON = (By.XPATH, f"{DELIVERY_TYPE_BLOCK}//span[contains(text(), 'Универсал')]/ancestor::button")
    # locator for delivery type 'Газель'
    TRUCK_DELIVERY_TYPE_BUTTON = (By.XPATH, f"{DELIVERY_TYPE_BLOCK}//span[contains(text(), 'Газель')]/ancestor::button")

    # the next locator is used to get all addresses shown as suggestions
    # after doing some input into the field of either sender or recipient address
    # (and is used to accept the address input)
    SENDER_ADDRESS_SUGGESTIONS = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='input address']//div[@class='dropdown-item']/span")
    RECIPIENT_ADDRESS_SUGGESTIONS = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='input address']//div[@class='dropdown-item']/span")

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY SENDER_INFO_BLOCK

    SENDER_ADDRESS_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='input address']/input")
    # elements for the next 3 locators becomes visible only after making some input in the field above
    SENDER_ENTRANCE_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input entrance']//input")
    SENDER_FLOOR_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input storey']/input")
    SENDER_APT_OR_OFFICE_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input apartment']/input")

    SENDER_PHONE_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//input[@type='tel']")

    # the next locator returns select-object, with 7 options to chose inside (including current day and so on)
    DATE_OF_PICK_UP_SELECT = (By.XPATH, f"{SENDER_INFO_BLOCK}//select[@id='day']")
    ALL_DATES_OF_PICK_UP_OPTIONS = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input day']/select/option")
    # the next locators return select-object
    START_TIME_OF_PICK_UP_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input time-from']//select")
    END_TIME_OF_PICK_UP_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input time-to']//select")

    # the next locator is used to expand additional fields in SENDER_INFO_BLOCK
    ADDITIONAL_SENDER_INFO_BUTTON = (By.XPATH, f"{SENDER_INFO_BLOCK}//span[contains(text(), 'Доп. информация')]")

    # the next 2 locators can be used only if the block with additional info was expanded before
    # (by using the locator above)
    SENDER_NAME_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input contact-name']/input")
    COMMENT_TO_SENDER_ADDRESS_FIELD = (By.XPATH, f"{SENDER_INFO_BLOCK}//div[@class='order-input comment']/textarea")

    ###

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY RECIPIENT_INFO_BLOCK

    RECIPIENT_ADDRESS_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='input address']/input")
    # elements for the next 3 locators becomes visible only after making some input in the field above
    RECIPIENT_ENTRANCE_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input entrance']/input")
    RECIPIENT_FLOOR_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input storey']/input")
    RECIPIENT_APT_OR_OFFICE_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input apartment']/input")

    RECIPIENT_PHONE_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//input[@type='tel']")

    # the next locator returns select-object, with 6 options to chose inside (including current day and so on)
    DATE_OF_RECEIVING_SELECT = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input day']/select")
    # the next locators return select-object
    START_TIME_OF_RECEIVING_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input time-from']//select")
    END_TIME_OF_RECEIVING_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input time-to']//select")

    GET_PAYMENT_FOR_GOODS_CHECKBOX = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[contains(text(), 'Получить наличные за товар')]/ancestor::label//input")

    # the next locator is used to expand additional fields in RECIPIENT_INFO_BLOCK
    ADDITIONAL_RECIPIENT_INFO_BUTTON = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), '+ Доп. информация')]")
    # the next 2 locators can be used only if the block with additional info was expanded before
    # (by using the locator above)
    RECIPIENT_NAME_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input contact-name']/input")
    COMMENT_TO_RECIPIENT_ADDRESS_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input comment']/textarea")

    WHAT_TO_DELIVER_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input details-item-name']/input")
    # the next 4 locators used to fill out the field above by predefined values
    # (it could be either 'Documents/Документы', 'Surprise/Сюрприз', 'Fragile/Хрупкий груз', or 'Huge size/Груз  100 см')
    # (by selecting "Other/Другое" option the input field is just cleared and activated for making input)
    DOCUMENTS_TYPE = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), 'Документы')]")
    SURPRISE_TYPE = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), 'Сюрприз')]")
    FRAGILE_TYPE = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), 'Хрупкий груз')]/ancestor::div[@class='suggestion-btn']")
    HUGE_SIZE_TYPE = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), 'Груз >100')]/ancestor::div[@class='suggestion-btn']")
    # the next locator is used to make any other input in the field
    OTHER_TYPE = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//span[contains(text(), 'Другое')]/ancestor::div[@class='suggestion-btn']")

    VALUE_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='cost order-input-wrapper']//input[@type='number']")
    # the next 2 locators return select-object
    WEIGHT_DROPDOWN = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//select[@name='weight']")
    WEIGHT_INPUT_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input-wrapper weight']//input[@type='number']")
    QUANTITY_FIELD = (By.XPATH, f"{RECIPIENT_INFO_BLOCK}//div[@class='order-input-wrapper count']//input[@type='number']")

    ###

    ###
    # THE NEXT LOCATORS CAN BE USED TO FIND ELEMENTS IN SPECIFICALLY ORDER_DETAILS_INFO_BLOCK

    # the next locators used only if the checkbox GET_PAYMENT_FOR_GOODS_CHECKBOX was selected before in RECIPIENT_INFO_BLOCK
    RETURN_PAYMENT_TO_CARD_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='pay-type']//input[@id='Банковская карта']")
    RETURN_PAYMENT_TO_Y_MONEY_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='pay-type']//input[@id='ЮMoney (Я.Деньги)']")
    RETURN_PAYMENT_TO_QIWI_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='pay-type']//input[@id='QIWI']")
    CARD_OR_Y_MONEY_OR_QIWI_NUMBER_FIELD = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='order-input cardholder']/input")

    PAYMENT_RETURN_EXCEPT_DELIVERY_PRICE_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Возврат за минусом доставки')]/../input")
    SENDER_PAYS_BY_CASH_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Отправитель наличными')]/../input")
    RECIPIENT_PAYS_BY_CASH_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Получатель наличными')]/../input")
    ONLINE_PAYMENT_BY_CARD_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Онлайн банковской картой')]/../input")
    PAYMENT_BY_POINTS_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Оплата бонусами')]/../input")
    PAYMENT_FROM_PERSONAL_ACC_BALANCE_OPTION = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//span[contains(text(), 'Оплата с баланса личного кабинета')]/../input")

    PROMOCODE_FIELD = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='string promocode']//input")
    # the next two locators are used to determine whether the promocode entered before was accepted
    # (it's determined by either green or red sign-indicator next to the promocode input field))
    PROMOCODE_GREEN_INDICATOR = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='string promocode']//input[contains(@style, 'green_check')]")
    PROMOCODE_RED_INDICATOR = (By.XPATH, f"{ORDER_DETAILS_BLOCK}//div[@class='string promocode']//input[contains(@style, 'wrong_cross')]")


    ACCEPT_ORDER_CREATION_BUTTON = (By.XPATH, "//button[@class='start']")

    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//h3[contains(text(), 'Заказ') and contains(text(), 'создан!')]/ancestor::div[@class='modal-block']")
    TITLE_IN_ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//div[@class='overlay']//div[@class='modal-title']/h3")
    CLOSE_ORDER_CONFIRMATION_WINDOW_BUTTON = (By.XPATH, "//h3[contains(text(), 'Заказ') and contains(text(), 'создан!')]/ancestor::div[@class='modal-block']//button[@class='close']")
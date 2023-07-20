from pages.base_page import BasePage
from locators.order_creation_form_locators import OrderCreationFormLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import allure
import time


class OrderCreationForm(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.wait = WebDriverWait(self.browser, 10)

    @allure.step("Select city of delivery from dropdown list")
    def select_city_of_delivery(self, city):
        location_dropdown_select_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.LOCATIONS_OF_DELIVERY_SELECT))
        Select(location_dropdown_select_element).select_by_visible_text(city)

    @allure.step("Select 'Пешком'/'On foot' option as a delivery method")
    def select_on_foot_delivery_method(self):
        on_foot_option = self.wait.until(
            ec.element_to_be_clickable(OrderCreationFormLocators.ON_FOOT_DELIVERY_TYPE_BUTTON))
        on_foot_option.click()

    @allure.step("Select 'Легковое авто'/'By car' option as a delivery method")
    def select_by_car_delivery_method(self):
        car_option = self.wait.until(
            ec.element_to_be_clickable(OrderCreationFormLocators.CAR_DELIVERY_TYPE_BUTTON))
        car_option.click()

    @allure.step("Select 'Универсал'/'By van' option as a delivery method")
    def select_by_van_delivery_method(self):
        van_option = self.wait.until(
            ec.element_to_be_clickable(OrderCreationFormLocators.VAN_DELIVERY_TYPE_BUTTON))
        van_option.click()

    @allure.step("Select 'Газель'/'By truck' option as a delivery method")
    def select_by_truck_delivery_method(self):
        truck_option = self.wait.until(
            ec.element_to_be_clickable(OrderCreationFormLocators.TRUCK_DELIVERY_TYPE_BUTTON))
        truck_option.click()

    @allure.step("Type sender address into input field")
    def type_sender_address(self, address):
        address_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_ADDRESS_FIELD))
        address_field.send_keys(address)
        self.select_address_from_suggested(address, OrderCreationFormLocators.SENDER_ADDRESS_SUGGESTIONS)

    @allure.step("After typing sender/recipient address, select the same one from "
                 "the dropdown list of suggested/revised addresses")
    # helper method to select specific address from suggested after making an input
    def select_address_from_suggested(self, address_to_find, locator):
        all_suggested_addresses = self.wait.until(ec.visibility_of_all_elements_located(locator))
        for address in all_suggested_addresses:
            print(address.text)
            if address.text == address_to_find:
                address.click()
                return
        print("No address from suggestions matches address from your input, check test data")

    @allure.step("Type sender entrance into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type entrance would not be displayed
    def type_sender_entrance(self, entrance):
        if entrance is not None:  # while entrance field is not required
            entrance_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_ENTRANCE_FIELD))
            entrance_field.send_keys(entrance)

    @allure.step("Type sender floor into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type floor would not be displayed
    def type_sender_floor(self, floor):
        if floor is not None:
            floor_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_FLOOR_FIELD))
            floor_field.send_keys(floor)

    @allure.step("Type sender apartment or office into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type apt or office would not be displayed
    def type_sender_apt_or_office(self, apt_or_office):
        if apt_or_office is not None:
            apt_or_office_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_APT_OR_OFFICE_FIELD))
            apt_or_office_field.send_keys(apt_or_office)

    @allure.step("Type sender phone number into input field")
    def type_sender_phone(self, number):
        phone_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_PHONE_FIELD))
        phone_field.send_keys(number)

    @allure.step("Select date of pick up from dropdown list")
    # for this method date_count should be provided, where 0 - is "today", 1 - is "tomorrow" and so on (max value is 6)
    def select_pick_up_date(self, date):
        select_date_dropdown = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.DATE_OF_PICK_UP_SELECT))
        Select(select_date_dropdown).select_by_index(date)

    @allure.step("Select start time of pick up from dropdown list")
    # for this method start_time parameter could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # also, there is one more type of value for start_time parameter - "DM" - to select "doesn't matter/не важно" option
    # and by None as value for start_time parameter it will leave the default value in the input field (so, no actions)
    def set_start_time_of_pick_up(self, start_time):
        if start_time is not None:
            select_start_time_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.START_TIME_OF_PICK_UP_FIELD))
            if start_time == "DM":
                start_time = "00:00"
            Select(select_start_time_element).select_by_value(start_time)

    @allure.step("Select end time of pick up from dropdown list")
    # in this method value for end_time parameter could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # also, there is one more type of value for end_time parameter - "DM" - to select "doesn't matter/не важно" option
    def set_end_time_of_pick_up(self, end_time):
        select_end_time_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.END_TIME_OF_PICK_UP_FIELD))
        if end_time == "DM":
            end_time = "23:59"
        Select(select_end_time_element).select_by_value(end_time)

    @allure.step("Click on 'Доп.информация'/'Additional info' to expand block with 2 "
                 "additional fields for sender info")
    # the next method is used to expand block with 2 additional fields:
    # 1) sender name 2) comment to sender address
    def expand_additional_sender_info_fields(self):
        time.sleep(3)
        expand_add_info_button = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.ADDITIONAL_SENDER_INFO_BUTTON))
        expand_add_info_button.click()

    @allure.step("Type sender name into input field")
    def type_sender_name(self, name):
        if name is not None:
            name_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.SENDER_NAME_FIELD))
            name_field.send_keys(name)

    @allure.step("Type comment to sender address into input field")
    def type_comment_to_sender_address(self, comment):
        if comment is not None:
            comment_to_address_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.COMMENT_TO_SENDER_ADDRESS_FIELD))
            comment_to_address_field.send_keys(comment)

    @allure.step("Type recipient address into input field")
    def type_recipient_address(self, address):
        address_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_ADDRESS_FIELD))
        address_field.send_keys(address)
        self.select_address_from_suggested(address, OrderCreationFormLocators.RECIPIENT_ADDRESS_SUGGESTIONS)

    @allure.step("Type recipient entrance into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using type_recipient_address method), before that the element to type entrance would not be displayed
    def type_recipient_entrance(self, entrance):
        if entrance is not None:
            entrance_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_ENTRANCE_FIELD))
            entrance_field.send_keys(entrance)

    @allure.step("Type recipient floor into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using type_recipient_address method), before that the element to type floor would not be displayed
    def type_recipient_floor(self, floor):
        if floor is not None:
            floor_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_FLOOR_FIELD))
            floor_field.send_keys(floor)

    @allure.step("Type recipient apartment of office into input field")
    # this method can be used only after some value was typed in the main address field
    # (by using type_recipient_address method), before that the element to type apt or office would not be displayed
    def type_recipient_apt_or_office(self, apt_or_office):
        if apt_or_office is not None:
            apt_or_office_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_APT_OR_OFFICE_FIELD))
            apt_or_office_field.send_keys(apt_or_office)

    @allure.step("Type recipient phone into input field")
    def type_recipient_phone(self, number):
        phone_field = self.wait.until(
            ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_PHONE_FIELD))
        phone_field.send_keys(number)

    @allure.step("Select date of recieving from dropdown list")
    # for this method date_count should be provided, where 0 - is "today", 1 - is "tomorrow" and so on (max value is 6)
    def select_receiving_date(self, date):
        if date is not None:
            select_date_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.DATE_OF_RECEIVING_SELECT))
            Select(select_date_element).select_by_index(date)

    @allure.step("Select start time of recieving from dropdown list")
    # for this method start_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # there is always an option with value "doesn't matter/не важно" exists, with should be provided as a "DM"
    def set_start_time_receiving(self, start_time):
        if start_time is not None:
            select_start_time_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.START_TIME_OF_RECEIVING_FIELD))
            if start_time == "DM":
                start_time = "00:00"
            Select(select_start_time_element).select_by_value(start_time)

    @allure.step("Select end time of recieving from dropdown list")
    # for this method end_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00" there
    # is always an option with value "doesn't matter/не важно" exists, with should be provided in parameters as "DM"
    # - meaning, doesn't matter
    def set_end_time_receiving(self, end_time):
        select_end_time_element = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.END_TIME_OF_RECEIVING_FIELD))
        if end_time == "DM":
            end_time = "23:59"
        Select(select_end_time_element).select_by_value(end_time)

    @allure.step("Select 'Получить наличные за товар'/'Get payment for goods' option in checkbox")
    def select_get_payment_for_goods(self, status):
        if status is True:
            select_get_payment_checkbox = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.GET_PAYMENT_FOR_GOODS_CHECKBOX))
            select_get_payment_checkbox.click()

    @allure.step("Click on 'Доп.информация'/'Additional info' to expand block with 2 "
                 "additional fields for recipient info")
    # the next method is used to expand block with 2 additional fields:
    # 1) recipient name 2) comment to recipient address
    def expand_additional_recipient_info_fields(self):
        time.sleep(3)
        expand_add_info_button = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.ADDITIONAL_RECIPIENT_INFO_BUTTON))
        expand_add_info_button.click()

    @allure.step("Type recipient name into input field")
    def type_recipient_name(self, name):
        if name is not None:
            name_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_NAME_FIELD))
            name_field.send_keys(name)

    @allure.step("Type comment to recipient address into input field")
    def type_comment_to_recipient_address(self, comment):
        if comment is not None:
            comment_to_address_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.COMMENT_TO_RECIPIENT_ADDRESS_FIELD))
            comment_to_address_field.send_keys(comment)

    @allure.step("Type custom value as what to deliver into input field")
    def type_what_to_deliver(self, what_to_deliver):
        what_to_deliver_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.WHAT_TO_DELIVER_FIELD))
        what_to_deliver_field.send_keys(what_to_deliver)

    @allure.step("Select 'Документы'/'Documents' option as what to deliver")
    def select_docs_as_what_to_deliver(self):
        docs_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.DOCUMENTS_TYPE))
        docs_option.click()

    @allure.step("Select 'Сюрприз'/'Surprise' option as what to deliver")
    def select_surprise_as_what_to_deliver(self):
        surprise_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.SURPRISE_TYPE))
        surprise_option.click()

    @allure.step("Select 'Хрупкий груз'/'Fragile' option as what to deliver")
    def select_fragile_as_what_to_deliver(self):
        fragile_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.FRAGILE_TYPE))
        fragile_option.click()

    @allure.step("Select 'Другое'/'Other' option as what to deliver")
    def select_other_type_of_what_to_deliver_and_type_it(self, what_to_deliver):
        other_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.OTHER_TYPE))
        other_option.click()
        what_to_deliver_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.WHAT_TO_DELIVER_FIELD))
        what_to_deliver_field.send_keys(what_to_deliver)

    @allure.step("Type value (in rubles) for one item in delivery into input field")
    def set_value_for_one_item(self, value):
        value_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.VALUE_FIELD))
        value_field.send_keys(value)


    @allure.step("Set weight of one item in delivery from predefined options (using user input in grams)")
    # for the next method "weight" parameter should be provided as a number of grams
    def set_weight_for_one_item_from_predefined_options(self, weight):
        weight_select_object = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.WEIGHT_DROPDOWN))
        # weight_select_object.click()

        if weight < 500:
            Select(weight_select_object).select_by_value("500")
        if 500 <= weight < 1000:
            Select(weight_select_object).select_by_value("1000")
        if 1000 <= weight < 3000:
            Select(weight_select_object).select_by_value("3000")
        if 3000 <= weight < 5000:
            Select(weight_select_object).select_by_value("5000")
        if 5000 <= weight < 10000:
            Select(weight_select_object).select_by_value("10000")
        if 10000 <= weight < 15000:
            Select(weight_select_object).select_by_value("15000")

    @allure.step("Set custom weight of one item in delivery (in grams)")
    def set_custom_weight_in_grams(self, weight):
        weight_select_object = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.WEIGHT_DROPDOWN))
        Select(weight_select_object).select_by_value("x")
        weight_input_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.WEIGHT_INPUT_FIELD))
        self.clear_text_field(weight_input_field)
        weight_input_field.send_keys(weight)

    @allure.step("Set quantity of items in delivery)")
    def set_quantity(self, count):
        count_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.QUANTITY_FIELD))
        self.clear_text_field(count_field)
        count_field.send_keys(count)


    # the next 4 methods are used to define
    # how payment for items delivered will be returned to sender
    @allure.step("Select (in checkbox) 'Банковская карта'/'Card' option as a type of payment return for goods delivered")
    def set_type_of_payment_return_for_goods_as_card(self):
        return_payment_to_card_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.RETURN_PAYMENT_TO_CARD_OPTION))
        return_payment_to_card_option.click()

    @allure.step("Select (in checkbox) 'ЮMoney (Я.Деньги)'/'YMoney' option as a type of payment return for goods delivered")
    def set_type_of_payment_return_for_goods_as_y_money(self):
        return_payment_to_y_money_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.RETURN_PAYMENT_TO_Y_MONEY_OPTION))
        return_payment_to_y_money_option.click()

    @allure.step("Select (in checkbox) 'QIWI' option as a type of payment return for goods delivered")
    def set_type_of_payment_return_for_goods_as_qiwi(self):
        return_payment_to_qiwi_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.RETURN_PAYMENT_TO_QIWI_OPTION))
        return_payment_to_qiwi_option.click()

    @allure.step("Type 'Номер карты, кошелька...' (billing info) for payment return for goods delivered")
    def type_billing_info_for_return(self, info):
        billing_info_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.CARD_OR_Y_MONEY_OR_QIWI_NUMBER_FIELD))
        billing_info_field.send_keys(info)

    @allure.step("Select (in checkbox) 'Возврат за минусом доставки'/'Return except price of delivery' option as a type of payment for delivery")
    # the next 6 methods are used to define how delivery will be
    def set_payment_for_delivery_as_return_except_price_of_delivery(self):
        return_except_delivery_price_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.PAYMENT_RETURN_EXCEPT_DELIVERY_PRICE_OPTION))
        return_except_delivery_price_option.click()

    @allure.step("Select (in checkbox) 'Отправитель наличными'/'Sender by cash' option as a type of payment for delivery")
    def set_payment_for_delivery_as_sender_by_cash(self):
        sender_by_cash_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.SENDER_PAYS_BY_CASH_OPTION))
        sender_by_cash_option.click()

    @allure.step("Select (in checkbox) 'Получатель наличными'/'Recipient by cash' option as a type of payment for delivery")
    def set_payment_for_delivery_as_recipient_by_cash(self):
        recipient_by_cash_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.RECIPIENT_PAYS_BY_CASH_OPTION))
        recipient_by_cash_option.click()

    @allure.step("Select (in checkbox) 'Онлайн банковской картой'/'Online by card' option as a type of payment for delivery")
    def set_payment_for_delivery_as_online_by_card(self):
        online_by_card_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.ONLINE_PAYMENT_BY_CARD_OPTION))
        online_by_card_option.click()

    @allure.step("Select (in checkbox) 'Оплата бонусами'/'By points' option as a type of payment for delivery")
    # the next method is used to select the option "Оплата бонусами"
    def set_payment_for_delivery_as_by_points(self):
        by_points_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.PAYMENT_BY_POINTS_OPTION))
        by_points_option.click()

    @allure.step("Select (in checkbox) 'Оплата с баланса личного кабинета'/'From personal account balance' option as a type of payment for delivery")
    def set_payment_for_delivery_as_from_personal_acc_balance(self):
        from_personal_acc_balance_option = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.PAYMENT_FROM_PERSONAL_ACC_BALANCE_OPTION))
        from_personal_acc_balance_option.click()

    @allure.step("Type promocode into input field")
    def type_promocode(self, code):
        if code is not None:
            promocode_field = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.PROMOCODE_FIELD))
            self.clear_text_field(promocode_field)
            promocode_field.send_keys(code)
            self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.PROMOCODE_GREEN_INDICATOR))

    @allure.step("Click on 'Запустить заказ'/'Create order' button to submit the form")
    def accept_order_creation_form(self):
        accept_button = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.ACCEPT_ORDER_CREATION_BUTTON))
        accept_button.click()

    @allure.step("Check that order confirmation window is shown")
    def order_confirmation_window_is_shown(self):
        confirmation_windows_found = self.wait.until(ec.visibility_of_all_elements_located(OrderCreationFormLocators.ORDER_CONFIRMATION_WINDOW))
        return len(confirmation_windows_found) == 1

    @allure.step("Get the number of order created (from confirmation window)")
    def get_number_of_order_created(self):
        confirmation_title = self.wait.until(ec.visibility_of_element_located(OrderCreationFormLocators.TITLE_IN_ORDER_CONFIRMATION_WINDOW))
        confirmation_title_text = confirmation_title.text
        text_split = confirmation_title_text.split()
        return (text_split[1])[1:]  # by that the number of order from confirmation window is returned without "№" symbol

    @allure.step("Close order confirmation window")
    def close_confirmation_window(self):
        close_button = self.wait.until(ec.element_to_be_clickable(OrderCreationFormLocators.CLOSE_ORDER_CONFIRMATION_WINDOW_BUTTON))
        close_button.click()
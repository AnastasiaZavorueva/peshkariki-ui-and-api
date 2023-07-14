import from pages.base_page import BasePage
from locators.order_creation_form_locators import OrderCreationFormLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from

class OrderCreationForm(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        wait = WebDriverWait(self.browser, 10)
        self.sender_info_block = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_INFO_BLOCK))
        self.recipient_info_block = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.RECIPIENT_INFO_BLOCK))
        self.order_details_block = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.ORDER_DETAILS_BLOCK))
        self.services_block = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SERVICES_BLOCK))



    def select_on_foot_delivery_type(self):
        wait = WebDriverWait(self.browser, 10)
        on_foot_option = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.ON_FOOT_DELIVERY_TYPE_BUTTON))
        on_foot_option.click()

    def select_by_car_delivery_type(self):
        wait = WebDriverWait(self.browser, 10)
        car_option = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.CAR_DELIVERY_TYPE_BUTTON))
        car_option.click()

    def select_by_van_delivery_type(self):
        wait = WebDriverWait(self.browser, 10)
        van_option = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.VAN_DELIVERY_TYPE_BUTTON))
        van_option.click()

    def select_by_truck_delivery_type(self):
        wait = WebDriverWait(self.browser, 10)
        truck_option = wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.TRUCK_DELIVERY_TYPE_BUTTON))
        truck_option.click()



    def type_sender_address(self, address):
        wait = WebDriverWait(self.browser, 10)
        address_field =  self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_ADDRESS_FIELD)))
        address_field.click()
        address_field.send_keys(address)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type entrance would not be displayed
    def type_sender_entrance(self, entrance):
        wait = WebDriverWait(self.browser, 10)
        entrance_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_ENTRANCE_FIELD)))
        entrance_field.click()
        entrance_field.send_keys(entrance)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type floor would not be displayed
    def type_sender_floor(self, floor):
        wait = WebDriverWait(self.browser, 10)
        floor_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_FLOOR_FIELD)))
        floor_field.click()
        floor_field.send_keys(floor)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type apt or office would not be displayed
    def type_sender_apt_or_office(self, apt_or_office):
        wait = WebDriverWait(self.browser, 10)
        apt_or_office_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_APT_OR_OFFICE_FIELD)))
        apt_or_office_field.click()
        apt_or_office_field.send_keys(apt_or_office)

    def type_sender_phone(self, number):
        wait = WebDriverWait(self.browser, 10)
        phone_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_PHONE_FIELD)))
        phone_field.click()
        phone_field.send_keys(number)

    # for this method date_count should be provided, where 0 - is "today", 1 - is "tomorrow" and so on (max value is 6)
    def select_pick_up_date(self, date_count):
        wait = WebDriverWait(self.browser, 10)
        select_date_element = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.DATE_OF_PICK_UP_SELECT)))
        select_date_element.select_by_index(date_count)

    # for this method start_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # there is always an option with value "doesn't matter/не важно" exists, with should be provided as a "DM"
    def set_start_time_of_pick_up(self, start_time):
        wait = WebDriverWait(self.browser, 10)
        select_start_time_element = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.START_TIME_OF_PICK_UP_FIELD)))
        if start_time == "DM":
            start_time = "00:00"
        select_start_time_element.select_by_value(start_time)

    # for this method end_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # there is always an option with value "doesn't matter/не важно" exists, with should be provided in parameters as "DM" - meaning, doesn't matter
    def set_end_time_of_pick_up(self, end_time):
        wait = WebDriverWait(self.browser, 10)
        select_end_time_element = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.END_TIME_OF_PICK_UP_FIELD)))
        if end_time == "DM":
            end_time = "23:59"
        select_end_time_element.select_by_value(end_time)

    # the next method is used to expand block with 2 additional fields:
    # 1) sender name 2) comment to sender address
    def expand_additional_sender_info_fields(self):
        wait = WebDriverWait(self.browser, 10)
        expand_add_info_button = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.ADDITIONAL_SENDER_INFO_BUTTON)))
        expand_add_info_button.click()

    def type_sender_name(self, name):
        wait = WebDriverWait(self.browser, 10)
        name_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_NAME_FIELD)))
        name_field.click()
        name_field.send_keys(name)

    def type_comment_to_pick_up_address(self, comment):
        wait = WebDriverWait(self.browser, 10)
        comment_to_address_field = self.sender_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.COMMENT_TO_SENDER_ADDRESS_FIELD)))
        comment_to_address_field.click()
        comment_to_address_field.send_keys(comment)



    def type_recipient_address(self, address):
        wait = WebDriverWait(self.browser, 10)
        address_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_ADDRESS_FIELD)))
        address_field.click()
        address_field.send_keys(address)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type entrance would not be displayed
    def type_recipient_entrance(self, entrance):
        wait = WebDriverWait(self.browser, 10)
        entrance_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_ENTRANCE_FIELD)))
        entrance_field.click()
        entrance_field.send_keys(entrance)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type floor would not be displayed
    def type_recipient_floor(self, floor):
        wait = WebDriverWait(self.browser, 10)
        floor_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_FLOOR_FIELD)))
        floor_field.click()
        floor_field.send_keys(floor)

    # this method can be used only after some value was typed in the main address field
    # (by using the method above), before that the element to type apt or office would not be displayed
    def type_recipient_apt_or_office(self, apt_or_office):
        wait = WebDriverWait(self.browser, 10)
        apt_or_office_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_APT_OR_OFFICE_FIELD)))
        apt_or_office_field.click()
        apt_or_office_field.send_keys(apt_or_office)

    def type_recipient_phone(self, number):
        wait = WebDriverWait(self.browser, 10)
        phone_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_PHONE_FIELD)))
        phone_field.click()
        phone_field.send_keys(number)

    # for this method date_count should be provided, where 0 - is "today", 1 - is "tomorrow" and so on (max value is 6)
    def select_receiving_date(self, date_count):
        wait = WebDriverWait(self.browser, 10)
        select_date_element = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.DATE_OF_PICK_UP_SELECT)))
        select_date_element.select_by_index(date_count)

    # for this method start_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # there is always an option with value "doesn't matter/не важно" exists, with should be provided as a "DM"
    def set_start_time_of_receiving(self, start_time):
        wait = WebDriverWait(self.browser, 10)
        select_start_time_element = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.START_TIME_OF_PICK_UP_FIELD)))
        if start_time == "DM":
            start_time = "00:00"
        select_start_time_element.select_by_value(start_time)

    # for this method end_time value could be either "00:00", "00:30", "01:00", "01:30" and so on up to "23:00"
    # there is always an option with value "doesn't matter/не важно" exists, with should be provided in parameters as "DM" - meaning, doesn't matter
    def set_end_time_receiving(self, end_time):
        wait = WebDriverWait(self.browser, 10)
        select_end_time_element = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.END_TIME_OF_PICK_UP_FIELD)))
        if end_time == "DM":
            end_time = "23:59"
        select_end_time_element.select_by_value(end_time)

    # the next method is used to expand block with 2 additional fields:
    # 1) recipient name 2) comment to recipient address
    def expand_additional_recipient_info_fields(self):
        wait = WebDriverWait(self.browser, 10)
        expand_add_info_button = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.ADDITIONAL_SENDER_INFO_BUTTON)))
        expand_add_info_button.click()

    def type_recipient_name(self, name):
        wait = WebDriverWait(self.browser, 10)
        name_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.SENDER_NAME_FIELD)))
        name_field.click()
        name_field.send_keys(name)

    def type_comment_to_recipient_address(self, comment):
        wait = WebDriverWait(self.browser, 10)
        comment_to_address_field = self.recipient_info_block.find_element(wait.until(EC.visibility_of_element_located(OrderCreationFormLocators.COMMENT_TO_SENDER_ADDRESS_FIELD)))
        comment_to_address_field.click()
        comment_to_address_field.send_keys(comment)


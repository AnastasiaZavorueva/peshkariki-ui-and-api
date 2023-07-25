from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.my_orders_page_locators import MyOrdersPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import staleness_of



class MyOrdersPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.wait = WebDriverWait(self.browser, 10)

    @allure.step("Click on 'Создать заказ'/'Create order' button to open order creation form")
    def navigate_to_create_order(self):
        create_order_button = self.wait.until(ec.element_to_be_clickable(MyOrdersPageLocators.CREATE_NEW_ORDER_BUTTON))
        create_order_button.click()

    @allure.step("Select 'Доставка товаров и документов'/'Delivery of goods and documents' in modal window shown")
    def select_goods_and_docs_delivery(self):
        create_order_button = self.wait.until(ec.element_to_be_clickable(MyOrdersPageLocators.GOODS_AND_DOCS_DELIVERY_BUTTON))
        create_order_button.click()

    @allure.step("Select 'Выкуп товара. Купим и доставим'/'Goods redemption. We'll buy and deliver goods' in modal window shown")
    def select_goods_redemption(self):
        create_order_button = self.wait.until(ec.element_to_be_clickable(MyOrdersPageLocators.GOODS_REDEMPTION_BUTTON))
        create_order_button.click()


    # it's better to use the next 2 methods for order status verification - whether it is active, canceled, or simply does not exist
    # (because, for example, False result of order_is_shown_in_list_as_canceled could be either it's active or doesn't exist, so the
    # additional check by another method is needed for clarification)

    @allure.step("Check that specific order (found by the order number provided) is shown on My orders page as active")
    def order_is_shown_in_list_as_active(self, order_number):

        try:
            all_numbers_of_active_orders = self.wait.until(ec.visibility_of_all_elements_located(MyOrdersPageLocators.ALL_NUMBERS_OF_ACTIVE_ORDERS))
        except TimeoutException:
            print("No active orders detected on page!")
            return False

        for number_element in all_numbers_of_active_orders:
            clear_number = number_element.text.strip()[1:]
            if clear_number == order_number:
                return True
        return False

    @allure.step("Check that specific order (found by the order number provided) is shown on My orders page as canceled")
    def order_is_shown_in_list_as_canceled(self, order_number):
        print(f"Order number is: {order_number}")
        try:
            all_numbers_of_canceled_orders = self.wait.until(ec.visibility_of_all_elements_located(MyOrdersPageLocators.ALL_NUMBERS_OF_CANCELED_ORDERS))
        except TimeoutException:
            print("No cancelled orders detected on page!")
            return False

        for number_element in all_numbers_of_canceled_orders:
            clear_number = number_element.text.strip()[1:]
            print(f"I compare order number {clear_number} with order number needed")
            if clear_number == order_number:
                return True
        return False

    @allure.step("Get block (web-element) with main info of specific order (found by the order number provided)")
    #  helper-method used to find block (web-element) that contains info of specific order (found by order number provided);
    def get_order_block(self, order_number) -> WebElement:
        try:
            all_orders_shown = self.wait.until(ec.visibility_of_all_elements_located(MyOrdersPageLocators.ALL_CARDS_OF_ALL_ORDERS))
        except TimeoutException:
            print("No orders detected on page!")
            return None

        for order in all_orders_shown:
            order_number_detected = order.find_element(*MyOrdersPageLocators.ORDER_NUMBER_SHOWN)
            if order_number_detected.text.strip()[1:] == order_number:
                return order

        print(f"No order found with the number specified before: {order_number}!")
        return None

    @allure.step("Get sender address from specific order (found by the order number provided)")
    def get_sender_address_from_order(self, order_number):
        order_needed = self.get_order_block(order_number)
        sender_address_element = order_needed.find_elements(*MyOrdersPageLocators.ADDRESSES_IN_ORDER_SHOWN)[0]  # we use index 0 because the locator returns 2 elements with addresses: the first one (with index 0) belongs to sender, while the second (with index 1) belongs to recipient
        clear_address_without_subway_info_and_dots_inside = sender_address_element.text.split("км, ")[1].strip().replace(".", "")
        return clear_address_without_subway_info_and_dots_inside

    @allure.step("Get recipient address from specific order (found by the order number provided)")
    def get_recipient_address_from_order(self, order_number):
        order_needed = self.get_order_block(order_number)
        recipient_address_element = (order_needed.find_elements(*MyOrdersPageLocators.ADDRESSES_IN_ORDER_SHOWN))[1]  # we use index 0 because the locator returns 2 elements with addresses: the first one (with index 0) belongs to sender, while the second (with index 1) belongs to recipient
        clear_address_without_subway_info_and_dots_inside = recipient_address_element.text.split("км, ")[1].strip().replace(".", "")
        return clear_address_without_subway_info_and_dots_inside

    @allure.step("Get value of what to deliver from specific order (found by the order number provided)")
    def get_what_to_deliver_from_order(self, order_number):
        order_needed = self.get_order_block(order_number)
        what_to_deliver_element = order_needed.find_element(*MyOrdersPageLocators.WHAT_TO_DELIVER_SHOWN)
        what_to_deliver_value = what_to_deliver_element.text.split(": ")[1].strip()
        print (f"text detected: {what_to_deliver_value}")
        if what_to_deliver_value == "Документы":
            return "docs"
        return what_to_deliver_value

    @allure.step("Get total weight of delivery from specific order (found by the order number provided)")
    def get_total_weight_from_order(self, order_number):
        order_needed = self.get_order_block(order_number)
        total_weight_element = order_needed.find_element(*MyOrdersPageLocators.TOTAL_WEIGHT_SHOWN)
        clear_total_weight_value = total_weight_element.text.split(" ")[1].strip()
        return int(clear_total_weight_value)  # since on frontend the value is shown as a string, we convert it into int to be comparable

    @allure.step("Get total value from specific order (found by the order number provided)")
    def get_total_value_from_order(self, order_number):
        order_needed = self.get_order_block(order_number)
        total_value_element = order_needed.find_element(*MyOrdersPageLocators.TOTAL_VALUE_SHOWN)
        clear_total_value = total_value_element.text.split(" ")[1].strip()
        return int(clear_total_value) # since on frontend the value is shown as a string, we convert it into int to be comparable

    @allure.step("Cancel specific order with the 'Parcel not ready' reason(found by the order number provided)")
    def cancel_order_as_parcel_not_ready(self, order_number):
        order_needed = self.get_order_block(order_number)

        if self.order_is_shown_in_list_as_canceled(order_number) is True:
            print("Order is shown as already cancelled!")
            return

        if self.order_is_shown_in_list_as_active(order_number) is True:
            cancel_button = self.wait.until(ec.element_to_be_clickable(order_needed.find_element(*MyOrdersPageLocators.CANCEL_ORDER_BUTTON)))
            cancel_button.click()
            cancel_order_confirmation_window = self.wait.until(ec.visibility_of_element_located(MyOrdersPageLocators.CANCEL_ORDER_CONFIRMATION_WINDOW))
            parcel_not_ready_option_in_window = self.wait.until(ec.element_to_be_clickable(cancel_order_confirmation_window.find_element(*MyOrdersPageLocators.PARCEL_NOT_READY_OPTION_IN_CANCEL_ORDER)))
            parcel_not_ready_option_in_window.click()
            self.wait.until(ec.element_to_be_selected(parcel_not_ready_option_in_window))
            confirm_order_cancellation_button = self.wait.until(ec.element_to_be_clickable(MyOrdersPageLocators.CONFIRM_ORDER_CANCELLATION_BUTTON))
            confirm_order_cancellation_button.click()
            print("I clicked to cancel")

            self.wait.until(lambda driver: order_needed.get_attribute('class') == 'order canceled')
            print("Class changed to canceled")

            # ANOTHER WAY TO CHECK "CANCELLED" INDICATOR PRESENCE
            # self.wait.until(lambda driver: len(order_needed.find_elements(*MyOrdersPageLocators.CANCELED_ORDER_INDICATOR)) == 1)
            # print("I got indicator")

    @allure.step("Cancel all orders shown as active on My orders page, with the 'Parcel not ready' reason")
    # helper method to cancel all orders that are shown as active on My orders page
    # (can be used for cleaning after test execution)
    def cancel_all_orders_as_parcel_not_ready(self):
        all_active_orders_shown = self.wait.until(ec.visibility_of_all_elements_located(MyOrdersPageLocators.ALL_CARDS_OF_ACTIVE_ORDERS))
        for active_order in all_active_orders_shown:
            order_number_detected = active_order.find_element(*MyOrdersPageLocators.ORDER_NUMBER_SHOWN).text.strip()[1:]
            self.cancel_order_as_parcel_not_ready(order_number_detected)






    # #TODO: methods to check 1) start time of pick up 2) end time of pick up 3) start time of delivery 4) end time of delivery 5) price of delivery 6) amount of money to be returned as payments for delivered goods
    # #TODO: methods to 2) edit order created (can be also used for order data check) 2) cancel order created

    # def get_pick_up_date_from_order(self, order_number):
    #
    # def get_delivery_date_from_order(self, order_number):

from pages.base_page import BasePage
from locators.my_orders_page_locators import MyOrdersPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure

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

    @allure.step("Check that order with a specific number is shown in the list of all active orders on My orders page")
    def order_is_shown_in_list(self, order_number):
        all_numbers_of_active_orders = self.wait.until(ec.visibility_of_all_elements_located(MyOrdersPageLocators.ALL_NUMBERS_OF_ACTIVE_ORDERS))
        for number_element in all_numbers_of_active_orders:
            clear_number = number_element.text.strip()[1:]
            if clear_number == order_number:
                return True
        return False
   #
   #  def get_sender_address_from_order(self, order_number):
   #      if self.order_is_shown_in_list(order_number):
   #
   #
   #
   #  def get_recipient_address_from_order(self, order_number):
   #
   #  def get_what_to_deliver_from_order(self, order_number):
   #
   #  def get_weight_from_order(self, order_number):
   #
   #  def get_value_from_order(self, order_number):
   #
   #  def get_pick_up_date_from_order(self, order_number):
   #
   #  def get_delivery_date_from_order(self, order_number):
   #
   #
   # #TODO: methods to check 1) start time of pick up 2) end time of pick up 3) start time of delivery 4) end time of delivery 5) price of delivery 6) amount of money to be returned as payments for delivered goods
   # #TODO: methods to 2) edit order created (can be also used for check of order data) 2) cancel order created
   #
   #
   #
   #
   #
   #

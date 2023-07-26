from pages.my_orders_page import MyOrdersPage
from pages.order_creation_form import OrderCreationForm
from config import Links
from tests.test_data import TestData
import pytest
import time

import allure

class TestScenarioCreateNewOrder:

    @allure.feature('Order Creation Form')
    @allure.story('Valid test data, test cases ID: 1, 2')
    @allure.severity('critical')
    @allure.description('A new order is created for delivery method "by foot" and with set of data provided;'
                        'then verification is done for main order components (such as sender address, recipient address,'
                        'what to delivery value, total weight of delivery, total value of delivery)')
    @pytest.mark.parametrize("order_data", TestData.order_info)
    def test_scenario_create_new_order_by_foot(self, browser, msk_login, order_data):
        my_orders_page = MyOrdersPage(browser, Links.my_orders_page)
        my_orders_page.navigate_to_create_order()
        my_orders_page.select_goods_and_docs_delivery()

        creation_form = OrderCreationForm(browser, Links.order_creation_form_page)
        creation_form.select_on_foot_delivery_method()

        creation_form.select_city_of_delivery(order_data["city_of_delivery"])

        creation_form.type_sender_address(order_data["sender_address"])
        creation_form.type_sender_entrance(order_data["sender_entrance"])
        creation_form.type_sender_phone(order_data["sender_phone"])
        creation_form.select_pick_up_date(order_data["pick_up_date"])
        creation_form.set_start_time_of_pick_up(order_data["start_time_of_pick_up"])
        creation_form.set_end_time_of_pick_up(order_data["end_time_of_pick_up"])


        creation_form.expand_additional_sender_info_fields()
        creation_form.type_sender_name(order_data["sender_name"])
        creation_form.type_comment_to_sender_address(order_data["comment_to_sender_address"])

        creation_form.type_recipient_address(order_data["recipient_address"])
        creation_form.type_recipient_entrance(order_data["recipient_entrance"])
        creation_form.type_recipient_floor(order_data["recipient_floor"])
        creation_form.type_recipient_apt_or_office(order_data["recipient_apt_or_office"])

        creation_form.type_recipient_phone(order_data["recipient_phone"])
        creation_form.select_receiving_date(order_data["receiving_date"])
        creation_form.set_start_time_receiving(order_data["start_time_receiving"])
        creation_form.set_end_time_receiving(order_data["end_time_receiving"])
        creation_form.select_get_payment_for_goods(order_data["get_payment_for_goods"])

        creation_form.expand_additional_recipient_info_fields()
        creation_form.type_recipient_name(order_data["recipient_name"])
        creation_form.type_comment_to_recipient_address(order_data["comment_to_recipient_address"])

        creation_form.set_what_to_deliver_type(order_data["what_to_deliver"])
        creation_form.set_value_for_one_item(order_data["value_per_item"])
        creation_form.set_custom_weight_in_grams(order_data["weight"])

        creation_form.set_quantity(order_data["quantity"])

        creation_form.select_type_of_payment_return_for_goods_delivered(order_data["type_of_payment_return_for_goods"])
        creation_form.type_billing_info_for_return(order_data["billing_info_for_return"])

        creation_form.select_payment_method_for_delivery(order_data["method_of_payment_for_delivery"])
        creation_form.type_promocode(order_data["promocode"])

        creation_form.accept_order_creation_form()

        assert creation_form.order_confirmation_window_is_shown()
        number_of_order_created = creation_form.get_number_of_order_created()
        creation_form.close_confirmation_window()

        assert creation_form.get_current_url() == Links.my_orders_page

        assert my_orders_page.order_is_shown_in_list_as_active(number_of_order_created)

        assert my_orders_page.get_sender_address_from_order(number_of_order_created) == order_data["sender_address"]
        assert my_orders_page.get_recipient_address_from_order(number_of_order_created) == order_data["recipient_address"]

        assert my_orders_page.get_what_to_deliver_from_order(number_of_order_created) == order_data["what_to_deliver"]  # test it
        assert my_orders_page.get_total_weight_from_order(number_of_order_created) == (order_data["weight"]*order_data["quantity"])
        assert my_orders_page.get_total_value_from_order(number_of_order_created) == (order_data["quantity"]*order_data["value_per_item"])

        # cancel order created after executing the whole test
        my_orders_page.cancel_order_as_parcel_not_ready(number_of_order_created)
        assert my_orders_page.order_is_shown_in_list_as_canceled(number_of_order_created) is True



    # def test_cancel_all_active_orders(self, browser, msk_login):
    #     my_orders_page = MyOrdersPage(browser, Links.my_orders_page)
    #     my_orders_page.scroll_page_to_the_bottom()
    #     my_orders_page.cancel_all_orders_as_parcel_not_ready()
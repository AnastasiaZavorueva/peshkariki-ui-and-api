from pages.my_orders_page import MyOrdersPage
from pages.order_creation_form import OrderCreationForm
from config import Links
from tests.test_data import TestData
import pytest
import time

import allure

class TestScenarioCreateNewOrder1:

    @allure.feature('Order Creation Form')
    @allure.story('Valid test data, test case ID 1')
    @allure.severity('critical')
    @allure.description('In the test, a new order is created (type of delivery - by foot) '
                        'and then verified to have all data recorded correctly')
    @pytest.mark.parametrize("order_data", TestData.order_info_one)
    def test_scenario_create_new_order_by_foot_1(self, browser, msk_login, order_data):
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

        creation_form.select_docs_as_what_to_deliver()
        creation_form.set_value_for_one_item(order_data["value_per_item"])
        creation_form.set_custom_weight_in_grams(order_data["weight"])

        creation_form.set_quantity(order_data["quantity"])

        creation_form.set_type_of_payment_return_for_goods_as_card()
        creation_form.type_billing_info_for_return(order_data["billing_info_for_return"])

        creation_form.set_payment_for_delivery_as_return_except_price_of_delivery()
        creation_form.type_promocode(order_data["promocode"])

        creation_form.accept_order_creation_form()

        assert creation_form.order_confirmation_window_is_shown()
        number_of_order_created = creation_form.get_number_of_order_created()
        creation_form.close_confirmation_window()

        assert creation_form.get_current_url() == Links.my_orders_page

        assert my_orders_page.order_is_shown_in_list_as_active(number_of_order_created)

        assert my_orders_page.get_sender_address_from_order(number_of_order_created) == order_data["sender_address"]
        assert my_orders_page.get_recipient_address_from_order(number_of_order_created) == order_data["recipient_address"]

        assert my_orders_page.get_what_to_deliver_from_order(number_of_order_created) == order_data["what_to_deliver"]
        assert my_orders_page.get_total_weight_from_order(number_of_order_created) == (order_data["weight"]*order_data["quantity"])
        assert my_orders_page.get_total_value_from_order(number_of_order_created) == (order_data["quantity"]*order_data["value_per_item"])

        # cancel order created after executing the whole test
        my_orders_page.cancel_order_as_parcel_not_ready(number_of_order_created)
        assert my_orders_page.order_is_shown_in_list_as_canceled(number_of_order_created) is True


        # my_orders_page.cancel_all_orders_as_parcel_not_ready()

    # def test_for_methods(self, browser, msk_login):
    #     my_orders_page = MyOrdersPage(browser, Links.my_orders_page)
    #     my_orders_page.scroll_page_to_the_bottom()
    #     my_orders_page.cancel_all_orders_as_parcel_not_ready()
    #     time.sleep(2)
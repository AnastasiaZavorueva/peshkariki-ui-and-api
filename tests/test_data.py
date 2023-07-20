class TestData:
    valid_login_credentials_msk_user = [{"+79999991122": "coup39fnB90812"}]

    valid_login_credentials_spb_user = [{"+79997777777": "1]23456"}]

    # None value stands for "not defined", so that no actions are done on these UI elements
    order_info_one = [
        {"city_of_delivery": "Москва",
         "sender_address": "г Москва, ул Тверская, д 1",
         "sender_entrance": 8,
         "type_sender_floor": None,
         "sender_apt_or_office": None,
         "sender_phone": "8999888888",  # MSK number
         "pick_up_date": 0,
         "start_time_of_pick_up": None,  # so, it was left as it was selected by default
         "end_time_of_pick_up": "DM",  # to select "doesn't matter/не важно" option

         "sender_name": "максим***/////548369043",
         "comment_to_sender_address": None,

         "recipient_address": "г Москва, Пречистенский пер, д 7А",
         "recipient_entrance": "первый",
         "recipient_floor": None,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999888888",  # MSK number
         "receiving_date": 0,
         "start_time_receiving": None, # so, it was left as it was selected by default
         "end_time_receiving": "23:30",
         "get_payment_for_goods": True,

         "recipient_name": "максим",
         "comment_to_recipient_address": None,

         "what_to_deliver": "docs",
         "value_per_item": 100,
         "weight": 50,
         "quantity": 100,

         # "type_of_payment_return_for_goods": "",
         "billing_info_for_return": "+ 78999888888",
         # "type_of_payment_for_delivery": "",

         "promocode": "шикарно"
         }

        #
        # {"sender_address": "",
        #  "sender_entrance": "",
        #  "type_sender_floor": "",
        #  "sender_apt_or_office": "",
        #  "sender_phone": "",
        #  "pick_up_date": "",
        #  "start_time_of_pick_up": "",
        #  "end_time_of_pick_up": "",
        #
        #  "sender_name": "",
        #  "comment_to_sender_address": "",
        #
        #  "recipient_address": "",
        #  "recipient_entrance": "",
        #  "recipient_floor": "",
        #  "recipient_apt_or_office": "",
        #  "recipient_phone": "",
        #  "receiving_date": "",
        #  "start_time_of_receiving": "",
        #  "end_time_receiving": "",
        #
        #  "recipient_name": "",
        #  "comment_to_recipient_address": ""}

    ]




# this helper class is used in TestData class below to select delivery payment method
class DeliveryPaymentMethodOptions:
    RETURN_EXCEPT_PRICE_OF_DELIVERY = 1
    SENDER_BY_CASH = 2
    RECIPIENT_BY_CASH = 3
    ONLINE_BY_CARD = 4
    BY_POINTS = 5
    FROM_PERSONAL_ACCOUNT_BALANCE = 6


class PaymentReturnForGoodsTypes:
    CARD = 1
    Y_MONEY = 2
    QIWI = 3


class WhatToDeliverOptions:
    CUSTOM = 1,
    DOCUMENTS = 2
    SURPRISE = 3
    FRAGILE = 4
    HUGE = 5
    ANOTHER = 6

class TestData:

    valid_login_credentials_msk_user = [{"+79999991122": "coup39fnB90812"}]

    valid_login_credentials_spb_user = [{"+79997777777": "123456"}]



    # None value stands for "not defined", so that no actions are done on these UI elements
    order_info = [
        {"city_of_delivery": "Москва",
         "sender_address": "г Москва, ул Тверская, д 1",
         "sender_entrance": 8,
         "type_sender_floor": None,
         "sender_apt_or_office": None,
         "sender_phone": "8999888888",  # MSK number
         "pick_up_date": 1,
         "start_time_of_pick_up": None,  # so, it was left as it was selected by default
         "end_time_of_pick_up": "DM",  # to select "doesn't matter/не важно" option

         "sender_name": "максим***/////548369043",
         "comment_to_sender_address": None,

         "recipient_address": "г Москва, Пречистенский пер, д 7А",
         "recipient_entrance": "первый",
         "recipient_floor": None,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999888888",  # MSK number
         "receiving_date": 1,
         "start_time_receiving": None,  # so, it was left as it was selected by default
         "end_time_receiving": "23:30",

         "get_payment_for_goods": True,
         "type_of_payment_return_for_goods": PaymentReturnForGoodsTypes.CARD,
         "billing_info_for_return": "+ 78999888888",

         "recipient_name": "максим",
         "comment_to_recipient_address": None,

         "what_to_deliver": WhatToDeliverOptions.DOCUMENTS,
         "value_per_item": 100,
         "weight": 50,
         "quantity": 100,

         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.RETURN_EXCEPT_PRICE_OF_DELIVERY,

         "promocode": "поехал"
         },

        {"city_of_delivery": "Москва",
         "sender_address": "Московская обл, Видное, ул Школьная, д 15",
         "sender_entrance": None,
         "type_sender_floor": "второй",
         "sender_apt_or_office": None,
         "sender_phone": "8999777777",  # SPB number
         "pick_up_date": 2,
         "start_time_of_pick_up": "16:00",
         "end_time_of_pick_up": "19:00",

         "sender_name": None,
         "comment_to_sender_address": "вход слева",

         "recipient_address": "Московская обл, Одинцово, деревня Губкино, д 39",
         "recipient_entrance": None,
         "recipient_floor": 3,
         "recipient_apt_or_office": None,
         "recipient_phone": "8999777777",  # SPB number
         "receiving_date": 2,
         "start_time_receiving": '18:00',  # so, it was left as it was selected by default
         "end_time_receiving": "21:00",

         "get_payment_for_goods": False,
         "type_of_payment_return_for_goods": None,
         "billing_info_for_return": None,

         "recipient_name": None,
         "comment_to_recipient_address": "второй подъезд, налево",

         "what_to_deliver": WhatToDeliverOptions.SURPRISE,


         "value_per_item": 1000,
         "weight": 300,
         "quantity": 50,


         "method_of_payment_for_delivery": DeliveryPaymentMethodOptions.SENDER_BY_CASH,

         "promocode": "поехал2"
         }
    ]




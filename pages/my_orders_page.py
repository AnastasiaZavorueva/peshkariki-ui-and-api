import from pages.base_page import BasePage
from locators.my_orders_page_locators import MyOrdersPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyOrdersPage(BasePage):

    def navigate_to_create_order(self):
        wait = WebDriverWait(self.browser, 10)
        create_order_button = wait.until(EC.element_to_be_clickable(MyOrdersPageLocators.CREATE_NEW_ORDER_BUTTON))
        create_order_button.click()

    def choose_goods_and_docs_delivery(self):
        wait = WebDriverWait(self.browser, 10)
        create_order_button = wait.until(EC.element_to_be_clickable(MyOrdersPageLocators.GOODS_AND_DOCS_DELIVERY_BUTTON))
        create_order_button.click()

    def choose_goods_redemption(self):
        wait = WebDriverWait(self.browser, 10)
        create_order_button = wait.until(EC.element_to_be_clickable(MyOrdersPageLocators.GOODS_REDEMPTION_BUTTON))
        create_order_button.click()

    def





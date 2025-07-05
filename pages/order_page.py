import allure
import random
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from data import rent_time_info
import locators.order_page_locators as locators


class OrderPage(BasePage):

    @staticmethod
    def format_rent_time_locator(rent_time_option_locator, option):
        by, locator_for_format = rent_time_option_locator
        format_locator = locator_for_format.format(text=option, color=option)
        return by, format_locator

    @allure.step('Открываем форму заказа (кнопка сверху)')
    def open_order_form_from_header(self):
        self.accept_cookies()
        self.scroll_to_element(locators.ORDER_BUTTON_HEADER)
        self.click_on_element(locators.ORDER_BUTTON_HEADER)

    @allure.step('Открываем форму заказа (кнопка в центре страницы)')
    def open_order_form_from_middle(self):
        self.accept_cookies()
        self.scroll_to_element(locators.ORDER_BUTTON_MIDDLE)
        self.click_on_element(locators.ORDER_BUTTON_MIDDLE)

    @allure.step('Открываем форму заказа (кнопка внизу страницы)')
    def open_order_form_from_bottom(self):
        self.accept_cookies()
        self.scroll_to_element(locators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(locators.ORDER_BUTTON_BOTTOM)

    @allure.step('Закрываем cookie-баннер, если он есть')
    def accept_cookies(self):
        try:
            self.click_on_element(locators.COOKIE_BUTTON)
        except:
            pass

    @allure.step('Заполняем форму данными')
    def fill_order_field(self, data):
        self.fill_text_to_field(locators.NAME_INPUT, data['name'])
        self.fill_text_to_field(locators.SURNAME_INPUT, data['surname'])
        self.fill_text_to_field(locators.ADDRESS_INPUT, data['address'])
        self.click_on_element(locators.METRO_STATION)
        self.find_element_with_wait(locators.SELECT_METRO_STATION)
        self.click_on_element(locators.SELECT_METRO_STATION)
        self.fill_text_to_field(locators.PHONE_NUMBER_UNPUT, data['phone'])

    @allure.step('Нажимаем на кнопку "Далее" ')
    def click_next_button(self):
        self.click_on_element(locators.NEXT_BUTTON)

    @allure.step('Заполняем срок аренды и цвет самоката')
    def fill_rent_info(self, data):
        date_input = self.find_element_with_wait(locators.DELIVERY_DATE_INPUT)
        date_input.send_keys(data['rent_date'])
        date_input.send_keys(Keys.ENTER)
        self.click_on_element(locators.RENTAL_PERIOD_DROPDOWN)

        choise_random_time = random.choice(rent_time_info)
        rent_locator = self.format_rent_time_locator(locators.RENTAL_TIME_DROPDOWN, choise_random_time)
        self.click_on_element(rent_locator)

        chosen_color = random.choice(['black', 'grey'])
        color_locator = self.format_rent_time_locator(locators.SELECT_COLOR, chosen_color)
        self.click_on_element(color_locator)

        self.fill_text_to_field(locators.COMMNET_INPUT, data['rent_comment'])

    @allure.step("Подтверждаем создание заказа")
    def confirm_order(self):
        self.click_on_element(locators.ORDER_BUTTON)
        self.click_on_element(locators.CONFIRM_BUTTON)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_create_order_button(self):
        self.click_on_element(locators.ORDER_BUTTON)

    @allure.step('Подтверждаем заказ')
    def confirm_create_order(self):
        self.click_on_element(locators.CONFIRM_BUTTON)

    @allure.step('Проверяем отображение окна об успешном заказе')
    def check_change_modal_window(self):
        self.find_element_with_wait(locators.SUCCES_CREATE_ORDER)

    @allure.step('Получаем текст сообщения об успешном заказе')
    def get_successful_create_order_title(self):
        return self.get_text_from_element(locators.SUCCES_CREATE_ORDER)



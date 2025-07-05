import allure
import pytest
from data import oleg_info, elena_info
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Успешное создание заказа с параметризацией")
    @allure.description("Проверяем 2 позитивных сценария с разными пользователями и кнопками 'Заказать'")

    @pytest.mark.parametrize('form_variant, order_data', [
        ['header', oleg_info],
        ['bottom', elena_info]
    ])
    def test_successful_order_creation(self, driver_main_page, form_variant, order_data):
        order_page = OrderPage(driver_main_page)

        if form_variant == 'header':
            order_page.open_order_form_from_header()
        else:
            order_page.open_order_form_from_bottom()

        order_page.fill_order_field(order_data)
        order_page.click_next_button()
        order_page.fill_rent_info(order_data)
        order_page.confirm_order()
        order_page.check_change_modal_window()

        order_text = order_page.get_successful_create_order_title()
        assert 'Номер заказа' in order_text

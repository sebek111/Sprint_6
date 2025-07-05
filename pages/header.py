import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators import header_locators as locators
from locators import home_page_locators as home_locators


class Header(BasePage):

    @allure.step('Нажимаем на лого Яндекса в шапке сайта')
    def click_yandex_logo(self):
        self.scroll_to_element(locators.LOGO_YANDEX)
        self.click_on_element(locators.LOGO_YANDEX)
        self.switch_to_last_tab()

    @allure.step('Нажимаем на лого Самоката в шапке сайта')
    def click_scooter_logo(self):
        self.scroll_to_element(locators.LOGO_SAMOKAT)
        self.click_on_element(locators.LOGO_SAMOKAT)
        self.find_element_with_wait(home_locators.SCROLL_LOCATOR)

    @allure.step("Переходим на открытую вкладку")
    def switch_the_last_open_page(self):
        self.switch_to_last_tab()

    @allure.step("Проверяем, что мы на странице Яндекса")
    def check_yandex_dzen_opened(self):
        try:
            self.wait_until_url_contains_any(["yandex", "dzen", "ya.ru"])
        except TimeoutException:
            raise AssertionError(f"Редирект не сработал. Открыт URL: {self.get_current_url()}")



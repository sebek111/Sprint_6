import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators import header_locators as locators
from locators import home_page_locators as home_locators


class Header(BasePage):

    @allure.step('Нажимаем на лого Яндекса в шапке сайта')
    def click_yandex_logo(self):
        self.scroll_to_element(locators.LOGO_YANDEX)
        self.wait.until(EC.element_to_be_clickable(locators.LOGO_YANDEX))
        self.click_on_element(locators.LOGO_YANDEX)
        self.switch_to_last_tab()

    @allure.step('Нажимаем на лого Самоката в шапке сайта')
    def click_scooter_logo(self):
        self.scroll_to_element(locators.LOGO_SAMOKAT)
        self.wait.until(EC.element_to_be_clickable(locators.LOGO_SAMOKAT))
        self.click_on_element(locators.LOGO_SAMOKAT)
        self.find_element_with_wait(home_locators.SCROLL_LOCATOR)

    @allure.step("Переходим на открытую вкладку")
    def switch_the_last_open_page(self):
        self.switch_to_last_tab()

    @allure.step("Проверяем, что мы на странице Яндекса")
    def check_yandex_dzen_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "yandex" in d.current_url or "dzen" in d.current_url or "ya.ru" in d.current_url
            )
        except TimeoutException:
            raise AssertionError(f"Редирект не сработал. Открыт URL: {self.driver.current_url}")


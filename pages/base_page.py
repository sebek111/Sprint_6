from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def fill_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def fill_the_field_and_click_enter(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def scroll_to_element_center(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_and_click(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_until_url_contains_any(self, substrings: list[str]):
        self.wait.until(lambda d: any(sub in d.current_url for sub in substrings))

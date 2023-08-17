from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _define_locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def url_open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def _find_element(self, locator, timeout=20):
        return self.wait_for_element_presence(locator, timeout)

    def wait_for_element_presence(self, locator, time=20):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator_type, locator)))
        return element

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def get_element_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def send_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def clear(self, locator):
        element = self._find_element(locator)
        element.clear()

    def refresh_page(self):
        self.driver.refresh()

    def autorization(self, login_locator, text1, password_locator, password, button_locator):
        self.send_text(login_locator, text1)
        self.send_text(password_locator, password)
        self.click(button_locator)

    def select_burger_menu(self, burger_locator, logout_locator):
        element = self._find_element(burger_locator)
        element.click()
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, logout_locator)))
        button.click()
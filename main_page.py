from base_page import BasePage
from selenium.common.exceptions import TimeoutException


class Autorization(BasePage):

    MAIN_PAGE_LOCATOR = 'https://www.saucedemo.com/'
    LOGIN_AREA_LOCATOR = '//*[@id="user-name"]'
    PASSWORD_AREA_LOCATOR = '//*[@id="password"]'
    password = 'secret_sauce'
    LOGIN_BUTTON_LOCATOR = '//input[@id="login-button"]'
    BURGER_MENU_LOCATOR = "//button[@id = 'react-burger-menu-btn']"
    LOGOUT_LOCATOR = "//a[@id = 'logout_sidebar_link']"
    PRODUCT_LOGO = '//*[@id="header_container"]/div[2]/span'
    LOCKED_LOCATOR_ERROR_TEXT = '//*[@id="login_button_container"]/div/form/div[3]/h3'
    ERROR_BUTTON_MAIN_PAGE = "//button[@class='error-button']"
    MAIN_PAGE_TEXT_LOCATOR = '//*[@id="login_credentials"]/h4'

    def navigate(self):
        self.url_open(self.MAIN_PAGE_LOCATOR)

    def check_data(self):
        login_data = ['standard_user', 'problem_user', 'performance_glitch_user', "locked_out_user"]
        # прогоняю всех пользователей через цикл используя исключения.
        for login in login_data:
            self.send_text(self.LOGIN_AREA_LOCATOR, login)
            print(f'ввели логин - данные {login}')
            self.send_text(self.PASSWORD_AREA_LOCATOR, self.password)
            self.click(self.LOGIN_BUTTON_LOCATOR)
        #здесь просто очищаю поля (удаляю текст ошибки, логин и пароль
            try:
                self.click(self.ERROR_BUTTON_MAIN_PAGE)
                self.clear(self.LOGIN_AREA_LOCATOR)
                self.clear(self.PASSWORD_AREA_LOCATOR)
            except TimeoutException:
        #в бургер меню : открываю меню и нажимаю логаут
                self.select_burger_menu(self.BURGER_MENU_LOCATOR, self.LOGOUT_LOCATOR)
                print(f"Выход  {login} прошло успешно. Покинул страницу ПРОДУКТЫ.")
        print("Успешно вышли")


from playwright.sync_api import expect

from pageobject.basepage import BasePage
from qwerty import fullname,email,password
from utils.datagenerator import DataGenerator

class Cinescope_reg(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.home_url}register"

        # Локаторы элементов
        self.full_name_input = self.page.get_by_role("textbox", name="Имя Фамилия Отчество")
        self.email_input = self.page.get_by_role("textbox", name="Email")
        self.password_input = self.page.get_by_role("textbox", name="Пароль", exact=True)
        self.repeat_password_input = self.page.get_by_role("textbox", name="Повторите пароль")

        self.register_button = self.page.get_by_role("button", name="Зарегистрироваться")
        self.sign_button = self.page.get_by_role("button", name="Войти")

        self.random_email = DataGenerator.generate_email()
        self.random_name = DataGenerator.generate_name()
        self.random_password = DataGenerator.generate_random_password()

    def open(self):
        self.open_url(self.url)

    def register(self):
        self.text_element_input(self.full_name_input, self.random_name)
        self.text_element_input(self.email_input, self.random_email)
        self.text_element_input(self.password_input, self.random_password)
        self.text_element_input(self.repeat_password_input, self.random_password)

    def click_buttonn(self):
        self.click_element(self.register_button)

    def assert_was_redirect_to_login_page(self):
        self.wait_redirect_for_url(f"{self.home_url}login")

    def assert_allert_was_pop_up(self):
        self.check_pop_up_element_with_text("Подтвердите свою почту")


class Cinescope_auth(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = f"{self.home_url}login"

        self.email_input = self.page.get_by_role("textbox", name="Email")
        self.password_input = self.page.get_by_role("textbox", name="Пароль")
        self.button_auth = self.page.locator("form").get_by_role("button", name="Войти")

        self.random_email = DataGenerator.generate_email()
        self.random_password = DataGenerator.generate_random_password()


    def open_auth(self):
        self.open_url(self.url)
        self.wait_redirect_for_url(self.url)

    def auth_input(self):
        self.text_element_input(self.email_input, self.random_email)
        self.text_element_input(self.password_input, self.random_password)
        expect(self.email_input).to_have_value(self.random_email)

    def click_button_auth(self):
        self.click_element(self.button_auth)


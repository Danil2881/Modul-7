import allure
from sqlalchemy.sql.base import elements


class PageAction:
    def __init__(self, page):
        self.page = page

    @allure.step("Клик по элементу '{locator}'")
    def click_element(self, locator: str):
        locator.click()

    @allure.step("Ввод текста '{text}' в поле '{locator}'")
    def text_element_input(self, locator, text: str,):
        locator.fill(text)

    @allure.step("Переход на страницу: {url}")
    def open_url(self,url):
        self.page.goto(url)

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_redirect_for_url(self,url):
        self.page.wait_for_url(url)
        assert self.page.url == url, "Страницы не совпадают"

    @allure.step("Получение текста элемента: {locator}")
    def get_text_locator(self, locator):
        self.page.locator(locator).text_content()

    @allure.step("Ожидание появления или исчезновения элемента: {locator}, state = {state}")
    def wait_for_element(self,locator:str, state: str = "visible"):
        self.page.wait_for_selector(locator, state)



    @allure.step("Скриншот текущей страницы")
    def make_screenshot_page(self):
        screenshot_path = "screenshot.png"
        self.page.screenshot(path=screenshot_path, full_page=True)

    @allure.step("Проверка всплывающего сообщения c текстом: {text}")
    def check_pop_up_element_with_text(self, text:str):

        with allure.step("Проверка появления аллерта с текстом"):
            notofication_locator = self.page.get_by_text(text)
            notofication_locator.wait_for(state = "visible")
            assert notofication_locator.is_visible(), "Уведомление не появилось"

        with allure.step("Проверка исчезновения аллерта"):
            notofication_locator.wait_for(state = "hidden")
            assert notofication_locator.is_visible() == False, "Уведомление не пропало"


from pageobject.registr_auth import Cinescope_reg, Cinescope_auth
import allure
import pytest

@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Register")
@pytest.mark.ui
class TestRegisterPage:

    def test_reg(self,page):
        page_1 = Cinescope_reg(page)
        page_1.open()
        page_1.register()
        page_1.click_buttonn()
        page_1.assert_was_redirect_to_login_page()
        page_1.make_screenshot_page()
        page_1.assert_allert_was_pop_up()

@allure.epic("Тестирование UI")
@allure.feature("Тестирование Страницы Register")
@pytest.mark.ui
class TestAuthPage:
    def test_auth(self,page):
        page_2 = Cinescope_auth(page)
        page_2.open_auth()
        page_2.auth_input()
        page_2.click_button_auth()

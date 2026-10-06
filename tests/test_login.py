import allure
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@allure.feature("登录")
class TestLogin:
    @pytest.fixture
    def login_page(self,page):
        return LoginPage(page).open()

    @allure.title("正确账号密码登陆成功")
    @pytest.mark.smoke
    def test_login_success(self, login_page, page):
        login_page.login("standard_user", "secret_sauce")
        expect(page).to_have_url("https://www.saucedemo.com/wrong_url.html")

    @allure.title("密码错误提示报错")
    def test_login_wrong_password(self, login_page):
        login_page.login("standard_user", "wrong")
        expect(login_page.error_message()).to_contain_text(
            "Username and password do not match"
        )

    @allure.title("用户名为空提示报错")
    def test_login_empty_username(self, login_page):
        login_page.login("", "secret_sauce")
        expect(login_page.error_message()).to_contain_text(
            "Username is required"
        )

    @allure.title("锁定用户无法登录")
    def test_login_locked_user(self, login_page):
        login_page.login("locked_out_user", "secret_sauce")
        expect(login_page.error_message()).to_contain_text("locked out")
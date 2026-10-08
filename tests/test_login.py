import pytest
import allure
from playwright.sync_api import expect
from pages.login_page import LoginPage


@allure.feature("登录")
class TestLogin:

    @pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("standard_user", "secret_sauce", None),                    # 正常
            ("standard_user", "wrong", "do not match"),                  # 密码错
            ("", "secret_sauce", "Username is required"),                # 用户名为空
            ("locked_out_user", "secret_sauce", "locked out"),           # 锁定
        ],
        ids=["success", "wrong_pwd", "empty_user", "locked"],
    )
    def test_login(self, page, username, password, expected_error):
        login = LoginPage(page).open()
        login.login(username, password)

        if expected_error is None:
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        else:
            expect(login.error_message()).to_contain_text(expected_error)
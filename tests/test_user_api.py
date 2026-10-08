import pytest
import allure
from api.user_api import UserAPI


@allure.feature("用户接口")
class TestUserAPI:

    @pytest.fixture
    def api(self):
        client = UserAPI()
        yield client
        client.close()

    @allure.title("查询存在的用户返回 200")
    def test_get_user_success(self, api):
        resp = api.get_user(1)
        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1
        assert "name" in data
        assert "email" in data

    @allure.title("查询不存在的用户返回 404")
    def test_get_user_not_found(self, api):
        resp = api.get_user(9999)
        assert resp.status_code == 404

    @allure.title("创建文章返回 201")
    def test_create_post(self, api):
        resp = api.create_post("标题", "内容", 1)
        assert resp.status_code == 201
        data = resp.json()
        assert data["title"] == "标题"
        assert data["userId"] == 1
import httpx

class UserAPI:
    """用户接口封装 —— 和 Page Object 是一个思路"""
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.client = httpx.Client(base_url=self.BASE_URL, timeout=10)

    def get_user(self, user_id: int) -> httpx.Response:
        return self.client.get(f"/users/{user_id}")

    def create_post(self, title: str, body: str, user_id: int) -> httpx.Response:
        return self.client.post(
            "/posts",
            json={"title": title, "body": body, "userId": user_id},
        )

    def close(self):
        self.client.close()
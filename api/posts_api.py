import requests

class PostsAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_post(self, post_id):
        return requests.get(
            f"{self.base_url}/posts/{post_id}"
        )

    def create_post(self, payload, headers=None):
        return requests.post(
            f"{self.base_url}/posts",
            json=payload,
            headers=headers
        )


    def update_post(self, post_id, payload):
        return requests.put(
            f"{self.base_url}/posts/{post_id}",
            json=payload
        )

    def patch_post(self, post_id, payload):
        return requests.patch(
            f"{self.base_url}/posts/{post_id}",
            json=payload
        )


    def delete_post(self, post_id):
        return requests.delete(
            f"{self.base_url}/posts/{post_id}",
        )

    def get_posts(self, params=None): # 如果呼叫的人沒有傳 params，那它預設就是 None
        return requests.get(
            f"{self.base_url}/posts",
            params=params
        )

# base_url
# → 外面傳進來的值

# self.base_url
# → 這個 PostsAPI 物件自己記住的值

import pytest
from api.posts_api import PostsAPI

@pytest.fixture
def posts_api(base_url):
    return PostsAPI(base_url)

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"
# 提供共用設定
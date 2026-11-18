import pytest
from test_data import CREATE_POST_DATA, UPDATE_POST_DATA, PATCH_POST_DATA, INVALID_POST_CASES
from utils.validators import validate_schema, validate_response_time
from utils.schemas import POST_SCHEMA


@pytest.mark.parametrize(
    "post_id, expect_status", INVALID_POST_CASES, ids=[
        "zero-id",
        "negative-id",
        "nonexistent-id"
    ]
)
def test_get_post_status(posts_api, post_id, expect_status):
    response = posts_api.get_post(post_id)

    assert response.status_code == expect_status

def test_get_post(posts_api):
    response = posts_api.get_post(1)
    assert response.status_code == 200
    validate_response_time(response, 2)
    data = response.json()

    validate_schema(data, POST_SCHEMA)

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != "" ## 有沒有實際內容？


def test_create_post(posts_api):
    response = posts_api.create_post(
        CREATE_POST_DATA)

    assert response.status_code == 201

    data = response.json()
    validate_response_time(response, 2)
    validate_schema(data, POST_SCHEMA)

    assert data["title"] == CREATE_POST_DATA["title"]
    assert data["body"] == CREATE_POST_DATA["body"]
    assert data["userId"] == CREATE_POST_DATA["userId"]

def test_create_post_with_headers(posts_api):
    payload = {
            "title": "QA header test",
            "body": "learning headers",
            "userId": 1
        }
    
    headers = {
            "Content-Type": "application/json"
        }
    response = posts_api.create_post(
        payload,
        headers=headers)

    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

def test_update_post(posts_api):
    response = posts_api.update_post(1, UPDATE_POST_DATA) # 把 payload 這包資料，用 PUT 的方式送到 /posts/1

    data = response.json()
    assert response.status_code == 200
    validate_response_time(response, 2)
    validate_schema(data, POST_SCHEMA)
    assert data["id"] == UPDATE_POST_DATA["id"]
    assert data["title"] == UPDATE_POST_DATA["title"]
    assert data["body"] == UPDATE_POST_DATA["body"]
    assert data["userId"] == UPDATE_POST_DATA["userId"]

def test_patch_post(posts_api):
    response = posts_api.patch_post(
        1, PATCH_POST_DATA
    )

    data = response.json()
    validate_schema(data, POST_SCHEMA)
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == PATCH_POST_DATA["title"]

def test_delete_post(posts_api):
    response = posts_api.delete_post(1)

    data = response.json()
    assert response.status_code == 200
    assert data == {}

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(posts_api, user_id):
    
    params = {
        "userId": user_id
    }

    response = posts_api.get_posts(params=params # 把「test 裡的 params 變數」傳給「get_posts() 的 params 參數」
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for item in data:
        validate_schema(item, POST_SCHEMA)
        assert item["userId"] == user_id
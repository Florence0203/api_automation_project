CREATE_POST_DATA = {
    "title": "QA automation",
    "body": "learning API testing",
    "userId": 1
}

UPDATE_POST_DATA = {
    "id": 1,
    "title": "update title",
    "body": "update body",
    "userId": 1
}

PATCH_POST_DATA = {
    "title": "patched title"
}

INVALID_POST_CASES = [
    (0, 404),
    (-1, 404),
    (99999, 404)
]
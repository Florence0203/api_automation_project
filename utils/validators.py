import pytest

def validate_schema(data, schema):
    for field, expected_type in schema.items():
        assert field in data, f"Missing field: {field}"
        assert isinstance(data[field], expected_type), (
            f"{field} should be {expected_type.__name__}"
        )
# 定義「怎麼檢查」

def validate_response_time(response, max_seconds):
    response_time = response.elapsed.total_seconds()

    assert response_time < max_seconds, (
        f"Response too slow: {response_time: .2f}s"
    )
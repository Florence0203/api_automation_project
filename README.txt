# API Automation Testing Project

A Python-based API automation testing framework built with
pytest and requests.

## Tech Stack

- Python
- pytest
- requests
- pytest-html

## Project Structure

api_automation_project/
├── api/        # API client methods
├── tests/      # Test cases, fixtures, test data
├── utils/      # Reusable validators and schemas
├── pytest.ini
└── requirements.txt

## Test Coverage
## Test Coverage

- GET single post
- GET invalid / nonexistent post IDs
- Create post
- Create post with custom headers
- Update post with PUT
- Partial update with PATCH
- Delete post
- Query posts by userId
- Response schema validation
- Response time validation


## Run Tests

```bash
python -m pytest

```markdown
## Test Report

HTML reports are generated automatically with pytest-html.

Report file:
report.html
import pytest

@pytest.fixture
def get_base_url():
    base_url = "http://localhost:5000/"
    return base_url
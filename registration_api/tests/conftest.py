from fastapi.testclient import TestClient
import pytest

from registration_api import app


@pytest.fixture
def client():
    return TestClient(app)

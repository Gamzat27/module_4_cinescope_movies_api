import pytest
import requests
from constants import HEADERS

BASE_AUTH = "https://auth.dev-cinescope.coconutqa.ru/login"

@pytest.fixture(scope="session")
def session_super_admin():
    session = requests.Session()
    session.headers.update(HEADERS)

    login_data = {"email": "api1@gmail.com", "password": "asdqwe123Q"}
    response = session.post(BASE_AUTH, json=login_data)
    response.raise_for_status()
    token = response.json().get("accessToken")
    assert token, "accessToken отсутствует."
    session.headers.update({"Authorization": f"Bearer {token}"})

    yield session
    session.close()

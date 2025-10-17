import pytest
import requests
from constants import HEADERS, BASE_URL, user_id

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


@pytest.fixture
def create_a_movie(session_super_admin):

    MOVIE_2 = {
        "name": "Смертельная битва, новая сага.",
        "imageUrl": "https://wallpapers.com/images/hd/mortal-kombat-x-1600-x-1000-wallpaper-zhvrxvii1hcg60ol.jpg",
        "price": 565,
        "description": "Смертельная битва!",
        "location": "MSK",
        "published": True,
        "genreId": 7
    }

    r = session_super_admin.post(f"{BASE_URL}movies", json=MOVIE_2)
    r.raise_for_status()
    movie_id = r.json()["id"]
    yield movie_id
    session_super_admin.delete(f"{BASE_URL}movies/{movie_id}")


@pytest.fixture
def create_a_genre(session_super_admin):

    genre = {
        "id": 1,
        "name": "Жанр, созданный в фикстуре"
    }

    r = session_super_admin.post(f"{BASE_URL}genres", json=genre)
    r.raise_for_status()
    genre_id = r.json()["id"]
    yield genre_id
    session_super_admin.delete(f"{BASE_URL}genres/{genre_id}")



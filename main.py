import requests
from constants import BASE_URL, HEADERS, MOVIES_ID, MOVIES_ENDPOINT, GENRES_ENDPOINT, modified_movie


def get_a_movie():
    response = requests.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}", headers=HEADERS)

    assert response.status_code == 200, "Фильм не найден."
    assert response.json()["id"] == MOVIES_ID, "Айди запрашиваемого фильма и полученного в ответе разный."
    print(response.status_code)

    print(response.json())


get_a_movie()


def get_movie_genres():
    response = requests.get(url=f"{BASE_URL}{GENRES_ENDPOINT}", headers=HEADERS)

    assert response.status_code == 200, f"Status code: {response.status_code}"
    assert response.json() is not None, "Тело ответа пустое."
    print(response.json())

get_movie_genres()


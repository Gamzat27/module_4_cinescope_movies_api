import requests
from constants import (BASE_URL, HEADERS, MOVIES_ENDPOINT, MOVIES_ID, GENRES_ENDPOINT, REVIEWS_ENDPOINT,
                       MOVIE, modified_movie, review_body, edited_review, user_id)


class TestApiMovies():

    #Тест на получение афиш фильмов (позитивный кейс).
    def test_fetching_movie_posters(self):
        response = requests.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}", headers=HEADERS)
        assert response.status_code == 200, "Запрос не выдал никаких результатов."
        assert response.json()["movies"] is not None, "Пустое тело ответа."

    # Тест для получения жанров фильмов (позитивный кейс)
    def test_get_movie_genres(self):
        response = requests.get(url=f"{BASE_URL}{GENRES_ENDPOINT}", headers=HEADERS)
        assert response.status_code == 200, f"Status code: {response.status_code}"
        assert response.json() is not None, "Тело ответа пустое."

    #Тест создание фильма (позитивный кейс)
    def test_create_a_movie(self, session_super_admin):
        response = session_super_admin.post(url= f"{BASE_URL}{MOVIES_ENDPOINT}", json=MOVIE)
        try:
            assert response.status_code == 201, "Фильм не создан."
        except AssertionError:
            assert response.status_code == 409, f"Непредвиденная ошибка. Статус код ошибка: {response.status_code}"

    #Тест редактирование фильма (позитивный кейс).
    def test_changing_the_movie(self, session_super_admin):
        response = session_super_admin.patch(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}", json=modified_movie)
        assert response.status_code == 200, "Фильм не получилось отредактировать."

    #Тест на получения фильма по id (позитивный кейс).
    def test_get_a_movie(self):
        response = requests.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}", headers=HEADERS)
        assert response.status_code == 200, "Фильм не найден."
        assert response.json()["id"] == MOVIES_ID, "Айди запрашиваемого фильма и полученного в ответе разный."

    #Тест создание отзыва к фильму (позитив)
    def test_creating_a_movie_review(self, session_super_admin):
        response = session_super_admin.post(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}",
                                            json=review_body)
        try:
            assert response.status_code == 201, "Отзыв к фильму не создан."
        except AssertionError:
            assert response.status_code == 409, f"Непредвиденная ошибка. Статус код ошибки: {response.status_code}"

    #Тест для получения отзывов фильма (позитивный кейс).
    def test_get_reviews_for_a_movie(self):
        response = requests.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}", headers=HEADERS)

        assert response.status_code == 200, (f"Запрос не выдал никакой информации."
                                             f" Статус код ответа: {response.status_code}")

    #Тест редактирование отзыва к фильму (позитив)
    def test_edited_review(self, session_super_admin):
        response = session_super_admin.put(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}",
                                           json=edited_review)
        assert response.status_code == 200, "Отзыв отредактировать не получилось."

    # Тест для получения отзывов фильма (позитивный кейс).
    def test_get_reviews_movie(self):
        response = requests.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}", headers=HEADERS)
        assert response.status_code == 200, (f"Запрос не выдал никакой информации."
                                                 f" Статус код ответа: {response.status_code}")

    #Тест скрыть отзыв к фильму (позитив)
    def test_hide_movie_review(self, session_super_admin):
        response = session_super_admin.patch(url=f"{BASE_URL}{MOVIES_ENDPOINT}"
                                                    f"18569{REVIEWS_ENDPOINT}hide/{user_id}")
        assert response.status_code == 200, "Отзыв скрыть не удалось."

    #Тест показ отзыва к фильму (позитив)
    def test_showing_a_movie_review(self, session_super_admin):
        response = session_super_admin.patch(url=f"{BASE_URL}{MOVIES_ENDPOINT}"
                                                    f"18569{REVIEWS_ENDPOINT}show/{user_id}")
        assert response.status_code == 200, "Не удалось показать отзыв к фильму."

    #Тест удалить отзыв к фильму (позитив)
    def test_delete_a_movie_review(self, session_super_admin):
        response = session_super_admin.delete(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}")
        assert response.status_code == 200, "Отзыв к фильму не удалось удалить."












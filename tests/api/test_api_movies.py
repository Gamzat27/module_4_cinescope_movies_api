import requests
from constants import (BASE_URL,MOVIES_ENDPOINT, MOVIES_ID, GENRES_ENDPOINT, REVIEWS_ENDPOINT,
                       MOVIE, modified_movie, review_body, edited_review, user_id, genre)


class TestApiMovies():

    #Тест на получение афиш фильмов (позитивный кейс).
    def test_fetching_movie_posters(self, session_super_admin):
        response = session_super_admin.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}")
        assert response.status_code == 200, "Запрос не выдал никаких результатов."
        assert response.json()["movies"] is not None, "Пустое тело ответа."

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
    def test_get_a_movie(self, session_super_admin):
        response = session_super_admin.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}")
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
    def test_get_reviews_for_a_movie(self, session_super_admin):
        response = session_super_admin.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}")

        assert response.status_code == 200, (f"Запрос не выдал никакой информации."
                                             f" Статус код ответа: {response.status_code}")

    #Тест редактирование отзыва к фильму (позитив)
    def test_edited_review(self, session_super_admin):
        response = session_super_admin.put(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}",
                                           json=edited_review)
        assert response.status_code == 200, "Отзыв отредактировать не получилось."

    # Тест для получения отзывов фильма (позитивный кейс).
    def test_get_reviews_movie(self, session_super_admin):
        response = session_super_admin.get(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}")
        assert response.status_code == 200, (f"Запрос не выдал никакой информации."
                                                 f" Статус код ответа: {response.status_code}")

    #Тест скрыть отзыв к фильму (позитив)
    def test_hide_movie_review(self, session_super_admin):
        response = session_super_admin.patch(url=f"{BASE_URL}{MOVIES_ENDPOINT}18988{REVIEWS_ENDPOINT}hide/{user_id}")
        assert response.status_code == 200, "Отзыв скрыть не удалось."

    #Тест показ отзыва к фильму (позитив)
    def test_showing_a_movie_review(self, session_super_admin):
        response = session_super_admin.patch(url=f"{BASE_URL}{MOVIES_ENDPOINT}"
                                                    f"{MOVIES_ID}{REVIEWS_ENDPOINT}show/{user_id}")
        assert response.status_code == 200, "Не удалось показать отзыв к фильму."

    # Тест для получения жанров фильмов (позитивный кейс)
    def test_get_movie_genres(self):
        response = requests.get(url=f"{BASE_URL}{GENRES_ENDPOINT}")
        assert response.status_code == 200, f"Status code: {response.status_code}"
        assert response.json() is not None, "Тело ответа пустое."

        # Тест создание жанра (позитив)
    def test_getting_a_genre(self, session_super_admin):
        response = session_super_admin.post(f"{BASE_URL}{GENRES_ENDPOINT}", json=genre)
        print(response.json())
        try:
            assert response.status_code == 201, "Не получилось создать новый жанр фильма."
        except AssertionError:
            assert response.status_code == 409, f"Непредвиденная ошибка: {response.status_code}."

        # Тест получение жанра по id (позитив)
    def test_getting_a_genre_by_ID(self, session_super_admin, create_a_genre):
        response = session_super_admin.get(f"{BASE_URL}{GENRES_ENDPOINT}{create_a_genre}")
        assert response.status_code == 200, "Не удалось получить жанр фильма по id."

    #Тест удалить отзыв к фильму (позитив)
    def test_delete_a_movie_review(self, session_super_admin):
        response = session_super_admin.delete(url=f"{BASE_URL}{MOVIES_ENDPOINT}{MOVIES_ID}{REVIEWS_ENDPOINT}")
        assert response.status_code == 200, "Отзыв к фильму не удалось удалить."

    #Тест удаление жанра (позитив)
    def test_deleting_a_genre(self, session_super_admin, create_a_genre):
        response = session_super_admin.delete(f"{BASE_URL}{GENRES_ENDPOINT}{create_a_genre}")
        assert response.status_code == 200, "Не удалось удалить жанр фильма."

    #Тест удаление фильма (позитив)
    def test_deleting_a_movie(self, session_super_admin, create_a_movie):
        response = session_super_admin.delete(f"{BASE_URL}{MOVIES_ENDPOINT}{create_a_movie}")
        assert response.status_code == 200, "Не удалось удалить фильм."
        assert response.json()["id"] == create_a_movie, "ID, удаленного фильма и созданного в fixture разные."



HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}


BASE_URL = "https://api.dev-cinescope.coconutqa.ru/"
MOVIES_ENDPOINT = "/movies/"
GENRES_ENDPOINT = "/genres/"
REVIEWS_ENDPOINT = "/reviews/"

MOVIES_ID = 18988

MOVIE = {
  "name": "Убийца 2",
  "imageUrl": "https://i.ytimg.com/vi/HHsmySeiA-U/maxresdefault.jpg",
  "price": 177,
  "description": "Боевик",
  "location": "MSK",
  "published": True,
  "genreId": 500
}

modified_movie = {
        "price": 555,
        "location": "SPB",
        "genreId": 5
    }

review_body = {
  "rating": 5,
  "text": "Отличное кино, для просмотра на досуге. Рекомендую."
}

edited_review = {
  "rating": 5,
  "text": "Отличное кино, для просмотра на досуге. Рекомендую. Написано с бэка"
}

user_id = "01993c58-0fd0-41fd-8976-f675521fc6f1"

genre = {
    "id": 7,
    "name": "Дуна"
}


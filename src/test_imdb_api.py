from src.imdb_api import *


def test_search_movie():
    inception_real_id = "tt1375666"
    inception_fetched_id = ImdbRequest._search_movie_id("Inception")
    assert inception_fetched_id == inception_real_id

test_search_movie()
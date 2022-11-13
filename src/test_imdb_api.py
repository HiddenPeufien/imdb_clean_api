import pytest as pytest

from imdb_api import *


@pytest.mark.skip(reason="I don't want to use more API request for now")
def test_search_movie_id():
    inception_real_id = "tt1375666"
    inception_fetched_id = ImdbRequest.search_movie_id("Inception")
    assert inception_fetched_id == inception_real_id

def test_load_movie_id():
    inception_real_id = "tt1375666"
    inception_loaded_id = ImdbRequest.load_movie_id('Search_inception')
    assert inception_loaded_id == inception_real_id
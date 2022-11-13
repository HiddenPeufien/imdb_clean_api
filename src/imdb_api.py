import os

from api import API


class ImdbRequest(API):
    key = os.environ.get('APIKEY_IMDB')
    url_base = 'https://imdb-api.com/API'

    @classmethod
    def search_corresponding_movies(cls, keywords, save_response = False):
        request_statement = f'{cls.url_base}/Search/{cls.key}/{keywords}'
        coresponding_movies_data = API.execute_request(request_statement)['results']
        return coresponding_movies_data
    @classmethod
    def search_movie_id(cls, keywords, save_response = False):
        request_statement = f'{cls.url_base}/Search/{cls.key}/{keywords}'
        movie_title = API.execute_request(request_statement)
        best_result_movie = cls.best_search_result(movie_title)
        best_result_id = cls.get_id(best_result_movie)
        return best_result_id

    @classmethod
    def load_movie_id(cls, filename):
        server_response = API.load_server_response(filename)
        loaded_movie = cls.best_search_result(server_response)
        loaded_movie_id = cls.get_id(loaded_movie)
        return loaded_movie_id

    @classmethod
    def get_id(cls, movie):
        movie_id = movie['id']
        return movie_id
    @classmethod
    def best_search_result(cls, search_results):
        return search_results['results'][0]
    @classmethod
    def request_review(cls,movie_id):
        comments = []
        request_statement = f'{cls.url_base}/Reviews/{cls.key}/{movie_id}'
        server_response = API.execute_request(request_statement)['items']
        for i in range(len(server_response)):
            comments.append(server_response[i]['content'])
        return comments
    @classmethod
    def full_request(cls,movie_title):
        id=cls.search_movie_id(movie_title)
        comments=cls.request_review(id)
        return comments


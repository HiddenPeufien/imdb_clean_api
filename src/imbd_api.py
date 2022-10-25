from http import server
import os
from pickle import FALSE
import re
from urllib import response
import requests
import json
from api import API


class ImdbRequest(API):
    key = os.environ.get('APIKEY_IMDB')
    url_base = 'https://imdb-api.com/API'
    
    @classmethod
    def _search_movie_id(cls, keywords, save_response = False):
        request_statement = f'{cls.url_base}/Search/{cls.key}/{keywords}'
        server_response = requests.get(request_statement)
        movie_titles = json.loads(server_response.content)
        if save_response == True : cls._save_server_response(f'Search_{keywords}',movie_titles)
        return cls._best_search_result(movie_titles)
    
    @classmethod
    def _load_movie_id(cls, filename):
        server_response = cls._load_server_response(filename)
        return cls._best_search_result(server_response)

    @classmethod
    def _best_search_result(cls, search_results):
        return search_results['results'][0]
    
    def request_review(movie_title):
        pass

print(ImdbRequest._load_movie_id('Search_inception'))
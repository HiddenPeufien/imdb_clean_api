from distutils.util import execute
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
        movie_title = API._execute_request(request_statement)
        return cls._best_search_result(movie_titles)
    
    @classmethod
    def _load_movie_id(cls, filename):
        server_response = cls._load_server_response(filename)
        return cls._best_search_result(server_response)

    @classmethod
    def _best_search_result(cls, search_results):
        return search_results['results'][0]
    
    def _request_review(movie_id):
        request_statement = f'{cls.url_base}/Reviews/{cls.key}/{id}'
        server_response = requests.get(request_statement)
        reviews = json

print(ImdbRequest._load_movie_id('Search_inception'))
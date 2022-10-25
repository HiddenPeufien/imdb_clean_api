from cmath import exp
from api import API
import os

def test_save_load():
    API.save_server_response('TODELETE.txt', {"test_key":1})
    reading = API.load_server_response('TODELETE.txt')
    os.remove('TODELETE.txt')
    assert reading == {"test_key":1}

def test_execute_request_no_save():
    server_response = API.execute_request('https://jsonplaceholder.typicode.com/todos/1')
    expected_response = {"userId":1,"id":1,"title":"delectus aut autem","completed":False}

    assert server_response == expected_response

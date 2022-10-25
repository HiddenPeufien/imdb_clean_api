from src.api import API
import os

def test_save_load():
    API._save_server_response('TODELETE.txt', '{"test_key":1}')
    reading = API._load_server_response('TODELETE.txt')
    os.remove('TODELETE.txt')
    assert reading == {"test_key":1}

def test_save_load_with_json():
    API._save_server_response('TODELETE.txt,')
test_save_load()
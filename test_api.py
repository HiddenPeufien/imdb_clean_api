from src.api import API

def test_save_load():
    API._save_server_response('TODELETE.txt', 'test')
    reading = API._load_server_response('TODELETE.txt')
    assert reading == 'test'


test_save_load()
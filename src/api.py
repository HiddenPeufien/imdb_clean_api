import json
import requests

class API:
    @classmethod
    def save_server_response(cls, filename, server_response_content):
        with open(filename,'w') as saving_file:
            json_obect = json.dump(server_response_content, saving_file)

        
    @classmethod
    def load_server_response(cls, filename):
        with open(filename,'r') as response_file:
            server_response = json.load(response_file)
        return server_response

    @classmethod
    def execute_request(cls, request, save_file = None):
        server_response = requests.get(request)
        pythonic_server_response= json.loads(server_response.content)
        if not(save_file is None) : cls.save_server_response(f'Search_',pythonic_server_response)
        return pythonic_server_response
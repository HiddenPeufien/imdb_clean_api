import json

class API:
    @classmethod
    def _save_server_response(cls, filename, server_response):
        with open(filename,'w') as saving_file:
            saving_file.write(str(server_response))
        
    @classmethod
    def _load_server_response(cls, filename):
        with open(filename,'r') as response_file:
            server_response = json.load(response_file)
        return server_response
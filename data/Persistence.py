import gzip
import json
import os

DATA_PATH = 'save/data.gzip'

class Persistence():
    def __init__(self, path=DATA_PATH):
        if not os.path.exists(path):
            os.mkdir(path) 

        self.path = path

    def load(self):
        with gzip.open(self.path, 'rb') as gf:
            json_bytes = gf.read()
        
        json_str = json_bytes.decode('utf-8')
        return json.loads(json_str)

    def save(self, data):
        json_str = json.dumps(data)
        json_bytes = json_str.encode('utf-8')

        with gzip.open(self.path, 'wb') as gf:
            gf.write(json_bytes)

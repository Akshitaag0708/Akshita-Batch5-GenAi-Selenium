import os
import json

def read_json(file_path):
    base_path = os.path.dirname(os.path.dirname(__file__))  # goes to API-Framework
    full_path = os.path.join(base_path, file_path)

    with open(full_path) as f:
        return json.load(f)

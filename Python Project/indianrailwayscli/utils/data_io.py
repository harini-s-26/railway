import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def load_json(relative_path):
    filepath = os.path.join(BASE_DIR, relative_path)
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as file:
        return json.load(file)

def write_json(relative_path, data):
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath = os.path.join(BASE_DIR, relative_path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

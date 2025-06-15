import os
import json

DB_FILE = os.path.join(os.path.dirname(__file__), '../db/data.json')

# JSON dosyasını oku
def read_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({'users': [], 'locations': []}, f)
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# JSON dosyasına yaz
def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)


import os
import json

USERS_FILE = os.path.join(os.path.dirname(__file__), '../db/users.json')
LOCATIONS_FILE = os.path.join(os.path.dirname(__file__), '../db/locations.json')

# JSON dosyasını oku
def read_db():
    if not os.path.exists(USERS_FILE) or not os.path.exists(LOCATIONS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)
        with open(LOCATIONS_FILE, 'w') as f:
            json.dump([], f)
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    with open(LOCATIONS_FILE, 'r') as f:
        locations = json.load(f)
    return {'users': users, 'locations': locations}

# JSON dosyasına yaz
def write_db(data):
    with open(USERS_FILE, 'w') as f:
        json.dump(data['users'], f, indent=2)
    with open(LOCATIONS_FILE, 'w') as f:
        json.dump(data['locations'], f, indent=2)

def read_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def write_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def read_locations():
    if not os.path.exists(LOCATIONS_FILE):
        with open(LOCATIONS_FILE, 'w') as f:
            json.dump([], f)
    with open(LOCATIONS_FILE, 'r') as f:
        return json.load(f)

def write_locations(locations):
    with open(LOCATIONS_FILE, 'w') as f:
        json.dump(locations, f, indent=2)


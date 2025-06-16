# AdaAv: Sulak Haritası - Flask API

This project provides a simple backend API for a React Native/Expo mobile app, using Python (Flask) and JSON files as the database.

## Features
- JWT-based authentication
- CRUD operations for locations and users
- Data stored in separate JSON files (`users.json`, `locations.json`)
- Example API endpoints for mobile integration

## Directory Structure
```
├── app/
│   ├── __init__.py             # Flask app setup (app = Flask(__name__))
│   ├── routes/
│   │   ├── __init__.py         # Blueprint imports
│   │   ├── auth.py             # Auth endpoints
│   │   ├── locations.py        # Location endpoints
│   │   ├── users.py            # User endpoints
│   │   ├── root.py             # Root endpoint
│   │   └── token.py            # JWT token_required decorator
│   ├── db/
│   │   ├── __init__.py
│   │   ├── users.json          # Users data
│   │   └── locations.json      # Locations data
│   └── utils/
│       └── db_handler.py       # JSON read/write helpers
│
├── app.py                      # Main entry point (from app import app)
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the project
└── README.md
```

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   ./start.sh
   # or
   python3 app.py
   ```

## API Endpoints

### Auth
- `POST   /auth/login`         — User login
- `GET    /auth/me`            — Get logged-in user info

### Users
- `GET    /users`              — List all users
- `POST   /users`              — Add a new user
- `GET    /users/:id`          — Get user by ID
- `PUT    /users/:id`          — Update user by ID
- `DELETE /users/:id`          — Delete user by ID (Kullanıcı kendini silemez)

### Locations
- `GET    /locations`          — List all locations
- `POST   /locations`          — Add a new location
- `PUT    /locations/:id`      — Update a location
- `DELETE /locations/:id`      — Delete a location

- `GET    /`                   — API status/info

## Notes
- All endpoints (except login) require a JWT token in the `Authorization: Bearer <token>` header.
- Data is stored in `app/db/users.json` and `app/db/locations.json`.

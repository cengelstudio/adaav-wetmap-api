# AdaAv: Sulak Haritası - Flask API

This project provides a simple backend API for a React Native/Expo mobile app, using Python (Flask) and a JSON file as the database.

## Features
- JWT-based authentication
- CRUD operations for locations
- Data stored in a JSON file
- Example API endpoints for mobile integration

## Directory Structure
```
├── app/
│   ├── __init__.py             # Flask app setup (app = Flask(__name__))
│   ├── routes/
│   │   ├── __init__.py         # Blueprint imports
│   │   ├── auth.py             # Auth endpoints
│   │   ├── locations.py        # Location endpoints
│   │   ├── root.py             # Root endpoint
│   │   └── token.py            # JWT token_required decorator
│   ├── db/
│   │   ├── __init__.py
│   │   └── data.json           # JSON database file
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

- `POST   /auth/login`         — User login
- `GET    /auth/me`            — Get logged-in user info
- `GET    /locations`          — List all locations
- `POST   /locations`          — Add a new location
- `PUT    /locations/:id`      — Update a location
- `DELETE /locations/:id`      — Delete a location
- `GET    /`                   — API status/info

## Notes
- All endpoints (except login) require a JWT token in the `Authorization: Bearer <token>` header.
- Data is stored in `app/db/data.json`.

from app import app
from flask import request

@app.before_request
def log_request_info():
    print(f"[REQUEST] {request.method} {request.path}")
    if request.data:
        print(f"Body: {request.data.decode('utf-8')}")
    else:
        print("Body: <empty>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from src.app import create_app
import os

app = create_app('production')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

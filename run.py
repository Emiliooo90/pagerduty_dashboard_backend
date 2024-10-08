import logging
from app import create_app

logging.basicConfig(level=logging.DEBUG)

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
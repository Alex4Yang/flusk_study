from flask import Flask

from app import *

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(routes)
    app.run(host="127.0.0.1", port=8080)

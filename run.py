from flask import Flask

from app import *

app = Flask(__name__)
app.register_blueprint(routes, url_prefix="/alex")

if __name__ == "__main__":
    app.run(host="127.0.0.1")

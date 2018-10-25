from flask import Flask

from app import *

application = Flask(__name__)
application.register_blueprint(routes)

if __name__ == "__main__":
    application.run(host="127.0.0.1")

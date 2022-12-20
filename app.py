from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

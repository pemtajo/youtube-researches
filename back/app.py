# coding=UTF-8
import traceback
from flask import Flask, json, abort, make_response
import os
from http import HTTPStatus
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

GENERIC_DESCRIPTION = "Sorry :( Something happened here! Someone should have dropped soda in the keyboard but everything will be clean soon"
from config.log import Log

log = Log("back")

SWAGGER_URL = "/docs"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, "/static/swagger.json", config={"app_name": "Created by AiqDocTests"},
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def jsonify(data):
    return json.dumps(data, ensure_ascii=False).encode("utf8")


@app.route("/health", methods=["GET"])
def health():
    return make_response(jsonify("Hello World!"), HTTPStatus.OK.value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.getenv("APPLICATION_PORT"))

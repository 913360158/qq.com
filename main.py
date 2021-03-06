# -*- coding: utf-8 -*-
import json
import os
import sys
from datetime import datetime
import flask
from handler import handlerdb

App = flask.Flask(__name__)
App.secret_key = os.urandom(24)


@App.route("/home", methods=["GET", "post"])
def home():
    try:
        data = flask.request.get_data()
        ser_session = flask.session
        req_cookie = flask.request.cookies
        req_form = flask.request.form
        req_file = flask.request.files
        req_json = json.loads(data)

        response = "hello world"
        response = json.dumps(response)

        print(f"data：{data}")
        print(f"ser_session:{ser_session}")
        print(f"req_cookie:{req_cookie}")
        print(f"req_form:{req_form}")
        print(f"req_file:{req_file}")
        print(f"req_json:{req_json};{type(req_json)}")
        action_name = str(req_json.get("Action"))
        handler_class = handlerdb.produce(action_name)

    except Exception as e:
        print("Exception Error!!")
        return str(e)
    return handler_class


if __name__ == '__main__':
    App.run(host='127.0.0.1', port=5000, debug=True)

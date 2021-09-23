from flask import Flask
import os
import requests

app = Flask(__name__)

environment_name = os.getenv('ENV_SET', 'DEV')


@app.route("/")
def hello_world():
    return "I am backend on environment: {}".format(environment_name)


app.run(host='0.0.0.0', port=4000)

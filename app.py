import yaml
from flask import Flask
from waitress import serve

import view
from request_handler import RequestHandler
from script_runner import ScriptRunner
from scripts.example_script import ExampleScript

with open("configs\\example_script\\example_script_key_mappings.yml") as file:
    ExampleScript.div_codes = yaml.load(file, Loader=yaml.FullLoader)

with open("configs\\required_params.yml") as rfile:
    RequestHandler.required_params = yaml.load(rfile, Loader=yaml.FullLoader)

with open("configs\\config.yml") as wfile:
    config = yaml.load(wfile, Loader=yaml.FullLoader)
    ScriptRunner.website = config.get('website')

app = Flask(__name__)

app.register_blueprint(view.view)

if __name__ == '__main__':
    app.debug = True
    # Product WSGI server "waitress"
    # serve(app, host='127.0.0.1', port='5000')
    serve(app, host='0.0.0.0', port='5000', threads=1)

    # Flask built in server
    # app.run()
    # app.run(host='0.0.0.0', port='5000')

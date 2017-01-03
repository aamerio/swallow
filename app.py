""" test app version 0.0.1 """
import logging
import json
from flask import Flask, Response, jsonify, request, current_app, make_response
from flask_restplus import Api, Resource, fields, reqparse
import config


CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'production': 'config.ProductionConfig',
    'local': 'local_config.LocalConfig',
}

app = Flask(__name__)
app.config.from_object(CONFIG_NAME_MAPPER['development'])

#import modules
#modules.init_app(app)


if app.debug:
    logging.getLogger('progress_backend').setLevel(logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    # We don't need default Flask's loggers when using invoke tasks as the
    # latter set up colorful loggers.
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)


api = Api(app, version="app.config['VERSION']", title='Progress API',
          description='A simple Progress API',
         )
parser = reqparse.RequestParser()

@api.representation('application/javascript')
def output_json(data, code, callback, headers=None):
    resp = make_response(callback + "(" + json.dumps(data) + ")", code)
    resp.headers.extend(headers or {"Content-Type": "application/javascript"})
    return resp

    

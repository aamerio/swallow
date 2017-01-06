""" test app version 0.0.1 """
import logging.config
import json
from flask import Flask, Blueprint, Response, jsonify, request, current_app, make_response
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
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

#import api
# modules.init_app(app)


if app.config['FLASK_DEBUG']:
    logging.getLogger('progress_backend').setLevel(logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    # We don't need default Flask's loggers when using invoke tasks as the
    # latter set up colorful loggers.
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)


api = Api(app, version=app.config['VERSION'], title='Progress API',
          description='A simple Progress API',
         )
parser = reqparse.RequestParser()


@api.representation('application/javascript')
def output_json(data, code, callback, headers=None):
    resp = make_response(callback + "(" + json.dumps(data) + ")", code)
    resp.headers.extend(headers or {"Content-Type": "application/javascript"})
    return resp

@api.route(app.config['PATH_SUFFIX'] + "/users")
class UserList(Resource):
    def get(self):
        parser.add_argument('callback', type=str, help='Rate to charge for this resource')
        args = parser.parse_args()
        users = [
            {'id': 1, 'firstName': 'Matteo', 'lastName': 'Pelo', 'role': 'Art Director', 'phone': '555-321321', 'active': 1, 'notes': 'Annotazioni annotazioni1', 'gender':'male'},
            {'id': 2, 'firstName': 'Alessandra', 'lastName': 'Brianti', 'role': 'Copywriter', 'phone': '555-00022', 'active': 1, 'notes': 'Annotazioni 2', 'gender':'female'},
            {'id': 3, 'firstName': 'Enrico', 'lastName': 'Discolo', 'role': 'Art Director', 'phone': '555-321321', 'active': 1, 'notes': 'Annotazioni 3', 'gender':'male'}
        ]
        return output_json(users, 200, args.callback)


def main():
    #initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=app.config['FLASK_DEBUG'])

if __name__ == "__main__":
    main()

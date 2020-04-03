import os
from flask import Flask, make_response
from flask_bcrypt import Bcrypt
from flask_restplus import Api

from .util.Database import db
from .conf.config import configs

from src.main.api.controller.UserController import UserList, User
from src.main.api.controller.DailyReportController import DailyReport, Trends, Stats, Summary

from flask_gzip import Gzip

flask_bcrypt = Bcrypt()


def index(path=None):
    index_file = os.path.abspath('dist/index.html')
    if not os.path.exists(index_file):
        return "Failed to render frontend app. No index file exists @ {}.".format(index_file)
    return make_response(open(index_file).read())


def staticfiles(file=None):
    file_path = os.path.abspath("dist/_nuxt/{}".format(file))
    if not os.path.exists(file_path):
        return "Failed to render staticfile {}.".format(file_path)
    return make_response(open(file_path).read())


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    gzip = Gzip(app)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/<path:path>', 'index', index)
    app.add_url_rule('/_nuxt/<file>', 'staticfiles', staticfiles)

    api = Api(doc='/doc')
    api.add_resource(UserList, '/api/users/')
    api.add_resource(User, '/api/users/<email>/')

    api.add_resource(DailyReport, '/api/reports/<date>/')
    api.add_resource(DailyReport, '/api/reports/')
    api.add_resource(Stats, '/api/stats/')
    api.add_resource(Trends, '/api/trends/')
    api.add_resource(Summary, '/api/summary/')

    db.init_app(app)
    api.init_app(app)

    flask_bcrypt.init_app(app)

    return app

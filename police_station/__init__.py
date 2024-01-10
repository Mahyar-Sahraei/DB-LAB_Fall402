import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='F3lQxPk5w90',
        DATABASE=os.path.join(app.instance_path, 'police_station.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import auth, main, db
    db.init_app(app)
    app.register_blueprint(auth.blue_print)
    app.register_blueprint(main.blue_print)
    
    app.add_url_rule('/', endpoint='index')

    return app
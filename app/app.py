import os

from flask import Flask, g

from config import get_current_config
from db import init_db
from routes import router


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_current_config())
    app.register_blueprint(router)

    @app.teardown_appcontext
    def close_connection(*_):
        db = getattr(g, '_database', None)
        if db:
            db.close()

    return app

if __name__ == "__main__":
    app = create_app()

    # TODO: Implement migrations and possibly build db in Dockerfile
    if not os.path.isfile(app.config['DATABASE_URI'].split(':')[1]):
        init_db(app)

    app.run(debug=True, host='0.0.0.0')

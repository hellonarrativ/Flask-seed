from flask import Flask

from config import get_current_config
from routes import router

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_current_config())
    app.register_blueprint(router)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

from flask import Flask

from routes import router

def create_app():
    app = Flask(__name__)
    app.register_blueprint(router)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')

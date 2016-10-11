import sqlite3

from flask import g

from config import get_current_config

DATABASE = get_current_config().DATABASE_URI

def init_db(app):
    # TODO: Implement migrations and possibly build db in Dockerfile
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE, uri=True)
    return db

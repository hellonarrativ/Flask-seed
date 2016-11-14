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
        # NOTE: By default, sqlite does not enforce foreign keys on
        #       new connections
        #       (http://www.sqlite.org/foreignkeys.html#fk_enable)
        #       This is much easier than compiling a custom sqlite3 library
        db.execute('PRAGMA foreign_keys = ON')
        db.row_factory = sqlite3.Row
    return db

import unittest
from unittest.mock import patch, MagicMock

from flask import g

from app import create_app
from db import init_db, get_db


class TestInitDb(unittest.TestCase):
    def test_creates_url_table(self):
        app = create_app()
        with app.app_context():
            db = get_db()

            url_table = db.execute("""
                SELECT
                    count(*)
                FROM sqlite_master
                WHERE
                    type='table' AND name='url'
            """).fetchone()
            self.assertEqual(url_table[0], 0)

            init_db(app)

            url_table = db.execute("""
                SELECT
                    count(*)
                FROM sqlite_master
                WHERE
                    type='table' AND name='url'
            """).fetchone()
            self.assertEqual(url_table[0], 1)


class TestGetDb(unittest.TestCase):
    @patch('db.sqlite3')
    def test_only_connects_to_db_once_per_app_context(self, mock_sqlite):
        app = create_app()
        with app.app_context():
            self.assertEqual(mock_sqlite.connect.call_count, 0)
            get_db()
            self.assertEqual(mock_sqlite.connect.call_count, 1)
            get_db()
            self.assertEqual(mock_sqlite.connect.call_count, 1)
        with app.app_context():
            self.assertEqual(mock_sqlite.connect.call_count, 1)
            get_db()
            self.assertEqual(mock_sqlite.connect.call_count, 2)
            get_db()
            self.assertEqual(mock_sqlite.connect.call_count, 2)


class TestDbTeardown(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()

    def test_closes_db_if_set(self):
        with create_app().app_context():
            g._database = self.mock_db
            g._database.__bool__ = lambda _: True
        self.mock_db.close.assert_called_once_with()

    def test_handles_no_database_being_set(self):
        with create_app().app_context():
            g._database = self.mock_db
            g._database.__bool__ = lambda _: False
        self.mock_db.close.assert_not_called()

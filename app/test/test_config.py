import unittest
from unittest.mock import patch

from config import get_config, get_current_config, LocalConfig, TestConfig


class TestGetConfig(unittest.TestCase):
    def test_returns_registered_config_with_appropriate_name(self):
        config = get_config('local')
        self.assertEqual(config, LocalConfig)


class TestGetCurrentConfig(unittest.TestCase):
    @patch('config.os')
    def test_returns_config_depending_on_app_env(self, mock_os):
        mock_os.environ = {'APP_ENV': 'test'}
        self.assertEqual(get_current_config(), TestConfig)

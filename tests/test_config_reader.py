import unittest
import config_reader


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config_test = config_reader.Config('config_test.ini')

    def test_get_units(self):
        self.assertEqual(self.config_test.get_olivian_uri(), 'test_uri')
        self.assertEqual(self.config_test.get_refresh_interval(), 99)


if __name__ == '__main__':
    unittest.main()

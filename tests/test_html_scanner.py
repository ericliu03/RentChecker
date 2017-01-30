import unittest
from datetime import datetime

import html_scanner


class TestScannerOlivian(unittest.TestCase):

    def setUp(self):
        self.test_markup = open('data/olivian.html')
        self.scanner = html_scanner.ScannerOlivian()

    def test_get_units(self):
        result = self.scanner.get_units(self.test_markup)
        self.assertEqual(len(result), 24)
        apt_unit = result['Plan H (A1DD)']
        self.assertEqual(apt_unit['beds'], 1)
        self.assertEqual(apt_unit['baths'], 1)
        self.assertEqual(apt_unit['sqft'], 962)
        self.assertEqual(apt_unit['price'], 2830)
        self.assertEqual(apt_unit['available'], datetime(2017, 2, 22))


class TestScannerCirrus(unittest.TestCase):
    def setUp(self):
        self.test_markup = open('data/cirrus.html')
        self.scanner = html_scanner.ScannerCirrus()

    def test_get_units(self):
        result = self.scanner.get_units(self.test_markup)
        self.assertEqual(len(result), 28)
        apt_unit = result['803']
        self.assertEqual(apt_unit['beds'], 1)
        self.assertEqual(apt_unit['baths'], 1)
        self.assertEqual(apt_unit['sqft'], 857)
        self.assertEqual(apt_unit['price'], 2645)
        self.assertEqual(apt_unit['available'], datetime(2017, 2, 4))


class TestScannerMetropolitanTower(unittest.TestCase):
    def setUp(self):
        self.test_markup = open('data/metropolitan_tower.html')
        self.scanner = html_scanner.ScannerMetropolitanTower()

    def test_get_units(self):
        result = self.scanner.get_units(self.test_markup)
        self.assertEqual(len(result), 12)
        apt_unit = result['Bourcher']
        self.assertEqual(apt_unit['beds'], 1)
        self.assertEqual(apt_unit['baths'], 1)
        self.assertEqual(apt_unit['sqft'], 751)
        self.assertEqual(apt_unit['price'], 2460)
        self.assertEqual(apt_unit['available'], datetime(9999, 12, 12))

if __name__ == '__main__':
    unittest.main()

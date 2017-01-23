from abc import ABCMeta, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup


class AbstractScanner(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_units(self, markup):
        pass

    @staticmethod
    def convert_to_int(s):
        return int(float(s))


class ScannerOlivian(AbstractScanner):

    def get_units(self, markup):
        """Try to find all apt plans for Olivian, key would be the plan name (e.g. PLAN R (B2CD))"""
        soup = BeautifulSoup(markup, "lxml")

        html_list = soup.find_all('li', 'floor-plan')
        data_list = {}
        for each_unit in html_list:
            data_list[each_unit['data-title']] = {
                'title': each_unit['data-title'],
                'beds': self.convert_to_int(each_unit['data-beds']),
                'baths': self.convert_to_int(each_unit['data-baths']),
                'sqft': self.convert_to_int(each_unit['data-sqft-min']),
                'price': self.convert_to_int(each_unit['data-rent-min']),
                'available': datetime.strptime(each_unit['data-date'], '%m/%d/%Y')
            }
        return data_list


class ScannerCirrus(AbstractScanner):

    def get_units(self, markup):
        soup = BeautifulSoup(markup, "lxml")

        html_list = soup.find_all('li', 'floor-plan')
        data_list = {}
        for each_unit in html_list:
            data_list[each_unit['data-title']] = {
                'title': each_unit['data-title'],
                'beds': self.convert_to_int(each_unit['data-beds']),
                'baths': self.convert_to_int(each_unit['data-baths']),
                'sqft': self.convert_to_int(each_unit['data-sqft-min']),
                'price': self.convert_to_int(each_unit['data-rent-min']),
                'available': datetime.strptime(each_unit['data-date'], '%m/%d/%Y')
            }
        return data_list

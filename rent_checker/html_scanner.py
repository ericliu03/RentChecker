from abc import ABCMeta, abstractmethod
from datetime import datetime

import logging
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


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
        log.info('Processing Olivian price data...')
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
        """Try to find all apt plans for Cirrus, key would be the Unit number"""
        log.info('Processing Cirrus price data...')
        soup = BeautifulSoup(markup, "lxml")

        html_list = soup.find_all('tr')
        data_list = {}
        for unit in html_list[1:]:
            attributes = unit.find_all('td')
            unit_dict = {}
            for each_attribute in attributes:
                name, content = self.process_data(each_attribute)
                unit_dict[name] = content

            data_list[self.convert_to_int(unit_dict['unit'])] = {
                'title': unit_dict['floor-plan'],
                'beds': self.convert_to_int(unit_dict['bedroom']),
                'baths': self.convert_to_int(unit_dict['bath']),
                'sqft': self.convert_to_int(unit_dict['size']),
                'price': self.convert_to_int(unit_dict['rent']),
                'available': datetime.strptime(unit_dict['availability'], '%Y-%m-%d')
            }

        return data_list

    @staticmethod
    def process_data(attribute):
        """the format of data is not uniform, need some extra processing"""
        name = attribute['class'][0]
        if name == 'unit':
            content = attribute.a.string.strip()
        else:
            content = attribute.string.strip()

        if name == 'availability':
            if content == 'NOW':
                content = datetime.today().date().isoformat()
            try:
                content = datetime.strptime(content, '%m/%d/%Y').date().isoformat()
            except ValueError:
                content = datetime.strptime(content, '%Y-%m-%d').date().isoformat()
        if name == 'rent':
            content = content[1:]

        if content == '':
            content = '0'

        return name, content

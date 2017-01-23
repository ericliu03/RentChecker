from datetime import datetime

import requests
import logging

log = logging.getLogger(__name__)


class Collector(object):
    def __init__(self, uri, scanner, saver):
        self.uri = uri
        self.scanner = scanner
        self.saver = saver
        log.info('Collector for {!s} created'.format(scanner))

    def get_content(self):
        print('Getting html for {}'.format(self.uri))
        response = requests.Session().get(self.uri)
        return response.content

    def collect(self):
        """Fetch the html and get unit data"""
        print('Begin Collecting Data at date', datetime.now())
        content = self.get_content()
        price_dict = self.scanner.get_units(content)
        self.saver.save(price_dict)

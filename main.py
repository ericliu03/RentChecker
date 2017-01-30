import os
import time
import logging
import logging.config

from collector import Collector
from config_reader import Config
from data_saver import DataOperator
from html_scanner import ScannerOlivian, ScannerCirrus, ScannerMetropolitanTower

config = Config('./config/rent_checker.ini')


def setup_log():
    print('Setting up log...')
    log_dir = './log/'
    log_path = log_dir + 'logV1.log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_formatter = logging.Formatter("%(asctime)s [%(name)-12.12s] [%(levelname)-5.5s]  %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    return logging.getLogger(__name__)


def main():
    log = setup_log()
    log.info('RentChecker initializing...')
    interval = config.get_refresh_interval()
    collector_olivian = Collector(config.get_olivian_uri(), ScannerOlivian(), DataOperator('Olivian'))
    collector_cirrus = Collector(config.get_cirrus_uri(), ScannerCirrus(), DataOperator('Cirrus'))
    collector_metropolitan_tower = Collector(config.get_metropolitan_tower_uri(), ScannerMetropolitanTower(), DataOperator('MetropolitanTower'))

    log.info('RentChecker initialized. Begin collecting...')
    while True:
        collector_olivian.collect()
        collector_cirrus.collect()
        collector_metropolitan_tower.collect()
        log.info('sleeping for {} seconds'.format(interval))
        time.sleep(interval)

main()

import os
import time
import logging
import logging.config

from collector import Collector
from config_reader import Config
from data_saver import DataOperator
from html_scanner import ScannerOlivian

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


def main():
    setup_log()
    collector_olivian = Collector(config.get_olivian_uri(), ScannerOlivian(), DataOperator('Olivian'))
    while True:
        interval = config.get_refresh_interval()
        collector_olivian.collect()
        print('sleeping for {} seconds'.format(interval))
        time.sleep(interval)

main()

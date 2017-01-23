import os
from datetime import datetime
import json

json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime) else None)


class DataOperator(object):

    def __init__(self, folder_name):
        self.file_dir = './data/{}/'.format(folder_name)
        if not os.path.exists(self.file_dir):
            os.makedirs(self.file_dir)

    def save(self, price_dict):
        print('Saving updated file...')
        current_time = datetime.now()
        file_path = '{}{}.json'.format(self.file_dir, current_time.date().isoformat())
        try:
            with open(file_path, 'r') as f:
                price_history = json.load(f)
        except FileNotFoundError:
            price_history = {}

        price_history[current_time.isoformat()] = price_dict

        with open(file_path, 'w+') as f:
            json.dump(dict(price_history), f, sort_keys=True)

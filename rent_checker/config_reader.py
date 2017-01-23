import configparser


class Config(object):
    def __init__(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        self.default_section = config['DEFAULT']

    def get_olivian_uri(self):
        return self.default_section['UriOlivian']

    def get_refresh_interval(self):
        return int(self.default_section['SnapshotInterval'])

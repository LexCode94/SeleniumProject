import configparser


def read_config_data(section, key):
    config = configparser.ConfigParser()
    config.read("../Utilities/Config.cfg")
    return config.get(section, key)
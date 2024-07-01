import yaml

def load_config(config_path='./config/config.yaml'):
    '''
    Load the config file
    :param config_path:
    :return:
    '''
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

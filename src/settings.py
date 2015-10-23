import os

class Config(object):
    # TODO: Add a useful comment
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True

class TestConfig(Config):
    ENV = 'test'

config_dict = {
    'dev': DevelopmentConfig,
    'test': TestConfig,

    'default': DevelopmentConfig
}

def get_tornado_config():
    """ Returns a dict containing the settings for the tornado app """
    env = os.getenv('APP_ENV') or 'default'
    config_obj = config_dict[env]
    return to_tornado_dict(config_obj)

def to_tornado_dict(config_obj):
    """
    Converts Config object to a dict that tornado can easily parse
    More specifically tornado expects settings to be defined as
    a dictionary with lowercased keys
    """
    return {k.lower(): v for k, v in config_obj.__dict__.iteritems() if not k.startswith('__')}

app_config = get_tornado_config()

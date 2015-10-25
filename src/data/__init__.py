from src.settings import app_config
from .memory_store import MemoryStore

def get_config_store(app_config):
    if app_config['env'] in {'dev', 'test'}:
        store = MemoryStore(app_config['memory_store_source'])
    else:
        raise ValueError("Enivornment '{}' not supported".format(app_config.ENV))
    return store

store = get_config_store(app_config)

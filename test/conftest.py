"""
Configures pytest and custom fixtures for tests in this package
To see a full list of fixtures run `py.test --fixtures`
"""
import pytest

from src.app import create_app
from src.settings import TestConfig, to_tornado_dict

def pytest_addoption(parser):
    """ Allows us to add --runslow as an argument to py.test so we can run tests marked slow """
    parser.addoption("--runslow", action="store_true", help="run slow tests")

def pytest_runtest_setup(item):
    """ Skip tests marked 'slow' unless we explicility asked to run them """
    if 'slow' in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run")

@pytest.fixture(scope='function')
def app():
    """
    App fixtures used by pytest-tornado for things like http_client
    """
    _app_config = to_tornado_dict(TestConfig)
    _app = create_app(_app_config)
    return _app

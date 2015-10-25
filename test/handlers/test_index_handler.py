import pytest

def handler_path(base_url):
    """ Path for this handler """
    return base_url + '/'

@pytest.mark.gen_test
def test_index_returns_200(http_client, base_url):
    url = handler_path(base_url)
    response = yield http_client.fetch(url)
    assert response.code == 200

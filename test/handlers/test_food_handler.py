import pytest

def handler_path(base_url):
    return base_url + '/food'

@pytest.mark.gen_test
def test_get_foods_returns_200(http_client, base_url):
    url = handler_path(base_url)
    response = yield http_client.fetch(url)
    assert response.code == 200

@pytest.mark.gen_test
def test_get_foods_returns_json(http_client, base_url):
    url = handler_path(base_url)
    response = yield http_client.fetch(url)
    content_type = response.headers['Content-Type'].split(';')[0]
    assert content_type == 'application/json'

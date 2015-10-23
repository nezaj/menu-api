import pytest

@pytest.mark.gen_test
def test_get_index(http_client, base_url):
    response = yield http_client.fetch(base_url + '/')
    assert response.code == 200

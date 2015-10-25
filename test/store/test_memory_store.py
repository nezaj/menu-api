"""
Tests MemoryStore Interface
"""
from src.data.memory_store import MemoryStore

# Mock needs to match function signature even if we don't use the params
# pylint: disable=unused-argument
def mock_load_data(store_instance, data_dir):
    return {
        'food': {
            'Burger': {'id': 'Burger', 'Price': 'test'},
            'Pizza': {'id': 'Pizza', 'Price': 'test'}
        }
    }

def test_init_loads_data(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    assert store.data == mock_load_data('self', 'data_dir')

def test_store_create_item(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    collection = 'food'
    item_id = 'Steak'
    params = {'id': item_id, 'Price': '$10.00'}

    # Item is not in the collection
    assert item_id not in store.get_collection(collection)

    # Item is present after creation
    store.create_item(collection, params)
    assert store.get_item(collection, item_id) == params

def test_store_delete_item(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    collection_id = 'food'
    item_id = 'Steak'
    params = {'id': item_id, 'Price': '$10.00'}

    # Newly created item is present in collection
    store.create_item(collection_id, params)
    assert item_id in store.get_collection(collection_id)

    # After deleting, no longer there
    store.delete_item(collection_id, item_id)
    assert item_id not in store.get_collection(collection_id)

    # Deleting the same item again returns none
    assert store.delete_item(collection_id, item_id) is None

def test_store_get_collection(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    mocked_data = mock_load_data('self', 'data_dir')
    collection_id = 'food'
    expected_collection = mocked_data[collection_id]

    # Returns collection if it exists
    assert store.get_collection(collection_id) == expected_collection

    # Returns None if collection does not exist
    dne_collection_id = 'cars'
    assert store.get_collection(dne_collection_id) is None

def test_store_get_item(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    mocked_data = mock_load_data('self', 'data_dir')
    collection_id = 'food'
    item_id = 'Burger'
    expected_item = mocked_data[collection_id][item_id]

    # Returns item if it exists
    assert store.get_item(collection_id, item_id) == expected_item

    # Returns None if item is not in the collection
    dne_item_id = 'Steak'
    assert dne_item_id not in store.get_collection(collection_id)
    assert store.get_item(collection_id, dne_item_id) is None

def test_update_item(monkeypatch):
    monkeypatch.setattr(MemoryStore, '_load_data', mock_load_data)
    store = MemoryStore('dir')
    mocked_data = mock_load_data('self', 'data_dir')
    collection_id = 'food'
    item_id = 'Burger'
    params = {'Price': '$10.00'}
    expected_item = mocked_data[collection_id][item_id]
    expected_item.update(params)

    # Returns updated item if it exists
    assert store.update_item(collection_id, item_id, params) == expected_item

    # Returns None if no item to update
    dne_item_id = 'Steak'
    assert store.update_item(collection_id, dne_item_id, params) is None

"""
Store implementation using in-memory data
"""
import json
import os

from .store_interface import StoreInterface

class MemoryStore(object):
    __implements__ = (StoreInterface, )

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = self._load_data(data_dir)

    def _load_data(self, data_dir):
        """
        Loads data from directory defined in settings. We expect there can be
        multiple collections of data and that each collection lives in its
        own subdirectory. As a result, we go through each directory and load
        it's data into it's own key.

        For example, the "food" collection is accessed via self.data['food']
        """
        data = {}
        for d in os.listdir(data_dir):
            subd = os.path.join(data_dir, d)
            if os.path.isdir(subd):
                data[d] = self._load_json_files(subd)
        return data

    def _load_json_files(self, data_dir):
        """
        Return a dictionary representing a collection of json from the given
        data directory.

        We iterate through each json file and load it's data. We then key
        the data in each file by the id defined in the file itself.
        """
        collection = {}
        for item in os.listdir(data_dir):
            df = os.path.join(data_dir, item)
            if df.endswith(".json"):
                jd = self._load_json_file(df)
                d_id, d_meta = self._process_json(jd)
                collection[d_id] = d_meta
        return collection

    @staticmethod
    def _load_json_file(f):
        """ Loads a json config file """
        with open(f) as jf:
            jd = json.load(jf)
        return jd

    @staticmethod
    def _process_json(jd):
        """ Returns id and metadata from json dict """
        jd_id = jd["id"]
        return jd_id, jd

    def create_item(self, collection_id, params):
        c = self.data[collection_id]
        item_id, item = self._process_json(params)
        c[item_id] = item
        return item

    def delete_item(self, collection_id, item_id):
        collection = self.get_collection(collection_id)
        item = self.get_item(collection_id, item_id)
        if collection and item:
            del collection[item_id]
            return item

    def get_collection(self, collection_id):
        return self.data.get(collection_id)

    def get_item(self, collection_id, item_id):
        collection = self.get_collection(collection_id)
        if collection:
            return collection.get(item_id)

    def update_item(self, collection_id, item_id, params):
        item = self.get_item(collection_id, item_id)
        if item:
            item.update(params)
            return item

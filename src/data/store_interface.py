"""
Interface for Store implmentations
"""
class StoreInterface:

    def create_item(self, collection, params):
        """
        Creates an adds a new item to the collection
        Returns created item.
        """
        raise NotImplementedError()

    def delete_item(self, collection, unit_id):
        """
        Deletes an item from a collection.
        Returns deleted item if found, returns None otherwhise """
        raise NotImplementedError()

    def get_collection(self, collection):
        """
        Returns all items in the collection
        Returns None if collection not found
        """
        raise NotImplementedError()

    def get_item(self, collection, unit_id):
        """
        Returns item from collection. Returns None if item not found
        """
        raise NotImplementedError()

    def update_item(self, collection, unit_id, params):
        """
        Returns updated item from collection. Returns None if item not found
        """
        raise NotImplementedError()

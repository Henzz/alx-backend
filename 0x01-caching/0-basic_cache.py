#!/usr/bin/env python3
"""
Basic cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system without any size limit.
    """
    def __init__(self):
        """
        Initializes the BasicCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value for the key in self.cache_data
        dictionary.

        Args:
            key (str): The key to be used for the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            The value linked to the key, or None if key is None
            or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

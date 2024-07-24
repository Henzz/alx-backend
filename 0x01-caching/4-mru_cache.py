#!/usr/bin/env python3
"""
MRUCache is a caching system and implements a MRU
caching system with a maximum size limit.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCaching and
    implements a MRU caching system.
    """
    def __init__(self):
        """
        Initializes the MRUCache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns the item value for the key key in the
        self.cache_data dictionary. Implements MRU
        eviction if cache is full.

        Args:
            key (str): The key to be used for the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            The value linked to the key, or None if key
            is None or not found.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)

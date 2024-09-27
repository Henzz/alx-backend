#!/usr/bin/env python3
"""
LFUCache is a caching system and implements a LFU
caching system with a maximum size limit.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class inherits from BaseCaching and
    implements a LFU caching system.
    """
    def __init__(self):
        """
        Initializes the LFUCache class.
        """
        super().__init__()
        self.freq = {}
        self.min_freq = 0
        self.order = {}

    def put(self, key, item):
        """
        Assigns the item value for the key key in the
        self.cache_data dictionary. Implements LFU
        eviction if cache is full.

        Args:
            key (str): The key to be used for the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.freq[key] += 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find least frequently used item
            min_freq_keys = [k for k,
                             v in self.freq.items() if v == self.min_freq]
            # If multiple items have the same min frequency, use LRU to evict
            if len(min_freq_keys) > 1:
                lru_key = min_freq_keys[0]
                for k in min_freq_keys:
                    if self.order[k] < self.order[lru_key]:
                        lru_key = k
                del self.cache_data[lru_key]
                del self.freq[lru_key]
                del self.order[lru_key]
                print(f"DISCARD: {lru_key}")
            elif len(min_freq_keys) == 1:
                if min_freq_keys[0] in self.cache_data:
                    del self.cache_data[min_freq_keys[0]]
                    del self.freq[min_freq_keys[0]]
                    del self.order[min_freq_keys[0]]
                    print(f"DISCARD: {min_freq_keys[0]}")
            self.min_freq = min(self.freq.values()) if self.freq else 0

        self.cache_data[key] = item
        self.freq[key] = 1
        self.order[key] = len(self.order)
        self.min_freq = 1

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

        self.freq[key] += 1
        self.order[key] = len(self.order)
        return self.cache_data.get(key)

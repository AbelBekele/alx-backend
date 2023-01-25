#!/usr/bin/env python3
"""Basic Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    ----------------
    CLASS: FIFOCache
    ----------------
    """

    def __init__(self):
        """
        ----------------------
        MAGIC METHOD: __init__
        ----------------------
        Description:
                Initializes the current
                class object
        """
        super().__init__()

    def put(self, key, item):
        """
        -----------
        METHOD: put
        -----------
        Description:
                Adds to caching dictionary an item
                provided a key
        Args:
                @key: key to add to the cache
                @item: value to add to the cache
        """
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            fifo_key = next(iter(self.cache_data))
            print('DISCARD:', fifo_key)
            del self.cache_data[fifo_key]

    def get(self, key):
        """
        -----------
        METHOD: get
        -----------
        Description:
                Given a key, returns the element
                from cache_data if the key exists
                in the cache_data dictionary.
        Args:
                @key: key to look for in cache
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]

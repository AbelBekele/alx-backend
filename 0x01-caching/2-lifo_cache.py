#!/usr/bin/env python3
"""Basic Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    ----------------
    CLASS: LIFOCache
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
        if not key or not item:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LIFO_key = list(self.cache_data)[-2]
            print('DISCARD:', LIFO_key)
            del self.cache_data[LIFO_key]

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

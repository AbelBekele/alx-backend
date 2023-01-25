#!/usr/bin/env python3
"""Basic Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    ----------------
    CLASS: LFUCache
    ----------------
    """
    usage_count = {}

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
        self.usage_count = {}

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

        """
        --------
        BEHAVIOR
        --------
        Look for page faults
        - Page faults occur when the item is not in
        the dictionary

        - If the item was in the dictionary, then
        update the item and reset the element usage count
        back to zero.

        While incrementing the rest of the elements by one

        - If self.cache has more than 4 elements
        - Remove the item with the highest count
        """
        self.cache_data[key] = item
        self.usage_count[key] = 0

        if key in self.cache_data:
            for k, v in self.usage_count.items():
                if k != key:
                    self.usage_count[k] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LFU_key = max(self.usage_count, key=self.usage_count.get)
            print('DISCARD:', LFU_key)
            del self.cache_data[LFU_key]
            del self.usage_count[LFU_key]

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

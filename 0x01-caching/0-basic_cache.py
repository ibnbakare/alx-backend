#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Storing and getting objects in a cache
    """
    def put(self, key, item):
        """item added to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key.
        """
        return self.cache_data.get(key, None)

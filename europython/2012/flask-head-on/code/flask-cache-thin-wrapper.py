def get(self, *args, **kwargs):
    "Proxy function for internal cache object."
    return self.cache.get(*args, **kwargs)

def set(self, *args, **kwargs):
    "Proxy function for internal cache object."
    self.cache.set(*args, **kwargs)

# Also add, delete, delete_many, etc.

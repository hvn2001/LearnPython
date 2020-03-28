# Linked list operations
# insert_at_tail(self, key, data)
# remove(self, data)
# remove_node(self, node)
# remove_head(self)
# remove_tail(self)
# get_head(self)
# get_tail(self)
from Coderust.P10Miscellaneous.P4LRUCache.LinkedList import LinkedList


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.cache_vals = LinkedList()

    def Set(self, key, value):
        node = self.get(value)
        if node is None:
            if (self.cache_vals.size >= self.capacity):
                self.cache_vals.insert_at_tail(key, value)
                self.cache.add(value)
                self.cache.remove(self.cache_vals.get_head().data)
                self.cache_vals.remove_head()
            else:
                self.cache_vals.insert_at_tail(key, value)
                self.cache.add(value)

        else:
            self.cache_vals.remove(value)
            self.cache_vals.insert_at_tail(key, value)

    def get(self, value):
        if value not in self.cache:
            return None
        else:
            i = self.cache_vals.get_head()
            while i is not None:
                if i.data is value:
                    return i
                i = i.next

    def printcache(self):
        node = self.cache_vals.get_head()
        while node != None:
            print("(" + str(node.key) + "," + str(node.data) + ")", end="")
            node = node.next
        print()


cache1 = LRUCache(2)
cache1.Set(10, 20)
cache1.printcache()

cache1.Set(15, 25)
cache1.printcache()

cache1.Set(20, 30)
cache1.printcache()

cache1.Set(25, 35)
cache1.printcache()

cache1.Set(5, 25)
cache1.printcache()

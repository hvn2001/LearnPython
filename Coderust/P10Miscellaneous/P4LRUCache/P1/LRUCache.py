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
        self.cache = {}
        self.cache_vals = LinkedList()

    def Set(self, key, value):
        # TODO: Write - Your - Code
        return

    def get(self, key):
        # TODO: Write - Your - Code
        return -1

    def get_cache(self):
        res = ""
        node = self.cache_vals.head
        while node:
            res += "(" + str(node.key) + "," + str(node.data) + ")"
            node = node.next
        return res

from DataStructures.IntroHashing.BuildingHashTable.HashEntry import HashEntry


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    # Helper Functions
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() is 0

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for i in range(0, len(self.bucket)):
            head = self.bucket[i]
            while head is not None:
                new_index = self.get_index(head.key)
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots


'''
ht = HashTable()
print(ht.is_empty())
'''


# Hash Function
'''
def get_index(self, key):
    # hash is a built in function in Python
    hash_code = hash(key)
    index = hash_code % self.slots
    return index
'''

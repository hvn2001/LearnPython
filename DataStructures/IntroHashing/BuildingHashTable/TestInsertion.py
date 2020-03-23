from DataStructures.IntroHashing.BuildingHashTable.HashTable import HashTable

ht = HashTable()
ht.insert(2, "London")
# Collides with (2, "London") - Added next to it at the same index
ht.insert(12, "Moscow")
ht.insert(7, "Paris")

print("Size of the list: " + str(ht.size))

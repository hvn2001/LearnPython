from DataStructures.IntroHeap.MaxHeap import MaxHeap

heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())

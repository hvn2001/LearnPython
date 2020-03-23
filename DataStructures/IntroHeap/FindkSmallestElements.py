from DataStructures.IntroHeap.MinHeap import MinHeap


def findKSmallest(lst, k):
    heap = MinHeap()  # Create a minHeap
    # Populate the minHeap with lst elements
    heap.buildHeap(lst)
    # Create a list of k elements such that:
    # It contains the first k elements from
    # removeMin() function
    kSmallest = [heap.removeMin() for i in range(k)]
    return kSmallest


print(findKSmallest([9, 4, 7, 1, -2, 6, 5], 3))  # [-2, 1, 4]

'''
The time complexity of creating a heap is O(n) and removing min is O(klogn). 
So the total time complexity is O(n + klogn) which is basically O(klogn).
'''

import heapq

heap = []  # Empty heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 70)
heapq.heappush(heap, 5)
heapq.heappush(heap, 35)
heapq.heappush(heap, 50)

# Popping the smallest value
minimum = heapq.heappop(heap)
print(minimum)

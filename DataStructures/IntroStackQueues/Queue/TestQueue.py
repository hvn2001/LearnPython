from DataStructures.IntroStackQueues.Queue.Queue import myQueue

queue = myQueue()

print("queue.enqueue(2);")
queue.enqueue(2)
print("queue.enqueue(4);")
queue.enqueue(4)
print("queue.enqueue(6);")
queue.enqueue(6)
print("queue.enqueue(8);")
queue.enqueue(8)
print("queue.enqueue(10);")
queue.enqueue(10)

print("Dequeue(): " + str(queue.dequeue()))
print("Dequeue(): " + str(queue.dequeue()))

print("front(): " + str(queue.front()))
print("back(): " + str(queue.back()))

print("queue.enqueue(12);")
queue.enqueue(12)
print("queue.enqueue(14);")
queue.enqueue(14)

while queue.isEmpty() is False:
    print("Dequeue(): " + str(queue.dequeue()))

print("isEmpty(): " + str(queue.isEmpty()))

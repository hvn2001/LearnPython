# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue
from DataStructures.IntroStackQueues.Queue.Queue import myQueue
from DataStructures.IntroStackQueues.Stack.Stack import myStack


def reverseK(queue, k):
    if queue.isEmpty() is True or k > queue.size() or k < 0:
        # Handling invalid input
        return None

    stack = myStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty() is False:
        queue.enqueue(stack.pop())

    size = queue.size()

    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue


# testing our logic
queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print("the queue before reversing:")
print(queue.queueList)
reverseK(queue, 5)
print("the queue after reversing:")
print(queue.queueList)

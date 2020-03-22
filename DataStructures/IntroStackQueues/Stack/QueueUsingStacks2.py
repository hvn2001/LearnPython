from Stack import myStack


# We can use 2 stacks for this purpose,mainStack to store original values
# and tempStack which will help in enqueue operation.
# Main thing is to put first entered element at the top of mainStack
class newQueue:
    def __init__(self):
        # Can use size from argument to create stack
        self.mainStack = myStack()
        self.tempStack = myStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into mainStack in O(1)
        self.mainStack.push(value)
        print(str(value) + " enqueued")
        return True

    # Removes Element From Queue
    def dequeue(self):
        # If both stacks are empty, end operation
        if self.tempStack.isEmpty():
            if self.mainStack.isEmpty():
                return None
            # Transfer all elements to tempStack
            while not self.mainStack.isEmpty():
                value = self.mainStack.pop()
                self.tempStack.push(value)
        # Pop the first value. This is the oldest element in the queue
        temp = self.tempStack.pop()
        print(str(temp) + " dequeued")
        return temp


queue = newQueue()
for i in range(5):
    queue.enqueue(i + 1)

print("----------")

for i in range(5):
    queue.dequeue()

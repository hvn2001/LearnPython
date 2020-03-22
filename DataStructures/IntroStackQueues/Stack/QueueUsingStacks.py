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
        if self.mainStack.isEmpty() and self.tempStack.isEmpty():
            self.mainStack.push(value)
            print(str(value) + "init main enqueued")
            return True
        else:
            while self.mainStack.isEmpty() is False:
                tmep = self.mainStack.pop()
                self.tempStack.push(tmep)
            self.mainStack.push(value)
            print(str(value) + "temp enqueued")
            while self.tempStack.isEmpty() is False:
                temp = self.tempStack.pop()
                self.mainStack.push(temp)
            return True

    # Removes Element From Queue
    def dequeue(self):
        if not self.mainStack.isEmpty():
            value = self.mainStack.pop()
            print(str(value) + "main dequeued")
            return value
        # If stack empty then return None
        return None

queue = newQueue()
for i in range(5):
    queue.enqueue(i+1)

print("----------")

for i in range(5):
    queue.dequeue()

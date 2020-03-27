class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):

        while len(self.stack1) != 0:
            temp = self.stack1[-1]
            self.stack1.pop()
            self.stack2.append(temp)

        self.stack1.append(data)

        while len(self.stack2) != 0:
            temp = self.stack2[-1]
            self.stack2.pop()
            self.stack1.append(temp)

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def dequeue(self):

        if self.is_empty():
            return -1;

        val = self.stack1[-1]
        self.stack1.pop()

        return val


qs = QueueUsingStack()
print("dequeue()" + " = " + str(qs.dequeue()))
qs.enqueue(3)
qs.enqueue(6)
qs.enqueue(16)
print("dequeue()" + " = " + str(qs.dequeue()))
qs.enqueue(8);
qs.enqueue(4);
print("dequeue()" + " = " + str(qs.dequeue()))

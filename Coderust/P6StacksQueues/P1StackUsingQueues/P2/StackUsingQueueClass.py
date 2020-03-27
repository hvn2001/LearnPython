from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, data):
        if len(self.queue1) == 0:
            self.queue1.append(data)
        else:
            self.queue2.append(data)
            while len(self.queue1) != 0:
                self.queue2.append(self.queue1.popleft())
            self.swap_queues()

    def is_empty(self):
        return len(self.queue1) + len(self.queue2) == 0;

    def pop(self):
        if self.is_empty():
            return -1;
        return self.queue1.popleft();

    def swap_queues(self):
        self.queue3 = self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.queue3


sq = StackUsingQueue()
print("Pop(): " + str(sq.pop()))
sq.push(3)
sq.push(5)
sq.push(9)
print("Pop(): " + str(sq.pop()))
sq.push(10);
sq.push(16);
print("Pop(): " + str(sq.pop()))

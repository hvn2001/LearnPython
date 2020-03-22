from DataStructures.IntroStackQueues.Queue.Queue import myQueue


def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result  # For number = 3 , result = {"1","10","11"}


print(findBin(2))
print(findBin(3))

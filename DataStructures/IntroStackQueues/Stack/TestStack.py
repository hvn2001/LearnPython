from DataStructures.IntroStackQueues.Stack.Stack import myStack

stack = myStack()
for i in range(5):  # Pushing values in
    stack.push(i)

print("top(): " + str(stack.top()))

for x in range(5):  # Removing values
    print('pop(): ', stack.pop())

print("isEmpty(): " + str(stack.isEmpty()))  # Checking if its empty

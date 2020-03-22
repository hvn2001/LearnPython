from DataStructures.IntroLinkedLists.LinkedList import LinkedList


# 1: Using a Set/List
def detect_loop(lst):
    # Used to store nodes which we already visited
    visited_nodes = []
    current_node = lst.get_head()

    # Traverse the list and put each node in the visitedNodes list
    # and if a node appears twice in the map
    # then it means there is a loop in the list
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.append(current_node)  # Insert node in visitedNodes list
        current_node = current_node.next_element
    return False


# ------------------------------


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

head = lst.get_head()
node = lst.get_head()

# Adding a loop
for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))


# 2: Floyd’s Cycle-Finding
# Floyd's Cycle Finding Algorithm
def detect_loop2(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False


# ----------------------


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

head = lst.get_head()
node = lst.get_head()

# Adding a loop
for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop2(lst))

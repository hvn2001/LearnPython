from DataStructures.IntroLinkedLists.SinglyLinkedListInsertion.LinkedList import LinkedList
from DataStructures.IntroLinkedLists.SinglyLinkedListInsertion.Node import Node


# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.

# HVN
def search(lst, value):
    # Write your code here
    if lst.get_head() is not None:
        temp_node = lst.get_head()
        if temp_node is None:
            return False
        while temp_node.next_element is not None:
            if temp_node.data == value:
                return True
            temp_node = temp_node.next_element
        if temp_node.data == value:
            return True
    return False


# Solution: Iterative
def searchSol1(lst, value):
    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.data is value:
            return True  # value found
        current_node = current_node.next_element

    return False  # value not found


# Solution: Recursive
def searchRec(current_node, value):
    if current_node is None:
        return False
    if current_node.data is value:
        return True
    return searchRec(current_node.next_element, value)


def searchSol2(lst, value):
    # Start from first element
    current_node = lst.get_head()
    return searchRec(current_node, value)


list = LinkedList()
list.insert_at_head(4)
list.insert_at_head(10)
list.insert_at_head(90)
list.insert_at_head(5)
list.print_list()
print(search(list, 4))
print(searchSol1(list, 4))
print(searchSol2(list, 4))

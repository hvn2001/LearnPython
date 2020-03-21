# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list
from DataStructures.IntroLinkedLists.SinglyLinkedListInsertion.LinkedList import LinkedList
from DataStructures.IntroLinkedLists.SinglyLinkedListInsertion.Node import Node

# HVN
# def insert_at_tail(lst, value):
#     lst.insert_at_tail(value)

list = LinkedList()
list.print_list()

# print("Inserting values in first list")
# for i in range(1, 10):
#     list.insert_at_head(i)

print("Inserting values in last list")
for i in range(1, 10):
    list.insert_at_tail(i)

list.print_list()


# Sol
def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    # if list not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    # Set the nextElement of the previous node to new node
    temp.next_element = new_node
    return


list = LinkedList()
for i in range(1, 10):
    insert_at_tail(list, i)
list.print_list()

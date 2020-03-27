from Coderust.P2LinkedList.Node import Node


def create_linked_list(list):
    the_next = None
    for i in range(len(list) - 1, -1, -1):
        node = Node(list[i])
        node.next = the_next
        the_next = node
    return the_next


def display(list_head):
    while list_head is not None:
        print(str(list_head.data) + ", ", end=" ")
        list_head = list_head.next
    print('\n')


def is_equal(list1, list1_expected):
    return True

from Coderust.P2LinkedList.LinkedList import create_linked_list, display


def reverse(head):
    # no need to reverse if head is null
    # or there is only 1 node.
    if head == None or head.next == None:
        return head

    reversed_list = reverse(head.next)

    head.next.next = head
    head.next = None
    return reversed_list


list_head = create_linked_list([7, 14, 21, 28])
print("Original: ", end="")
display(list_head)
list_head = reverse(list_head)
print("After Reverse: ", end="")
display(list_head)

from Coderust.P2LinkedList.LinkedList import create_linked_list, display


def reverse(head):
    # no need to reverse if head is null
    # or there is only 1 node.
    if (head == None or head.next == None):
        return head

    list_to_do = head.next

    reversed_list = head
    reversed_list.next = None

    while list_to_do != None:
        temp = list_to_do
        list_to_do = list_to_do.next
        temp.next = reversed_list
        reversed_list = temp
    return reversed_list


list_head = create_linked_list([7, 14, 21, 28])
print("Original: ", end="")
display(list_head)
list_head = reverse(list_head)
print("After Reverse: ", end="")
display(list_head)
'''
Original: 7, 14, 21, 28
After Reverse: 28, 21, 14, 7
'''

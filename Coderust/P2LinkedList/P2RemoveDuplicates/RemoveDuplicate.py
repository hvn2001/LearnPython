from Coderust.P2LinkedList.LinkedList import create_linked_list, display, is_equal


def remove_duplicates(head):
    if head == None:
        return head

    dup_set = set()
    dup_set.add(head.data)
    curr = head

    while curr.next != None:
        if curr.next.data in dup_set:
            # Duplicate node found. Let's remove it from the list.
            curr.next = curr.next.next
        else:
            # Element not found in map, let's add it.
            dup_set.add(curr.next.data)
            curr = curr.next

    return head


array1 = [4, 7, 4, 9, 7, 11, 4]
array1_expected = [4, 7, 9, 11]
list1 = create_linked_list(array1)
list1_expected = create_linked_list(array1_expected)
print("Original: ", end="")
display(list1)
list1 = remove_duplicates(list1)
print("After removing duplicates: ", end="")
display(list1)
assert is_equal(list1, list1_expected)

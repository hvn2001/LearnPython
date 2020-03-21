from DataStructures.IntroLinkedLists.SinglyLinkedListInsertion.LinkedList import LinkedList


def delete_at_head(lst):
    # Get Head and firstElement of List
    first_element = lst.get_head()

    # if List is not empty then link head to the
    # nextElement of firstElement.
    if first_element is not None:
        lst.head_node = first_element.next_element
        first_element.next_element = None
    return


lst = LinkedList()
for i in range(11):
    lst.insert_at_head(i)

lst.print_list()

delete_at_head(lst)
delete_at_head(lst)

lst.print_list()

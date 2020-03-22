from DataStructures.IntroLinkedLists.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    # Insertion at Head
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list

    def insert_at_tail(self, value):
        temp_node = Node(value)
        temp = self.head_node
        if temp is None:
            self.head_node = temp_node
            return
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = temp_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

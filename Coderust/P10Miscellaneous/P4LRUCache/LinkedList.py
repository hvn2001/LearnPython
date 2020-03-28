from Coderust.P10Miscellaneous.P4LRUCache.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.size = 0

    def get_head(self):
        return self.head_node

    # Insertion at Head
    '''
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list
    '''

    def insert_at_tail(self, key, value):
        temp_node = Node(key, value)
        temp = self.head_node
        self.size = self.size + 1
        if temp is None:
            self.head_node = temp_node
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = temp_node

    def remove_head(self):
        temp = self.head_node
        self.head_node = self.head_node.next
        temp.next = None
        self.size = self.size - 1

    def remove(self, val):
        before = None
        temp = self.head_node
        if temp is None:
            return
        while temp is not None:
            if temp.data == val:
                break
            before = temp
            temp = temp.next
        if temp == self.head_node:
            self.head_node = self.head_node.next
            temp.next = None
            self.size = self.size - 1
            return
        if temp is not None:
            before.next = temp.next
            temp.next = None
            self.size = self.size - 1

    def size(self):
        return self.size

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
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, "-> None")
        return True

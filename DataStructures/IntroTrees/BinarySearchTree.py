# use `Node` class from Node.py
from DataStructures.IntroTrees.Node import Node


class BinarySearchTree:
    def __init__(self, val):  # Initializes a root node
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True
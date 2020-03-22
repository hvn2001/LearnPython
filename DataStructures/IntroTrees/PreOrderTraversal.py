from DataStructures.IntroTrees.BinarySearchTree import BinarySearchTree
from DataStructures.IntroTrees.Print import display


def preOrderPrint(node):
    if node is not None:
        print(node.val)
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

display(BST.root)
preOrderPrint(BST.root)

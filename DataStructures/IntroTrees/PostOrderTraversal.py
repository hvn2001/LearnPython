from DataStructures.IntroTrees.BinarySearchTree import BinarySearchTree
from DataStructures.IntroTrees.Print import display


def postOrderPrint(node):
    if node is not None:
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
display(BST.root)
postOrderPrint(BST.root)

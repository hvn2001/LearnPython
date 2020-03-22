from DataStructures.IntroTrees.BinarySearchTree import BinarySearchTree


def findMin(root):
    if (root is None):  # check for None
        return None
    while root.leftChild:  # Traverse until the last child
        root = root.leftChild
    return root.val  # return the last child


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))


def findMinRecursive(root):
    if root is None:  # check if root exists
        return None
    elif root.leftChild is None:  # check if left child exists
        return root.val  # return if not left child
    else:
        return findMinRecursive(root.leftChild)  # recurse onto the left child


BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMinRecursive(BST.root))

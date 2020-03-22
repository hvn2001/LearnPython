from DataStructures.IntroTrees.BinarySearchTree import BinarySearchTree


# Using a recursive helper function

def findAncestors(root, k):
    result = []
    recfindAncestors(root, k, result)  # recursively find ancestors
    return str(result)  # return a string of ancestors


def recfindAncestors(root, k, result):
    if root is None:  # check if root exists
        return False
    elif root.val is k:  # check if val is k
        return True
    recur_left = recfindAncestors(root.leftChild, k, result)
    recur_right = recfindAncestors(root.rightChild, k, result)
    if recur_left or recur_right:
        # if recursive find in either left or right sub tree
        # append root value and return true
        result.append(root.val)
        return True
    return False  # return false if all failed


BST = BinarySearchTree(6)
BST.insert(1)
BST.insert(133)
BST.insert(12)
print(findAncestors(BST.root, 12))

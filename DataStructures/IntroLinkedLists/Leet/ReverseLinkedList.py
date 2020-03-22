# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # To reverse linked, we need to keep track of three things
        previous_node = None  # Maintain track of the previous node
        current = head  # The current node
        next_node = None  # The next node in the list

        # Reversal
        while current:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node

        # Set the last element as the new head node
        head = previous_node
        return head


def print_list(node):
    if node is None:
        print("List is Empty")
        return False
    temp = node
    while temp.next is not None:
        print(temp.val, end=" -> ")
        temp = temp.next
    print(temp.val, "-> None")
    return True


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
node1.next.next.next.next = ListNode(5)
sol = Solution()
print_list(node1)
print_list(sol.reverseList(node1))

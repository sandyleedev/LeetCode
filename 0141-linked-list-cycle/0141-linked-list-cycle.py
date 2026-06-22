# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        nodes = set()
        curr_node = head

        # if next node's value is already in the set, return True
        # if it's not and None, 

        # next exists and value not in set
        while curr_node.next and not curr_node in nodes:
            nodes.add(curr_node)
            curr_node = curr_node.next

        if curr_node in nodes:
            return True

        return False
        

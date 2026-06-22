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

        while curr_node:
            if curr_node in nodes:
                return True
            nodes.add(curr_node)
            curr_node = curr_node.next
        
        return False
        

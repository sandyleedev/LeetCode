# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        ele = set()

        while head:
            if head in ele:
                return True
            else:
                ele.add(head)
                head = head.next

        return False

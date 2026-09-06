# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # store the inorder value:index in the hashmap
        # to locate easily later

        inorder_map = {}

        for i, value in enumerate(inorder):
            inorder_map[value] = i
        
        curr_pre_index = 0

        def build(left, right):
            nonlocal curr_pre_index

            if left > right:
                return None

            root_value = preorder[curr_pre_index]
            curr_pre_index += 1

            # make root node
            root = TreeNode(root_value)
            mid_index = inorder_map[root_value]

            root.left = build(left, mid_index - 1)
            root.right = build(mid_index + 1, right)

            return root
        
        return build(0, len(preorder) - 1)





            


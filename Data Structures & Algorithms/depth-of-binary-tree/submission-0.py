# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0  

        def traverse(node, current_depth):
            nonlocal max_d
            if not node:
                return
        
            max_d = max(max_d, current_depth)
            
            traverse(node.left, current_depth + 1)
            traverse(node.right, current_depth + 1)

        traverse(root, 1)
        return max_d
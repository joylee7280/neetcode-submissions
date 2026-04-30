# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node):
            if node.left == None and node.right == None:
                return
            elif node.left and node.right:
                temp = node.left
                node.left = node.right
                node.right = temp
                traverse(node.left)
                traverse(node.right)
                return
            elif node.left == None:
                node.left = node.right
                node.right = None
                traverse(node.left)
            elif node.right == None:
                node.right = node.left
                node.left = None
                traverse(node.right)
        if root:
            traverse(root)
        return root

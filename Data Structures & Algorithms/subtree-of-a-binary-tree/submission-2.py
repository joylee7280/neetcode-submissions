# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            left_match = same(node1.left, node2.left)
            right_match = same(node1.right, node2.right)
            return left_match and right_match
        def traverse(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot:
                return False
            elif root.val == subRoot.val:
                if same(root, subRoot) == True:
                    return True
                else:
                    return traverse(root.left, subRoot) or traverse(root.right,subRoot)
            else:
                return traverse(root.left, subRoot) or traverse(root.right,subRoot)
        return traverse(root, subRoot)
        
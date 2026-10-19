# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_val = float('-inf')

        def dfs(node):
            nonlocal prev_val

            if not node:
                return True
            
            if not dfs(node.left):
                return False
            
            if node.val <= prev_val:
                return False

            prev_val = node.val

            return dfs(node.right)
        return dfs(root)
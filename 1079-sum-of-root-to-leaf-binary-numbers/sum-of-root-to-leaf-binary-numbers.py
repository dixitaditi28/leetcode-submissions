# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Build the binary number
            current = current * 2 + node.val
            
            # If it's a leaf, return the number
            if not node.left and not node.right:
                return current
            
            # Otherwise sum left and right paths
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)
        
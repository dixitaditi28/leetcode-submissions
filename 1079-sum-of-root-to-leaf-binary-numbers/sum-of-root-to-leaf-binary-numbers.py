class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, path):
            if not node:
                return
                
            if not node.left and not node.right:
                self.total += int(path + str(node.val), 2)
                return

            new_path = path + str(node.val)
            dfs(node.left, new_path)
            dfs(node.right, new_path)
        dfs(root, '')
        return self.total
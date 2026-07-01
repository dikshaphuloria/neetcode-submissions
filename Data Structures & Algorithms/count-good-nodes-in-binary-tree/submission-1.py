# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1

        def dfs(node, value):
            if not node:
                return 0

            if node.val >= value:
                self.count+=1
            
            value = max(value, node.val)
            dfs(node.right, value)
            dfs(node.left, value)

        dfs(root.right, root.val)
        dfs(root.left, root.val)
        return self.count


            



        
        
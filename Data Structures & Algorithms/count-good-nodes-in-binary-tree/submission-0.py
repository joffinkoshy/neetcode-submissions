# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0

        def helper(node,prev):
            nonlocal ans
            if not node:
                return

            if node.val>=prev:
                ans+=1
                prev=node.val

            if node.left:
                helper(node.left,prev)

            if node.right:
                helper(node.right,prev)


        helper(root,-float('inf'))
        return ans


        
        
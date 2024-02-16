# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        levels = {}

        def traverse(node, level):
            if not node:
                return None
            if level not in levels:
                levels[level] = node.val
            else:
                if node.val >= levels[level]:
                    levels[level] = node.val
            
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        

        traverse(root, 1)
        return levels.values()
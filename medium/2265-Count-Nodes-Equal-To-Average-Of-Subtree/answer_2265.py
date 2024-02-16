# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def traverse(node):
            nonlocal ans

            if not node:
                return 0, 0
            
            left_travel_sum, left_travel_count = traverse(node.left)
            right_travel_sum, right_travel_count = traverse(node.right)

            total = node.val + left_travel_sum + right_travel_sum
            count = 1 + left_travel_count + right_travel_count

            if total // count == node.val:
                ans += 1
            
            return total, count
        
        traverse(root)
        return ans
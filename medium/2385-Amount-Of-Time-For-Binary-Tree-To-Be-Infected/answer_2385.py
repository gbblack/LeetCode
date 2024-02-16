# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def dfs(node):
            if node is None:
                return
            if node.left:
                spread[node.val].append(node.left.val)
                spread[node.left.val].append(node.val)
            if node.right:
                spread[node.val].append(node.right.val)
                spread[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        spread = defaultdict(list)
        dfs(root)
        visited = set()

        queue = deque([start])
        mins = -1

        while queue:
            mins +=1
            for _ in range(len(queue)):
                x = queue.popleft()
                visited.add(x)
                for j in spread[x]:
                    if j not in visited:
                        queue.append(j)
        
        return mins
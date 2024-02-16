class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        stack = []
        compare = []
        
        for i in range(1, n+1):
            if i in target:
                stack.append('Push')
                compare.append(i)
                if compare == target:
                    break
            else:
                stack.append('Push')
                stack.append('Pop')
        
        return stack
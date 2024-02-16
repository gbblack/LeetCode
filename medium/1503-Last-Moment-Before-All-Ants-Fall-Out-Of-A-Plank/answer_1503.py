class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int: 
        if not left:
            left_max = 0
        else:
            left_max = max(left)
        if not right:
            right_max = n - n
        else:
            right_max = n - min(right)
        
        return max(left_max, right_max)
        
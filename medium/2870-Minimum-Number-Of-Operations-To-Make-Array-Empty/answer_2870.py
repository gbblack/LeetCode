class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        operations_total = 0

        if 1 in list(count.values()):
            return -1
        else:
            for k, v in count.items():
                operations_total += v // 3
                if v % 3:
                    operations_total += 1
        
        return operations_total
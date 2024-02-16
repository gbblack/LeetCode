class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = []

        res.append(nums[0])

        for i in range(1, n):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                left = 0
                right = len(res) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if res[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                res[left] = nums[i]
        
        return len(res)
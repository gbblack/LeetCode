class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for elem in range(0, len(nums)-1):
            
            if nums[elem] == nums[elem+1]:
                count += 1
            else:
                count = 0
            
            if count >= 2:
                nums[elem] = "ugh"
            
        while "ugh" in nums: nums.remove("ugh")
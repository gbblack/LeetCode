class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        i = 0
        j = 0
        max_dist = 0
        
        while i < len(nums1):
            if j < len(nums2) and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j-i)
                j += 1
            else:
                i += 1
                j += 1

        return max_dist
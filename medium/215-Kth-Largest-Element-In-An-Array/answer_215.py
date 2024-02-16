class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k_array = []

        for i in nums:
            if len(k_array) < k:
                heapq.heappush(k_array, i)
            else:
                if i > k_array[0]:
                    heapq.heappushpop(k_array, i)
        return heapq.heappop(k_array)
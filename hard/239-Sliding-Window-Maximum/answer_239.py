class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        dq = deque()
        for i in range(0, len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            while dq and i - dq[0] >= k:
                dq.popleft()
            if i >=k - 1:
                result.append(nums[dq[0]])
        return result
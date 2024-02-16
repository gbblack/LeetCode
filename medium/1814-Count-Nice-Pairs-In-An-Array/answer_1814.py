class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        def reverse(num):
            rev = 0
            while num > 0:
                rev = rev * 10 + num % 10
                num //= 10
            return rev
        
        freq = {}

        for num in nums:
            r = num-reverse(num)
            if r not in freq:
                freq[r] = 1
            else:
                freq[r] += 1
        
        res = 0

        for f in freq.keys():
            total = freq[f]
            res = (res + (total*(total-1))//2)%mod
        
        return res

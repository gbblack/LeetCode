class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        uniques = set(arr)

        dp = {x: 1 for x in arr}

        mod = 10**9 + 7

        for i in arr:
            for j in arr:
                if i % j == 0 and i // j in uniques:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j]
                    dp[i] %= mod
        return sum(dp.values()) % mod
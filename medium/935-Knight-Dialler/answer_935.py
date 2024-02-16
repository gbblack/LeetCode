class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7

        paths = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
            }

        dp = [[0] * 10 for _ in range(n+1)]

        for cell in range(10):
            dp[0][cell] = 1
        for remain in range(1, n):
            for cell in range(10):
                ans = 0
                for next_cell in paths[cell]:
                    ans = (ans + dp[remain - 1][next_cell]) % mod
                
                dp[remain][cell] = ans
        ans = 0

        for cell in range(10):
            ans = (ans + dp[n - 1][cell]) % mod
        
        return ans
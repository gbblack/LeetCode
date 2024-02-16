class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        k, rem_3 = divmod(n, 3)
        if rem_3 == 1:
          return 3**(k-1) * (3+1)
        l, rem_2 = divmod(rem_3, 2)
        return 3**k * 2**l
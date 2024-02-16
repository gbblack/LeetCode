class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        res = 0

        for letter in letters:
            left = s.find(letter)
            right = s.rfind(letter)

            between = set(s[left+1 : right])

            res += len(between)
        
        return res

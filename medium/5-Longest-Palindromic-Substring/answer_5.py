class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_length = 1
        res = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if j-i+1 > max_length and res[i:j+1] == s[i:j+1][::-1]:
                    max_length = j-i+1
                    res = s[i:j+1]
        return res
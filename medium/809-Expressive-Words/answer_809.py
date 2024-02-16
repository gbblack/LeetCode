class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def is_stretchy(stretch, word):
            i = 0
            j = 0

            while i < len(stretch) and j < len(word):

                if stretch[i] != word[j]:
                    return False
                
                len_s = 1
                while i + 1 < len(stretch) and stretch[i] == stretch[i + 1]:
                    i += 1
                    len_s += 1
                
                len_w = 1
                while j + 1 < len(word) and word[j] == word[j + 1]:
                    j += 1
                    len_w += 1
                
                if (len_s != len_w and len_s < 3) or len_s < len_w:
                    return False

                i += 1
                j += 1
            
            return i == len(stretch) and j == len(word)
        
        return sum(is_stretchy(s, word) for word in words)
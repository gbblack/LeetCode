class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count_s = defaultdict(list)
        
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            count_s[sortedWord].append(strs[i])

        print(count_s.values())
        return count_s.values()
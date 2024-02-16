class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        unique = set()
        
        sorted_freqs = sorted(cnt.values(), reverse=True)
        
        for freq in sorted_freqs:
            if freq not in unique:
                unique.add(freq)
                continue

            while freq > 0 and freq in unique:
                freq -= 1
                deletions += 1

            unique.add(freq)
            
        return deletions
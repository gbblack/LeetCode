class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        prs = [0]
        
        for time in travel:
            prs.append(prs[-1] + time)

        trucks = {}
        
        for house, g in enumerate(garbage):
            for c in g:
                trucks[c] = prs[house]
        
        return sum(trucks.values()) + sum(map(len, garbage))
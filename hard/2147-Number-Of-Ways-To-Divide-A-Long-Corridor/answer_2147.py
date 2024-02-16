class Solution:
    def numberOfWays(self, corridor: str) -> int:

        mod = 10 ** 9 + 7
        seat = 0
        plant = 0
        num_divides = 1
        
        for i in corridor:
            if i == 'S':
                seat += 1
            else:
                if seat == 2:
                    plant += 1
            if seat == 3:
                num_divides = num_divides*(plant+1) % mod
                seat, plant = 1, 0
            
        if seat != 2:
            return 0
        return num_divides
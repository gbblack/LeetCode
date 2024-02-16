class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = [[] for row in range(numRows)]

        index = 0
        step = 1

        for letter in s:
            rows[index].append(letter)
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
            
        for r in range(0, numRows):
            rows[r] = "".join(rows[r])
        
        return "".join(rows)
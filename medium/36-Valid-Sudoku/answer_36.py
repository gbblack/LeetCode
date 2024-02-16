class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stats = []

        for row in range(0,9):
            for col in range(0, 9):
                element = board[row][col]
                if element != '.':
                    stats += [(row, element), (element, col), (row // 3, col // 3, element)]
        
        if len(stats) == len(set(stats)):
            return True
        else:
            return False
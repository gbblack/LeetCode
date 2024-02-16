class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k == 1:
            winner = max(arr[0], arr[1])
            return winner
        
        curr_winner = arr[0]
        multi_wins = 0

        for i in range(1, len(arr)):
            if curr_winner > arr[i]:
                multi_wins += 1
            else:
                curr_winner = arr[i]
                multi_wins = 1
            if multi_wins == k:
                return curr_winner
        
        return curr_winner
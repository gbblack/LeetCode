class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        flag = False
        n = len(arr)

        if n == 1:
            return 1

        for i in range(n - 1):
            if arr[i] > arr[i+1] or arr[i+1] - arr[i] > 1 or arr[0] != 1:
                flag = True
                break
        
        if not flag:
            return arr[n - 1]

        arr.sort()

        for i in range(n):
            if i == 0 and arr[0] != 1:
                arr[0] = 1
            elif i > 0 and arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        
        return arr[n - 1]
        
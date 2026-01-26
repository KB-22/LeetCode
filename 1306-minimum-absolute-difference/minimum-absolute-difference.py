from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        min_diff = float('inf')
        n = len(arr)
        
        # Find minimum difference
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        
        result = []
        # Collect pairs with minimum difference
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result

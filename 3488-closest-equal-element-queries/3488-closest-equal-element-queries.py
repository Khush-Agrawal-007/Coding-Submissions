from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Store naturally sorted indices for each number
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
            
        # Initialize the answers for all indices in the array to -1
        ans = [-1] * n
        
        # Step 2: Precompute the minimum distance for each valid index
        for arr in pos.values():
            m = len(arr)
            
            # If the element appears only once, we leave its answer as -1
            if m == 1:
                continue
            
            # The circular distance between the first and last occurrence
            wrap_dist = n - arr[-1] + arr[0]
            
            for k in range(m):
                # Distance to the previous identical element
                prev_dist = arr[k] - arr[k-1] if k > 0 else wrap_dist
                    
                # Distance to the next identical element
                next_dist = arr[k+1] - arr[k] if k < m - 1 else wrap_dist
                    
                # The minimum of looking backward vs. looking forward
                ans[arr[k]] = min(prev_dist, next_dist)
                
        # Step 3: Fetch results for the requested queries
        return [ans[q] for q in queries]
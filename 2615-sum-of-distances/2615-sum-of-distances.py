from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Step 1: Map each number to a list of its indices
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
        
        ans = [0] * len(nums)
        
        # Step 2: Calculate distances for each group of indices
        for indices in indices_map.values():
            n = len(indices)
            if n == 1:
                continue
                
            # Calculate the total distance for the first index in the group
            current_ans = sum(indices) - n * indices[0]
            ans[indices[0]] = current_ans
            
            # Step 3: Compute distances for the rest of the indices using a running difference
            for i in range(n - 1):
                diff = indices[i+1] - indices[i]
                
                # elements_left: number of matching elements at or before the current index
                # elements_right: number of matching elements strictly after the current index
                elements_left = i + 1
                elements_right = n - 1 - i
                
                # Update distance based on how many elements we moved closer to or further from
                current_ans += elements_left * diff - elements_right * diff
                ans[indices[i+1]] = current_ans
                
        return ans
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        
        # Step 1: Cyclic Sort - Place numbers in their correct indices
        while i < n:
            correct_idx = nums[i] - 1
            
            # Check conditions:
            # 1. 0 < nums[i] <= n: The number is positive and fits in the array bounds
            # 2. nums[i] != nums[correct_idx]: The number is not already at the correct spot
            #    (This check also handles duplicates preventing infinite loops)
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # Swap current number to its correct position
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # If current number is out of range or already placed, move to next
                i += 1
        
        # Step 2: Find the first index that doesn't match
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers 1..n are present, the answer is n+1
        return n + 1
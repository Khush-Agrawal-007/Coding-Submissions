class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        array_sum = sum(nums)
        
        # Calculate initial F(0)
        current_f = sum(i * num for i, num in enumerate(nums))
        max_f = current_f
        
        # Calculate F(1) to F(n-1) using the recurrence relation
        for k in range(1, n):
            current_f = current_f + array_sum - (n * nums[n - k])
            max_f = max(max_f, current_f)
            
        return max_f
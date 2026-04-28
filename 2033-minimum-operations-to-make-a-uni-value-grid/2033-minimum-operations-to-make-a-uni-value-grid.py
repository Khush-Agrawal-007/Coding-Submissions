class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Flatten the 2D grid into a 1D list
        nums = [val for row in grid for val in row]
        
        # Check for feasibility: 
        # All numbers must have the same remainder when divided by x
        remainder = nums[0] % x
        for n in nums:
            if n % x != remainder:
                return -1
        
        # Sort to find the median (which minimizes the sum of absolute differences)
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Calculate total operations to make all elements equal to the median
        operations = sum(abs(n - median) // x for n in nums)
        
        return operations
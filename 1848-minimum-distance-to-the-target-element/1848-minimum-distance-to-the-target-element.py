class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        
        # Iterate through the array with both index (i) and value (num)
        for i, num in enumerate(nums):
            if num == target:
                # Calculate the absolute distance and update the minimum
                min_dist = min(min_dist, abs(i - start))
                
        return min_dist
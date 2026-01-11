class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Set the initial target to the last index of the array
        goal = len(nums) - 1
        
        # Iterate backwards from the last index down to 0
        for i in range(len(nums) - 1, -1, -1):
            # Check if we can jump from current index 'i' to the 'goal'
            # i + nums[i] represents the furthest index we can reach from i
            if i + nums[i] >= goal:
                # If we can reach the goal, shift the goal closer to the start
                goal = i
                
        # If the goal has shifted all the way to index 0, it means
        # there is a valid path from the start to the end.
        return goal == 0
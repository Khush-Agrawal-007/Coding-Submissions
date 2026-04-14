class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        # Sort robots and factories by their position
        robot.sort()
        factory.sort()

        # Flatten factories into single available spots based on their limit
        spots = []
        for pos, limit in factory:
            spots.extend([pos] * limit)

        n = len(robot)
        
        # dp[i] will store the min total distance for robots[i:] 
        # using the current suffix of available factory spots.
        dp = [float('inf')] * (n + 1)
        
        # Base case: 0 cost to fix 0 remaining robots
        dp[n] = 0

        # Process each factory spot from right to left
        for spot in reversed(spots):
            # Iterate through robots from left to right
            for i in range(n):
                # We take the minimum between:
                # 1. Skipping the current spot (keeping the old dp[i])
                # 2. Assigning robot[i] to this spot + cost of assigning remaining robots
                dp[i] = min(dp[i], abs(robot[i] - spot) + dp[i + 1])

        # Return the minimum cost to assign all robots (from index 0)
        return dp[0]
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def get_distance(a, b):
            # 26 represents an unplaced finger, cost to place it anywhere is 0
            if a == 26: 
                return 0
            # Convert 1D index to 2D coordinates on the 6x5 keyboard
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        # Convert the string into integer indices (0 to 25)
        nums = [ord(c) - ord('A') for c in word]
        memo = {}

        def dp(i, other_finger):
            # Base case: we have typed the whole word
            if i == len(nums):
                return 0
            
            # Check memoization cache
            if (i, other_finger) in memo:
                return memo[(i, other_finger)]
            
            curr = nums[i]
            # If i == 0, the "previous" finger hasn't been placed yet either
            prev = nums[i-1] if i > 0 else 26
            
            # Option 1: Move the finger currently on 'prev' to 'curr'
            # The 'other_finger' stays where it is
            cost1 = get_distance(prev, curr) + dp(i + 1, other_finger)
            
            # Option 2: Move the 'other_finger' to 'curr'
            # The finger that was on 'prev' now becomes the new 'other_finger'
            cost2 = get_distance(other_finger, curr) + dp(i + 1, prev)
            
            # Record and return the minimum cost of the two choices
            memo[(i, other_finger)] = min(cost1, cost2)
            return memo[(i, other_finger)]

        # Start at index 0, with the "other" finger unplaced (26)
        return dp(0, 26)
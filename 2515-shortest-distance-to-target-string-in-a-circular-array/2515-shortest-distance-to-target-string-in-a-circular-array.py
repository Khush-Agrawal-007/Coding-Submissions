class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        # If the target is not in the array, it's impossible to reach
        if target not in words:
            return -1
        
        n = len(words)
        min_dist = n  # Initialize with maximum possible distance
        
        for i, word in enumerate(words):
            if word == target:
                # Calculate direct distance
                direct_dist = abs(startIndex - i)
                # Calculate wrap-around distance
                wrap_dist = n - direct_dist
                
                # Find the minimum of the two paths and update the global minimum
                current_min = min(direct_dist, wrap_dist)
                min_dist = min(min_dist, current_min)
                
        return min_dist
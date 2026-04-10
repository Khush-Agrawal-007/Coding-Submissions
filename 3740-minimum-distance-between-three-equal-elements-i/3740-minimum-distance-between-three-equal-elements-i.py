class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = []
            indices[num].append(i)
            
        min_dist = float('inf')
        
        # Check consecutive triplets for each unique number
        for pos in indices.values():
            # We need at least 3 occurrences to form a valid tuple
            if len(pos) >= 3:
                for i in range(len(pos) - 2):
                    # Distance simplifies to 2 * (k - i)
                    dist = 2 * (pos[i+2] - pos[i])
                    if dist < min_dist:
                        min_dist = dist
                        
        return min_dist if min_dist != float('inf') else -1
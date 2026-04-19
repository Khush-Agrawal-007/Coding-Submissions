class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i, j = 0, 0
        max_dist = 0
        n, m = len(nums1), len(nums2)
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                # If j < i, distance is negative, max() handles this automatically
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
                
        return max_dist
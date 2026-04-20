class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        
        # Check from the right for a color different from the first house
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                ans1 = j
                break
                
        # Check from the left for a color different from the last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans2 = (n - 1) - i
                break
                
        return max(ans1, ans2)
class Solution(object):
    def rob(self,nums):
        prev_house = 0 # Max loot 2 houses ago
        curr_house = 0 # Max loot 1 house ago
        
        for money in nums:
            # Temp stores the max if we consider the current house
            temp = max(curr_house, prev_house + money)
            prev_house = curr_house
            curr_house = temp
            
        return curr_house
        
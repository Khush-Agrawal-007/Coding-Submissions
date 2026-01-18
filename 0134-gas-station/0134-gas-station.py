class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 1. Global Check: If total gas is less than total cost, 
        # it's impossible to complete the circle.
        if sum(gas) < sum(cost):
            return -1
        
        current_tank = 0
        start_index = 0
        
        # 2. Greedy Search for the starting position
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # If tank becomes negative, we couldn't make it from 'start_index' to 'i'.
            # It also means no station between 'start_index' and 'i' can be the start.
            # So, we try the next station (i + 1) as the new start.
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index
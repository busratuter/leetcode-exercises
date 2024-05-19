from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank, start_index = 0, 0, 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0
        
        return start_index if total_tank >= 0 else -1
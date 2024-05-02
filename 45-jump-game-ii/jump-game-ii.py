class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        max_reachable = nums[0]  
        jumps = 1  
        steps_available = nums[0]  
        
        for i in range(1, n):
            if i == n - 1: 
                return jumps
            
            max_reachable = max(max_reachable, i + nums[i])
            steps_available -= 1
            
            if steps_available == 0:  
                jumps += 1
                steps_available = max_reachable - i
                
        return jumps

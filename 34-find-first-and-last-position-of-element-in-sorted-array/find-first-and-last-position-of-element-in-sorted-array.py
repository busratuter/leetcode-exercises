from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_first):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        first_pos = binary_search(True)
        last_pos = binary_search(False)
        
        return [first_pos, last_pos]



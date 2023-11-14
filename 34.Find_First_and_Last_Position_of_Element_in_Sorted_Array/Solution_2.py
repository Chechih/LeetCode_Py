from typing import List 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target in nums):
            start = nums.index(target)
            return [start, start + nums.count(target) - 1]
        return [-1, -1]
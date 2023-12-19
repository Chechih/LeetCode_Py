from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_leg = len(nums)
        rule = set(range(1, nums_leg + 2))
        diff = rule - set(nums)
        if(len(diff) > 0):
            return min(diff)
        else:
            return 1

slution = Solution()
print(slution.firstMissingPositive([1]))
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(len(nums)):
            if(nums[j] > nums[i - 1]):
                # nums[i - 1]  上一次出現的值
                # 如果比上一次出現的值大
                nums[i], nums[j] = nums[j], nums[i]
                # 互換陣列中兩個值
                i += 1
        return i
    
solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
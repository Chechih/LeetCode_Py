from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rlt = []
        def find_combination_sum(stack: List[int]) -> None:
            if(not nums):
                rlt.append(stack.copy())
            for i in range(len(nums)):
                stack.append(nums[i])
                temp = nums[i]
                nums.remove(temp)
                find_combination_sum(stack)
                nums.insert(i, temp)
                # 加回去 避免 for 迴圈炸掉 且才能檢查其他組合
                stack.pop()

        find_combination_sum([])
        return rlt
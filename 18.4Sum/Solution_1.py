from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_leg = len(nums)
        rlt = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue  # 避免重複解
            for j in range(i + 1, nums_leg - 2):
                nn = nums[j]
                if j > i + 1 and nn == nums[j - 1]:
                    continue  # 避免重複解
                left = j + 1
                right = nums_leg - 1
                processing_target = target - n - nn
                
                while left < right:
                    total = nums[left] + nums[right]
                    if total == processing_target:
                        rlt.append([n, nn, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # 避免重複解
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # 避免重複解
                        left += 1
                        right -= 1
                    elif total < processing_target:
                        left += 1
                    else:
                        right -= 1
            if n *4 > target:# 如果基準點的四倍比目標值大，直接放棄找，因為已經排序過，後面的數字只會越來越大
                break
                    
        return rlt
    
#測試
solution = Solution()
print(solution.fourSum([1,1,1,1,2,2,2,2,2], 8))
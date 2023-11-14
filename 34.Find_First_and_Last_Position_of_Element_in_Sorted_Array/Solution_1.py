from typing import List 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        mid = 0
        rlt = [-1, -1]
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                if (mid == 0 or nums[mid -1] < nums[mid]):
                    # 找左邊
                    rlt[0] = mid
                    break
                else:
                    right -= 1
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        if rlt[0] == -1:
            return rlt
        left = rlt[0]
        # 因為上面找到了 直接用他繼續找
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid +1] > nums[mid]:
                    # 找右邊
                    rlt[1] = mid
                    break
                else:
                    left += 1
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return rlt
    

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
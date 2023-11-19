from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # 先去頭尾這樣就不用特別判斷頭尾了
        while right - left > 1:
            # 一直尋找到相差一
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right



solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
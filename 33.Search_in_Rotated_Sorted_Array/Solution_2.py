from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[right] >= nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
    
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))
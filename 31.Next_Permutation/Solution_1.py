from typing import List

class Solution:
    def swap(self, nums: List[int], ind1: int, ind2: int) -> None:
        '''
        交換
        '''
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_no_increment_num = len(nums) - 2
        # 找到第一個不再遞增的位置
        while (first_no_increment_num >= 0 and nums[first_no_increment_num + 1] <= nums[first_no_increment_num]):
            first_no_increment_num -= 1
        
        # 如果到了最左邊，就直接反向输出
        if (first_no_increment_num < 0):
            nums.reverse()
            return
        
        # 找出剛好大於的位置
        near_max_num = len(nums) - 1
        while (near_max_num >= 0 and nums[near_max_num] <= nums[first_no_increment_num]):
            near_max_num -= 1
        
        self.swap(nums, first_no_increment_num, near_max_num)

        #將後面的值排序成最小的數字
        nums[first_no_increment_num + 1::] = sorted(nums[first_no_increment_num + 1::])

solution = Solution()
print(solution.nextPermutation([1,3,2]))  #[2,1,3]
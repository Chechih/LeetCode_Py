from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        其實這題就是要找最大面積，而他的面積，其實就是由兩個因素決定的，
        1. 下排的寬度(位子相減)
        2. 高度最小值(height 的值)
        所以可以使用雙指標，從左右兩側跑，當指標互相靠近時，盡可能地去找出更大的 height ，去補償寬度邊小
        '''
        height_leg = len(height)
        left = 0
        right = height_leg - 1
        max_area = 0# 存最大面積
        while left < right:
            area = 0
            if height[left] <  height[right]:# 右邊己較高時
                area = height[left] * (right - left)# 左邊當高
                left += 1
            else:# 左邊己較高時
                area = height[right] * (right - left)# 右邊當高
                right -= 1
            max_area = max(max_area, area)

        return max_area

#測試
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
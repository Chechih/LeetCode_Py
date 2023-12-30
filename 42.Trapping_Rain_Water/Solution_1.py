from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        height_leg = len(height)
        left_height = [0] * height_leg
        right_height = [0] * height_leg
        left_height[0] = height[0]
        right_height[height_leg - 1] = height[height_leg - 1]
        for i in range(1, height_leg):
            # 先找出所有的左邊
            left_height[i] = max(left_height[i - 1], height[i])

        for i in range(height_leg - 2, -1, -1):
            # 再找出所有的右邊
            right_height[i] = max(height[i], right_height[i + 1])   

        rlt = 0
        for i in range(1, height_leg - 1):
            # 比較每個位子的左右兩邊並減去現在高度，就是當前的水量
            rlt += min(left_height[i], right_height[i]) - height[i]

        return rlt



solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
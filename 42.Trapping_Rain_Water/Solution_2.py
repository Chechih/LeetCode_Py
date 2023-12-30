from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        height_leg = len(height)

        left, right = 0, height_leg - 1
        left_max, right_max = height[left], height[right]
        rlt = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                rlt += left_max - height[left]
                left += 1
            else:
                rlt += right_max - height[right]
                right -= 1

        return rlt

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
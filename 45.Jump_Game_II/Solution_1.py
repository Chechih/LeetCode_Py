from typing import List

class Solution:
    max_num = 10000
    def jump(self, nums: List[int]) -> int:
        nums_leg = len(nums)
        step_dict = [0] * nums_leg
        # 紀錄這個位子到終點的最少歩數
        if(nums_leg == 1):
            # 在終點上不用走了
            return 0
        # 設定最大值用的
        for i in range(nums_leg - 1, -1, -1):
            max_move = nums[i]
            if(i + max_move >= nums_leg -1):
                # 超過終點直接紀錄 1 步
                step_dict[i] = 1
            elif(max_move == 0):
                # 不可能到達
                step_dict[i] = self.max_num
            else:
                step_dict[i] = min(step_dict[i + 1: i + max_move + 1]) + 1
                # 計算最小步數
        return step_dict[0]

solution = Solution()
print(solution.jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0 ,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5 ,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7 ,5,1,9,9,3,5,0,7,5]))
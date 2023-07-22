from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rlt = [-1, -1]
        numVals_dict = { }#建立值對應到位子的字典
        for numInd, numVal in enumerate(nums): 
            differ = target - numVal#差值
            differ_ind = numVals_dict.get(differ, -1)#取值, 取不到回傳 -1
            if(differ_ind != -1 and differ_ind != numInd):#題目有說相同位子的數字不能用兩次
                rlt = [numInd, differ_ind]
                break
            else:
                numVals_dict[numVal] = numInd
        return rlt

#測試
solution = Solution()
solution.twoSum([3,2,4], 6);
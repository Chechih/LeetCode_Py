# 1. Two Sum
### 問題
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

##### Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
##### Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
##### Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

### 翻譯
給定一個整數數組，返回兩個數字的索引，使它們相加達到特定目標。

您可以假設每個輸入都有一個解決方案。

### 想法
看到題目時，第一個最直接的想法一定是用兩個迴圈下去跑XDD
不過因為他只有兩個數字，可以作弊一下，用一個迴圈下去跑，跑到的那個數字去和目標數字相減，得出的差值檢查看看在不在陣列裡面，就可以得到答案了，不過要小心，相同位子的數字只能用一次。
且檢查時，可以用字典增加速度。

### 解法
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rlt = [-1, -1]
        numVals_dict = { val : idx for idx, val in enumerate(nums) }#建立值對應到位子的字典
        for numInd, numVal in enumerate(nums): 
            differ = target - numVal#差值
            differ_ind = numVals_dict.get(differ, -1)#取值, 取不到回傳 -1
            if(differ_ind != -1 and differ_ind != numInd):#題目有說相同位子的數字不能用兩次
                rlt = [numInd, differ_ind]
                break
        return rlt
```
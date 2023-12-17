# 40. Combination Sum II
### 問題
Given a collection of candidate numbers (**candidates**) and a target number (**target**), find all unique combinations in **candidates** where the candidate numbers sum to **target**.

Each number in **candidates** may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

### 翻譯
給定一個候選數字集合（**candidates**）和一個目標數字（**target**），找出所有在 **candidates** 中，其候選數字總和為 **target** 的獨特組合。

**candidates** 中的每個數字在組合中只能使用一次。

**注意：** 解集不得包含重複的組合。

##### Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

##### Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]

##### Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

### 想法
這題其實和 [39.Combination_Sum](https://chechih.github.io/posts/LeetCode/39.Combination_Sum/) 差不多，差別在於 39 可以種複使用，這題只能使用給的數字，不果解法類似，多了一開始要先統計給定的 candidates 數字有哪些，然後慢慢遞迴消耗掉即可。
### 解法
```python
class Solution:
    def findCombinationSum(self, candidates_dict: Dict[str, int], target: int, ind: int, values: List[int], rlt: List[List[int]]) -> None:
        val_sum = sum(values)
        if(val_sum == target):
            rlt.append(values.copy())
            return
        candidates_keys = list(candidates_dict.keys())
        for i in range(ind, len(candidates_keys)):
            key = candidates_keys[i]
            candidates_dict[key] -= 1
            if(candidates_dict[key] < 0):
                # 如果沒有了
                candidates_dict[key] += 1
                continue
            if(val_sum + key > target):
                # 超過
                candidates_dict[key] += 1
                return
            values.append(key)
            self.findCombinationSum(candidates_dict, target, i, values, rlt)
            candidates_dict[key] += 1
            values.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        candidates.sort()
        candidatesDict = Counter(candidates)
        self.findCombinationSum(candidatesDict, target, 0, [], rlt)
        return rlt
```
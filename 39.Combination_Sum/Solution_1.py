from typing import List

class Solution:
    def findCombinationSum(self, candidates: List[int], target: int, index: int, val_ary: List[int], rlt: List[List[int]]) -> None:
        val_sum = sum(val_ary)
        if(val_sum == target):
            rlt.append(val_ary.copy())
        for i in range(index, len(candidates)):
            if(val_sum + candidates[i] > target):
                return
            val_ary.append(candidates[i])
            self.findCombinationSum(candidates, target, i, val_ary, rlt)
            val_ary.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rlt = []
        candidates.sort()
        self.findCombinationSum(candidates, target, 0, [], rlt)
        return rlt

solution = Solution()
print(solution.combinationSum([2,3,6,7], 7))
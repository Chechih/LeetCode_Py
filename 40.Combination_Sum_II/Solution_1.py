from typing import List
from typing import Dict
from collections import Counter

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

solution = Solution()
print(solution.combinationSum2([2,5,2,1,2], 5))
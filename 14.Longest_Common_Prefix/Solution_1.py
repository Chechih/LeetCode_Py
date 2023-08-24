from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_leg = len(strs)
        rlt = ''
        if strs_leg < 1:# 沒有字串直接回傳空字串
            return rlt
        first_str = strs[0]
        strs.remove(first_str)
        for i, fc in enumerate(first_str): 
            is_same = True
            for s in strs:
                if len(s) <= i or s[i] != fc:# 檢查每個字串是不是都相同
                    is_same = False
                    break
            if not is_same:
                break
            rlt += fc
        return rlt

#測試
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
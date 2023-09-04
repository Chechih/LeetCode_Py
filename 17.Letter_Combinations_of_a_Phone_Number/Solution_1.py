from typing import List

class Solution:
    rule = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def gather(self, letters: List[int], digits: str, thisTxt: str = '') -> None:
        if(len(digits) < 1):
            letters.append(thisTxt)# 如果 digits 都消耗完畢，將蒐集的字母存起來
            return
        for m in self.rule[digits[0]]:# 取出一個數字開始跑有可能的字母
            self.gather(letters, digits[1::], thisTxt + m)
    
    def letterCombinations(self, digits: str) -> List[str]:
        rlt = []
        if digits != '':# 空的直接不跑
            self.gather(rlt, digits)
        
        return rlt

#測試
solution = Solution()
print(solution.letterCombinations("234"))

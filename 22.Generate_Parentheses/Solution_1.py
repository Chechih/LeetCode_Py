from typing import List

class Solution:
    def getCombination(self, lParentheses: int, rParentheses: int, combination: List[str], nowParenthes: str = '') -> None:
        if(lParentheses > 0):
            self.getCombination(lParentheses -1, rParentheses, combination, nowParenthes + '(')
        if(rParentheses > 0 and lParentheses < rParentheses):
            self.getCombination(lParentheses, rParentheses - 1, combination, nowParenthes + ')')
        if(lParentheses == 0 and rParentheses == 0):
            combination.append(nowParenthes)
        
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        self.getCombination(n, n, combination)
        return combination
    
# 測試
solution = Solution()
print(solution.generateParenthesis(3))
from collections import deque 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_parentheses = 0
        # 紀錄左誇號
        right_parentheses = 0
        max_leg = 0
        # 找最大合法值
        for c in s:
            if c == '(':
                left_parentheses += 1
            else:
                right_parentheses += 1
            if left_parentheses == right_parentheses:
                max_leg = max(max_leg, right_parentheses * 2)
            if left_parentheses < right_parentheses:
                left_parentheses = right_parentheses = 0
        left_parentheses = right_parentheses = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '(':
                left_parentheses += 1
            else:
                right_parentheses += 1
            if left_parentheses == right_parentheses:
                max_leg = max(max_leg, left_parentheses * 2)
            if left_parentheses > right_parentheses:
                left_parentheses = right_parentheses = 0
        
        return max_leg

            

solution = Solution()

print(solution.longestValidParentheses("(()") == 2)
print(solution.longestValidParentheses(")()())") == 4)
print(solution.longestValidParentheses("()(()") == 2)
print(solution.longestValidParentheses("())()))))") == 2)
print(solution.longestValidParentheses(")))(()(())(()") == 6)


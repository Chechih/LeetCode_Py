from collections import deque 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        rlt = 0
        stack = []
        stack.append(-1)
        # 先加入 -1 為了讓後面好計算
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                # 取出對應的左誇號
                if (not stack):
                    stack.append(i)
                    # 新的起始點
                else:
                    rlt = max(rlt, i - stack[-1])
                    # 因為 stack 不是空的代表左誇號是連在一起的所以直接減去他的前一位

        return rlt

            

solution = Solution()

print(solution.longestValidParentheses("(()") == 2)
print(solution.longestValidParentheses(")()())") == 4)
print(solution.longestValidParentheses("()(()") == 2)
print(solution.longestValidParentheses("())()))))") == 2)
print(solution.longestValidParentheses(")))(()(())(()") == 6)

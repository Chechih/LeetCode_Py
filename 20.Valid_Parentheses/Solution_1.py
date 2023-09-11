
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []# 記錄用的
        for c in s:
            if c == '(' or c == '[' or c == '{':# 左括號全部存起來
                stack.append(c)
            else:# 右括號，全部從堆疊底取出一個比對
                pop = None
                if stack:
                    pop = stack.pop()
                else:# 只有右括號
                    return False
                if c == ')' and pop != '(':
                    return False
                if c == ']' and pop != '[':
                    return False
                if c == '}' and pop != '{':
                    return False
        return len(stack) == 0 # 看看是不是空的，空的代表是完整的括號


#測試
solution = Solution()
print(solution.isValid(')()'))
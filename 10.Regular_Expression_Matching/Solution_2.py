class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        dp = [[False for i in range(s_leg + 1)] for j in range(p_leg + 1)]
        # 建 dp 用的陣列
        dp[0][0] = True
        for j in range(s_leg + 1):
            for i in range(1, p_leg + 1):# p 沒有字時，不可能匹配，直接不考慮
                if i - 1 >= 0 and p[i - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                    # 沒有 * 時，只能下去比對字串是不是相等，或是等於 . 了
                elif i - 2 >= 0:
                    dp[i][j] = dp[i - 2][j]
                    # * 重複 0 次時
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and (s[j - 1] == p[i - 2] or p[i - 2] == '.'))
                    # * 重複 1 次以上時

        return dp[p_leg][s_leg]
    
#測試
solution = Solution()
print(solution.isMatch("a", ".*..a*") == False)
print(solution.isMatch("aa", "aa") == True) 
print(solution.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*") == False)
print(solution.isMatch("aaa", "ab*a*c*aa") == True)
print(solution.isMatch("aa", "a") == False) 
print(solution.isMatch("aa", "a*") == True) 
print(solution.isMatch("ab", ".*") == True)
print(solution.isMatch("ab", ".*c") == False)
print(solution.isMatch("aaa", "a*a") == True) 
print(solution.isMatch("ssippi", "s*p*.") == False) 
print(solution.isMatch("mississippi", "mis*is*ip*.") == True) 
print(solution.isMatch("aab", "c*a*b") == True)
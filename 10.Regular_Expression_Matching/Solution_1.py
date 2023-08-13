class Solution:
    def run_isMatch(self, s: str, p: str) -> bool:
        s_leg = len(s)
        p_leg = len(p)
        if s == '' and p == '':
            return True
        if p_leg > 1 and p[1] == '*':
            if s_leg > 0 and (s[0] == p [0] or p [0] =='.'):
                return self.run_isMatch(s[1::], p) or self.run_isMatch(s, p[2::])
                #如果 p 第二個字是 *, 則可能是 s 第一個字, 或是完全沒匹配直接拿掉兩種可能
            else:
                #如果地一個字完全不同, 那一定要拿掉 p
                return self.run_isMatch(s, p[2::])
        if s_leg > 0 and p_leg > 0 and (s[0] == p [0] or p [0] =='.'):
            return self.run_isMatch(s[1::], p[1::])
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        p_ary = []# 用來把重複的正規清掉比如 a*a*a*a* -> a*
        for pc in p:
            if pc != '*':
                p_ary.append(pc)
            else:
                last = p_ary.pop()
                if len(p_ary) == 0 or (p_ary[-1] != last + '*'):
                    p_ary.append(last + '*')
        return self.run_isMatch(s, ''.join(p_ary))
                


#測試
solution = Solution()
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

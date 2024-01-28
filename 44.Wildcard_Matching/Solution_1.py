class Solution:
    rlt_dict = {}
    def merage_star(self, p: str) ->str:
        new_p = ''
        is_start = False
        for pp in p:
            if(pp == '*' and is_start):
                continue
            if(pp == '*'):
                is_start = True
            else:
                is_start = False
            new_p += pp
        return new_p
    def call_match(self, s: str, p: str) -> bool:
        if((s, p) in self.rlt_dict):
            return self.rlt_dict[(s, p)]
        if((len(s) <= 0 and p != '*') or (len(p) <= 0 and len(s) > 0)):
            self.rlt_dict[(s, p)] = False
        elif(p[0] == '?'):
            self.rlt_dict[(s, p)] = self.call_match(s[1:], p[1:])
        elif(p[0] == '*'):
            if(p == '*'):
                self.rlt_dict[(s, p)] = True
            else:
                self.rlt_dict[(s, p)] = self.call_match(s[1:], p) or self.call_match(s, p[1:])
        elif(s[0] == p[0]):
            self.rlt_dict[(s, p)] = self.call_match(s[1:], p[1:])
        else:
            self.rlt_dict[(s, p)] = False
        return self.rlt_dict[(s, p)]

    def isMatch(self, s: str, p: str) -> bool:
        self.rlt_dict = {}
        self.rlt_dict[('','')] = True
        p = self.merage_star(p)
        rlt =  self.call_match(s, p)
        return rlt



# solution = Solution()
# print(solution.isMatch("adceb","*a*b"))

# solution = Solution()
# print(solution.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))

# solution = Solution()
# print(solution.isMatch("abcabczzzde", "*abc???de*"))

solution = Solution()
print(solution.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
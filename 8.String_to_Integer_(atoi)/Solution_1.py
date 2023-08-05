class Solution:
    max_size = 2 ** 31 - 1#32 位元最大值
    min_size = -max_size - 1 #32 位元最小值
    def is_number(self, c: str)-> bool:
        '''
        檢查 char 是不是數字
        '''
        return c >= '0' and c <= '9'
    def myAtoi(self, s: str) -> int:
        s = s.strip()#字串左右兩邊空格拿掉
        rlt_s = ''
        if s.startswith('+'):#檢查正號
            s = s[1:]
        elif s.startswith('-'):#檢查負號
            s = s[1:]
            rlt_s = '-'
        for c in s:
            if self.is_number(c):
                rlt_s += c
            else:
                break
        if rlt_s == '' or rlt_s == '-':
            return 0
        rlt = int(rlt_s)
        if(rlt > self.max_size):
            return self.max_size
        elif(rlt < self.min_size):
            return self.min_size
        else:
            return rlt

#測試
solution = Solution()
print(solution.myAtoi("   +0 123"))
class Solution:
    def isHappy(self, n):
        s = set()
        return self.helper(n, s)
        
    def helper(self, n, s):
        if n == 1: 
            return True 
        n_str = str(n)
        sum = 0
        for c in n_str: 
            sum += int(c) * int(c) 
        if sum in s: 
            return False 
        s.add(sum)
        return self.helper(sum, s)
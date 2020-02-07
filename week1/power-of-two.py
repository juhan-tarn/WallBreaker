class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #using bitwise operator
        return n > 0 and not (n & n-1)

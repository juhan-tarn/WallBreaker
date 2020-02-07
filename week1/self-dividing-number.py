class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if self.check_sdn(i):
                ans.append(i)
        return ans

    def check_sdn(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num))

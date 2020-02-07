class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        for exp, char in enumerate(s[::-1]):
            sum += (ord(char) - ord("A") + 1) * (26 ** exp)
        return sum

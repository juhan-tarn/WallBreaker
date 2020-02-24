class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        flag = 0
        for i in range(len(s)):
            flag += (ord(t[i]) - ord(s[i]))
        flag += ord(t[-1])
        return chr(flag)
                
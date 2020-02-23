class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1 
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i
        return -1
            
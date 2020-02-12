class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.split()
        return " ".join([i[::-1]for i in new_s])
        
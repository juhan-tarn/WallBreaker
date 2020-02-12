class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j= 0, len(s) - 1 
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

'''
Use two pointers, one start from the beginning, one from the end
when i < j keep moving i/j if the current is not letters
if s[i] and s[j] are both letters, check if they are equal, 
return False if not
'''
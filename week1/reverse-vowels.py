class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        two pointers i and j
        if s[i] not vowels, i ++
        if s[j] not vowels, j--
        if s[i] and s[j] both are vowels, swap
        """
        
        i, j = 0, len(s) - 1
        vowels = 'aeiou'
        s = list(s)
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].lower() not in vowels:
                i += 1
            elif s[j].lower() not in vowels:
                j -= 1
        return "".join(s)

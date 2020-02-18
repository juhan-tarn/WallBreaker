class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #use two hashmap
        map_s, map_t = {}, {}
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = t[i]
            elif map_s[s[i]] != t[i]:
                return False
        for i in range(len(t)):
            if t[i] not in map_t:
                map_t[t[i]] = s[i]
            elif map_t[t[i]] != s[i]:
                return False
        return True
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans =[]
        ls=len(s)
        lp=len(p)
        
        s_list = [0 for i in range(26)]
        p_list = [0 for i in range(26)]
        
        '''
        construct the array for pattern 
        '''
        for i in range(lp):
            p_list[ord(p[i]) - ord('a')] += 1
        '''
        while iterating the loop, construct the array for the given string and
        constantly compare with the pattern list 
        '''
        for i in range(ls):
            if i >= lp:
                s_list[ord(s[i-lp]) - ord('a')] -= 1
           
            s_list[ord(s[i]) - ord('a')] += 1
            
            if s_list == p_list:
                ans.append(i - lp + 1)
        
        return ans
class Solution:
    '''
    Approach 1: sort
    '''
    def isAnagram(self, s, t):
        if(sorted(s) == sorted(t)):
            return True
        return False

    '''
    Approach 2:
    list of size 26 to record the frequency of each letter in the given string
    '''
    def isAnagram_II(self, s, t):
        s_list, t_list = [0] * 26, [0] * 26
        s_list = self.helper(s, s_list)
        t_list = self.helper(t, t_list)
        return s_list == t_list

    def helper(self, input_str, input_list):
        for char in input_str:
            input_list[ord(char) - ord("a")] += 1
        return input_list

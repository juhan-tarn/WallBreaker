class Solution:
    def wordPattern(self, pattern: str, str_: str) -> bool:
        tokens = str_.split()
            
        if len(tokens) != len(pattern):
            return False
        dict_ = {}
        
        for i, word in enumerate(tokens):
            if word in dict_.keys():
                if pattern[i] != dict_[word]:
                    return False
            else:
                if pattern[i] in dict_.values():
                    return False
                dict_[word] = pattern[i]
        return True
class Solution:
    import collections
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        new_paragraph = paragraph.lower().split()
        
        ban_set = set(banned)
        word_count, max_word, max_count = {}, '', 0
        
        for word in new_paragraph:
            if word in ban_set:
                continue
            word_count[word] = word_count.get(word, 0) + 1
            if word_count[word] > max_count:
                max_word, max_count = word, word_count[word]
            
        return max_word

    def mostCommonWord_II(self, paragraph: str, banned: List[str]) -> str:    
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split()
        count = collections.Counter(words)
        for word in banned:
            del count[word]
        return count.most_common(1)[0][0]
        
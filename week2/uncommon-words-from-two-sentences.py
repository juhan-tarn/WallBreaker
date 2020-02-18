class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_count = {}
        A = A.split()
        B = B.split()
        whole = A + B
        for word in whole:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        return [word for word in word_count if word_count[word] == 1]
        
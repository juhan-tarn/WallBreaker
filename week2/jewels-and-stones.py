class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #return sum(S.count(j) for j in J)
        return sum([ch in set(J) for ch in S])
        
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        B = set()
        for a in A:
            B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
        return len(B)
        
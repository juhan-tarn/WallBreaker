class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        reversed = [i[::-1] for i in A]
        for i in range(len(reversed)):
            for j in range(len(reversed)):
                reversed[i][j] = 1 - reversed[i][j]
        return reversed
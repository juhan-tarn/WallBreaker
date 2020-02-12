class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        cnt_row, cnt_col = len(A), len(A[0])
        result = []
        
        for i in range(cnt_col):
            new_row = []
            for j in range(cnt_row):
                new_row.append(A[j][i])
            result.append(new_row)
        return result
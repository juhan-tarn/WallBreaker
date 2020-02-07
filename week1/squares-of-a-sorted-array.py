class Solution:
    #using sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i*i for i in A])

    #using two pointers
    def sortedSquares_II(self, A:List[int]) -> List[int]:
        '''
        first find the critical point that separates +- , i for negative, j for positive
        while i >= 0 and j < len(A):
            if A[i]**2 < A[j] **2: append A[i], i--
            else append A[j], j --
        while i >= 0: append A[i], i --
        while j < N, append A[j], j++
        '''
        ans = []
        j = 0
        while j < len(A) and A[j] < 0:
            j += 1
        i = j - 1
        while i >= 0 and j < len(A):
            if A[i]**2 < A[j] **2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1
        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
        while j < len(A):
            ans.append(A[j] ** 2)
            j += 1
        return ans

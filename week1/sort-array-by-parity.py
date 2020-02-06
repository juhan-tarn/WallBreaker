class Solution:
    '''
    Approach 1:
    Use two arrays to record even and odd
    '''
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd

    '''
    Approach 2:
    In-place
    '''
    def sortArrayByParity_in_place(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2: #(1, 0)
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A

class Solution:
    #using sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i*i for i in A])

    #using two pointers
    def sortedSquares_II(self, A:List[int]) -> List[int]:
        

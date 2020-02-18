class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candyKinds = set()
        for candy in candies:
            candyKinds.add(candy)
        return min(len(candyKinds), len(candies) // 2)

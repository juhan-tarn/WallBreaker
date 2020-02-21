class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection_II(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        s1, s2 = set(nums1), set(nums2)
        return [x for x in s1 if x in s2]
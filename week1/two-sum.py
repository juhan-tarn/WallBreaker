class Solution(object):
    def twoSum(self, nums, target):
        ansdict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ansdict.keys():
                return [ansdict[diff], i]
            ansdict[nums[i]] = i

        raise("No Two Sum solution")

    '''
    time complexity: O(n) for building the hashmap
    space complexity: O(n) for using the hashmap
    '''

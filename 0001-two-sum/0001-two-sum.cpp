class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for indx, num in enumerate(nums):
            if num in d:
                return[d[num], indx]
            else:
                d[target - num] = indx
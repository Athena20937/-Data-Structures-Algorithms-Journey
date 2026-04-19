class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 
        r = len(nums) - 1
        k = len(nums)
        while l <= r:
            if nums[r] == val:
                nums.remove(nums[r])
                r -= 1
            else:
                r -= 1
        return k
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums)==len(nums):
            return False
        return True

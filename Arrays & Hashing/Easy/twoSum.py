class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i, n in enumerate(nums):
            diff = target - n
            ind = dict_nums.get(diff, -1)
            if ind != -1:
                return [dict_nums[diff], i]
            else:
                dict_nums[n] = i

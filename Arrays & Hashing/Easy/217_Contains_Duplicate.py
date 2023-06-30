class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sol 1
        # set_nums = set(nums)
        # if len(set_nums) == len(nums):
        #     return False
        # else:
        #     return True

        #sol 2
        # dict_nums = {}
        # for i in nums:
        #     dict_nums[i]=1 + dict_nums.get(i,0)
        # for i in nums:
        #     if dict_nums[i]>1:
        #         return True
        # return False

        #sol 3
        set_num = set()
        for i in nums:
            if i in set_num:
                return True
            set_num.add(i)
        return False

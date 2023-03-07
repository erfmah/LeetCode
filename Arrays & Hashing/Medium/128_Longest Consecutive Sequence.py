class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_l = 0
        l = 1
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                l = 1
                while n+l in nums:
                    l += 1
                max_l = max(l , max_l)
            #print(n,checked)
        return max_l
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for n in nums:
            dict_nums[n] = 1 + dict_nums.get(n,0)
        values = sorted(dict_nums.values())
        ans = []
        for n in dict_nums:
            if dict_nums[n] in values[len(dict_nums)-k:]:
                ans.append(n)
        return ans

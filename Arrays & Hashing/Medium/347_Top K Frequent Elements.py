class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_num = {}
        for n in nums:
            dict_num[n] = 1 + dict_num.get(n, 0)
        vals = dict_num.values()
        s_val = sorted(vals)
        res = []
        for ke in dict_num.keys():
            if dict_num[ke] in s_val[-1*k:]:
                res.append(ke)
        return res
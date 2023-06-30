class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict_num = {}
        # for n in nums:
        #     dict_num[n] = 1 + dict_num.get(n, 0)
        # vals = dict_num.values()
        # s_val = sorted(vals)
        # res = []
        # i=1
        # print(s_val)
        # for i in range(1, k+1):
        #     res.append(list(dict_num.keys())[list(dict_num.values()).index(s_val[-1*i])])
        #     del dict_num[list(dict_num.keys())[list(dict_num.values()).index(s_val[-1*i])]]
        # return res

        d = {}
        res = []
        for i in nums:
            d[i] = 1+d.get(i,0)
        vals = d.values()
        vals = sorted(vals)
        print(vals)
        vals = vals[len(vals)-k:]
        keys = d.keys()
        print("keys", keys)
        print(vals)
        for i in keys:
            if d[i] in vals:
                res.append(i)
        return res
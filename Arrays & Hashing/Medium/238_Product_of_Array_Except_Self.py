class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # p = 1
        # has_zero = False
        # for n in nums:
        #     if n ==0:
        #         if has_zero:
        #             return [0]*len(nums)
        #         else:
        #             has_zero = True
        #     else:
        #          p *= n
        # res = []
        # for n in nums:
        #     if n == 0:
        #         res.append(int(p))
        #     else:
        #         if has_zero:
        #             res.append(0)
        #         else:
        #             res.append(int(p/n))
        # return res

        mult = 1
        has_zero = False
        has_two_zero = False
        for i in nums:
            if i == 0 :
                if has_zero:
                    has_two_zero = True
                has_zero = True
            else:
                mult *= i
        res = []
        if has_two_zero:
            return [0]*len(nums)
        for i in nums:
            if has_zero:
                if i == 0:
                    res.append(mult)
                else:
                    res.append(0)
            else:
                res.append(int(mult/i))
        return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zero = False
        has_2_zero = False
        prod = 1
        for n in nums:
            if n != 0:
                prod *= n
            else:
                if has_zero:
                    has_2_zero = True
                else:
                    has_zero = True
        if has_2_zero:
            return [0]*len(nums)
        
        res = []
        for i, n in enumerate(nums):
            if has_zero:
                if n == 0: 
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//n)
        return res
            

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        checked_three = []
        checked_element = []
        nums = sorted(nums)
        res = set()
        #print(nums)
        for i in range(len(nums)):
            if not i in checked_element:
                checked_element.append(nums[i])
                l = i+1
                r = len(nums)-1
               # print("1:", i, nums[i])
                while l<r:
                    if nums[l]+nums[r]>(-1*nums[i]):
                        r -= 1
                        #print("2:", i, nums[i], l , r)
                    elif nums[l]+nums[r]<(-1*nums[i]):
                        l += 1
                        #print("3:", i, nums[i], l , r)
                    elif nums[l]+nums[r]==(-1*nums[i]):
                        #print("4:", i, nums[i], l , r)
                        res.add((nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return res


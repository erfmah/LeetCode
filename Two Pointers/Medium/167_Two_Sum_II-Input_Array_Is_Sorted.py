class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sol 1
        # res=[]
        # i = 0
        # for i in range(len(numbers)):
        #     if target-numbers[i] in numbers:
        #         if i != numbers.index(target-numbers[i]):
        #             res.append(i+1)
        #     i+=1
        # return res

        #sol2
        l = 0
        r = len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return l+1,r+1
            elif numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1
        #sol 3
        # d = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in d:
        #         return d[target - numbers[i]] , i+1
        #     else:
        #         d[numbers[i]] = i+1
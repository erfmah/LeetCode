class Solution:
    def maxArea(self, height: List[int]) -> int:
#sol 1: not efficient time limit

        # res = []
        # for i, n in enumerate(height):
        #     max_temp = -1
        #     for j in range(i+1, len(height)):
        #         area = (j-i) * min(height[i], height[j])
        #         if area > max_temp:
        #             max_temp = area
        #     res.append(max_temp)
        # return max(res)
        l = 0
        r = len(height) - 1
        max_area = (r-l)*min(height[l], height[r])
        for i, n in enumerate(height):
            max_area = max(max_area, (r-l)*min(height[l], height[r]))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_area
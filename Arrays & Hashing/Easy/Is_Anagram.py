class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #o(nlogn)
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # return False
        #o(n)
        counter = [0]*27
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            counter[ord(s[i])-ord('a')]+=1
            counter[ord(t[i])-ord('a')]-=1
        for c in counter:
            if c != 0:
                return False
        return True

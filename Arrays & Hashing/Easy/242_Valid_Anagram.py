class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #sol 1
        """
        letters = dict()
        for l1 in s:
            if l1 in letters.keys():
                letters[l1] +=1
            else:
                letters[l1] = 1
        letters2 = dict()
        for l1 in t:
            if l1 in letters2.keys():
                letters2[l1] +=1
            else:
                letters2[l1] = 1
        """

        #sol 2
        # if len(s) != len(t):
        #     return False
        # dict_s, dict_t = dict(), dict()
        # for l in range(len(s)):
        #     dict_s[s[l]] = 1 + dict_s.get(s[l],0)
        #     dict_t[t[l]] = 1 + dict_t.get(t[l],0)
        # return dict_s == dict_t

        #sol 3
        dict_s = {}
        dict_t = {}
        for i in s:
            dict_s[i] = 1 + dict_s.get(i, 0)
        for i in t:
            dict_t[i] = 1 + dict_t.get(i, 0)
        return dict_s == dict_t

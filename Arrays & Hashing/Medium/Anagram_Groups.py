class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ans = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in dict_ans.keys():
                l_s = dict_ans[sorted_s]
                l_s.append(s)
                dict_ans[sorted_s] = l_s
            else:
                dict_ans[sorted_s] = [s]
                
        return dict_ans.values()

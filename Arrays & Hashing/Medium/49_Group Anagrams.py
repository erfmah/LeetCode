class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = []
        for s in strs:
            d = {}
            for l in s:
                d[l] = 1 + d.get(l, 0)
            dicts.append(d)

        selected = set()
        res = []
        for i in range(len(strs)):
            r = []
            if not i in selected:
                selected.add(i)
                r.append(strs[i])
            else:
                continue
            for j in range(len(strs)):
                if dicts[j] == dicts[i] and j not in selected:
                    r.append(strs[j])
                    selected.add(j)
            res.append(r)
        return res

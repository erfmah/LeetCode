class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dicts = []
        # for s in strs:
        #     d = {}
        #     for l in s:
        #         d[l] = 1 + d.get(l,0)
        #     dicts.append(d)
        
        # selected = set()
        # res = []
        # for i in range(len(strs)):
        #     r = []
        #     if not i in selected:
        #         selected.add(i)
        #         r.append(strs[i])
        #     else:
        #         continue
        #     for j in range(len(strs)):
        #         if dicts[j]== dicts[i]and j not in selected:
        #             r.append(strs[j])
        #             selected.add(j)
        #     res.append(r)
        # return res

        # dicts = []
        # for s in strs:
        #     d = {}
        #     for i in s:
        #         d[i] = 1 + d.get(i,0)
        #     dicts.append(d)
        # res = []
        # selected = []
        # for i in range(len(strs)):
        #     if i not in selected:
        #         r = [strs[i]]
        #         selected.append(i)
        #         for j in range(i+1, len(strs)):
        #             if dicts[i] == dicts[j]:
        #                 if j not in selected:
        #                     r.append(strs[j])
        #                     selected.append(j)
        #                 else:
        #                     continue
        #         res.append(r)
        # return res

        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
            print(ans)
        return ans.values()

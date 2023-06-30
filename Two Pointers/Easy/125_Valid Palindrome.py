class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # s_org = ""
        # s_org_r = ""
        # for i in s:
        #     if i.isdigit() or i.isalpha():
        #         s_org = s_org+i
        #         s_org_r = i+s_org_r
        # print(s_org,s_org_r)
        # return s_org==s_org_r
        # s_1 = ""
        # s_2 = ""
        # s = s.lower()
        # for i in s:
        #     if i.isalpha() or i.isdigit():
        #         s_1 = s_1+i
        #         s_2 = i+s_2
        # return s_1 == s_2
        l = 0 
        r = len(s)-1
        s = s.lower()
        while l<=r:
            if not (s[l].isdigit() or s[l].isalpha()):
                l+=1
                # print("1",l)
            elif not (s[r].isdigit() or s[r].isalpha()):
                r-=1
                # print("2",r)
            elif s[l] == s[r]:
                l+=1
                r-=1
                # print("3", l,r)
            else:
                # print("4", s[l],s[r])
                return False
        return True
         
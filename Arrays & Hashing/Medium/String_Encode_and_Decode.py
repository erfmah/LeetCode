class Solution:

    def encode(self, strs: List[str]) -> str:
        embedding = ""
        for s in strs:
            embedding += str(len(s)) + "r" + s
        return embedding

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        print(s)
        while i < len(s):
            print(i)
            print(output)
            length = int(s[i])
            while s[i+1] != 'r':
                length = length*10+int(s[i+1])
                i += 1
            i+=1
            if length == 0:
                output.append("")
            else:
                output.append(s[i+1: i+1+length])
            i = i+1+length
        return output

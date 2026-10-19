class Solution:

    def encode(self, strs: List[str]) -> str:
        s_encode = []

        for s in strs:
            s_encode.append(str(len(s)))
            s_encode.append('#')
            s_encode.append(s)

        return ('').join(s_encode)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1

            l = int(s[i:j])
            i = j + 1
            j = i + l

            res.append(s[i:j])
            i = j

        return res






        

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for val in strs:
            s += str(len(val)) + "#" + val
        
        return s

    def decode(self, s: str) -> List[str]: 
        ans = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            ans.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return ans
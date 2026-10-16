class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        new_s = {}
        new_t = {}

        for i in range(len(s)):
            new_s[s[i]] = new_s.get(s[i], 0) + 1
            new_t[t[i]] = new_t.get(t[i], 0) + 1

        return new_s == new_t

       
        
        
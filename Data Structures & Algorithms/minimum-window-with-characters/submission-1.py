class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or not s or not t:
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen, l = [-1,-1], float('inf'), 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch,0)

            if ch in countT and countT[ch] == window[ch]:
                have+=1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r-l+1
                    res = [l, r]

                window[s[l]]-=1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have-=1

                l+=1

        l, r = res

        return s[l:r+1]







        
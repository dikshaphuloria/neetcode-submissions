class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""

        countT = {}

        for val in t:
            countT[val] = 1 + countT.get(val, 0)

        window = {}
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("inf")
        left = 0

        for right, val in enumerate(s):
            window[val] = 1 + window.get(val, 0)

            if val in countT and window[val] == countT[val]:
                have+=1

            while have == need:
                if (right - left + 1) < reslen:
                    res = [left, right]
                    reslen = right - left + 1

                window[s[left]]-=1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have-=1
                
                left+=1
            
        left,right = res

        return s[left:right+1]




        

        

        
           


            

            

        

        
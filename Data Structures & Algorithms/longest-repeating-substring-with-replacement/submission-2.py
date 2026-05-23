class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0 
        maxf = 0

        for right, val in enumerate(s):
            count[val] = 1 + count.get(val, 0)
            maxf = max(maxf, count[val])

            while (right - left + 1) - maxf > k:
                count[s[left]]-=1
                left+=1

            res = max((right - left + 1), res)

        return res
            

        
        
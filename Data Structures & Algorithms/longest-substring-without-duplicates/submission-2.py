class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l = 0

        for r, val in enumerate(s):
            while val in seen:
                seen.remove(s[l])
                l+=1
            seen.add(val)

            longest = max(longest, r-l+1)


        return longest
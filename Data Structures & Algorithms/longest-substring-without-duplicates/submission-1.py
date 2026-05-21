class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        longest = 0
        
        for c in s:
            if c not in seen:
                seen.append(c)

            else:
                seen = seen[seen.index(c)+1:]
                seen.append(c)

            longest = max(longest, len(seen))


        return longest
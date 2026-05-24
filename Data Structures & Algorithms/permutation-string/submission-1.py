class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window = {}
        left = 0

        for val in s1:
            s1_count[val] = 1 + s1_count.get(val, 0)

        for right, val in enumerate(s2):
            window[val] = 1 + window.get(val, 0)

            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char]-=1

                if window[left_char] == 0:
                    del window[left_char]
                
                left+=1

            if s1_count == window:
                return True

        return False
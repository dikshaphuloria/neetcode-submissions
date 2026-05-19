class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for val in s:
            if val.isalnum():
                new_str+=val.lower()

        return new_str == new_str[::-1]
        
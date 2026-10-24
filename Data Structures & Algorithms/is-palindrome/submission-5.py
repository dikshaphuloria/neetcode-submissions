class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list(x.lower() for x in s if x.isalnum())

        return new_s == new_s[::-1]



        
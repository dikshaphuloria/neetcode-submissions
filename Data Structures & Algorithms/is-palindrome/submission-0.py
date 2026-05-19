class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []

        for val in s:
            if val.isalnum():
                new_list.append(val.lower())

        return new_list == new_list[::-1]
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            elif not self.alphaNum(s[left].lower()):
                left+=1

            elif not self.alphaNum(s[right].lower()):
                right-=1

            else:
                return False

        return True

    
    def alphaNum(self, c:str):
        return (ord('a') <= ord(c) <= ord('z')
             or ord('0') <= ord(c) <= ord('9'))

        
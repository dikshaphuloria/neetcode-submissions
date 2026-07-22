class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        bracket_dict = {')':'(', ']':'[', '}':'{'}
        stack = []

        for b in s:
            if b in bracket_dict:
                if stack and stack[-1] == bracket_dict[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0




        
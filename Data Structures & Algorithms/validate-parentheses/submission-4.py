class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')':'(', ']':'[', '}':'{'}
        stack = []

        for b in s:
            if b in bracket:
                if stack and stack[-1] == bracket[b]:
                    stack.pop()
                else:
                    stack.append(b)

            else:
                stack.append(b)

        return stack == []

        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {')':'(', '}':'{', ']':'['}

        for i, val in enumerate(s):
            if val in match.values():
                stack.append(val)

            elif stack and stack[-1] == match[val]:
                stack.pop()

            else:
                stack.append(val)

        return stack == []

        
        

        
        
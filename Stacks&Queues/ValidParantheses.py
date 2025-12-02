class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#" # this means only pop from the stack if stack is not empty
                # assign dummy value if stack is empty
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack # python treats empty collections as false and non-empty as true

        

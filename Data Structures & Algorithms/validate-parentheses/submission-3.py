class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            b = []
            chars = {']':'[', '}':'{', ')':'('}
            stack = []
            for char in s:
                if char in chars:
                    top_element = stack.pop() if stack else "*"
                    if top_element != chars[char]:
                        return False

                else:
                    stack.append(char)
            return len(stack) == 0
            
          

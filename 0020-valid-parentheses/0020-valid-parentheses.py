class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        if (len(s)%2 != 0):
            return False

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if (len(stack) != 0):
                    if (i == ")"):
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    elif (i == "}"):
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    elif (i == "]"):
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
                else: 
                    return False
        if (len(stack) != 0):
            return False
            
        return True
        
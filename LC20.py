class Solution:
    def isValid(self, s: str) -> bool:
        brStack = []
        for i in s:
            if i == "(":
                brStack.append(")")
            elif i == "{":
                brStack.append("}")
            elif i == "[":
                brStack.append("]")
            elif brStack == [] or i != brStack[-1]:
                return False
            else:
                brStack.pop()
        return brStack == []

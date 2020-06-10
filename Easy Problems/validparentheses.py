def isValid(s):
        
    # :type s: str
    # :rtype: bool

#Try 1 - ran in 32 ms and took 12.7 MB of memory
    parenList = []
    for char in s:
        if not parenList:
            parenList.append(char)
        elif char == ")" and parenList[-1] == "(":
            parenList.pop()
        elif char == "}" and parenList[-1] == "{":
            parenList.pop()
        elif char == "]"and parenList[-1] == "[":
            parenList.pop()
        else:
            parenList.append(char)

    if not parenList:
        return True
    else:
        return False

#Testing
s = "]"
t = "()[]{}"
u = "(]" 
v = "([)]"
w = "{[]}"
print(isValid(s))
print(isValid(t))
print(isValid(u))
print(isValid(v))
print(isValid(w))                  
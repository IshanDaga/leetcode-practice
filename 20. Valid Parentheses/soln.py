def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stck = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stck.append(c)
        else:
            if len(stck) < 1:
                return 0
            if c == ')' and stck[-1] != '(':
                return 0
            elif c == ']' and stck[-1] != '[':
                return 0
            elif c == '}' and stck[-1] != '{':
                return 0
            else :
                stck.pop()
    if stck == []:
        return 1
    return 0

print(isValid('()[]{}'))
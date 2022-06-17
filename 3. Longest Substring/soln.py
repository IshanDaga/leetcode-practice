def lengthOfLongestSubstring(s: str) -> int:
    if(len(s) == 0):
        return 0
    if(len(s) == 1):
        return 1
    li = [s[0]]
    lp,rp = 0,1
    res = 0
    while rp<len(s):
        if s[rp] in li:
            while s[lp] != s[rp]:
                li.remove(s[lp])
                lp += 1
            li.remove(s[lp])
            lp += 1
        li.append(s[rp])
        rp += 1
        res = max(res, len(li))
    return res

print(lengthOfLongestSubstring("bbbbbb"))
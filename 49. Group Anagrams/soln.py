from collections import defaultdict
from typing import List

def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        ans[str(sorted(s))].append(s)
    return ans.values()

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    count = [0]*26
    ans = defaultdict(list)
    for s in strs:
        for c in s:
            count[ord(c)-ord('a')] +=1
        ans[tuple(count)].append(s)
    return ans.values()
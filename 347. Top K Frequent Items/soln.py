from collections import defaultdict
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = defaultdict(int)
    for n in nums:
        res[n] += 1
    res = sorted(res.items(), key = lambda item: item[1], reverse=True)
    return [res[i][0] for i in range(k)]

topKFrequent([1,1,1,1,2,2,3,4,5], 2)
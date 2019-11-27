from typing import List
from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        l = list(map(Counter, A))
        res = reduce(lambda x, y: x & y, l)
        return list(res.elements())

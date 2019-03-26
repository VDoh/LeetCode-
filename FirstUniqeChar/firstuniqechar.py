import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] +=1
        
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
        
s = Solution()
s.firstUniqChar("oopppee")
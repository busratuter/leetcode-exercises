from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev_seq = self.countAndSay(n - 1)
        result = ""
        
        for char, group in groupby(prev_seq):
            count = len(list(group))
            result += str(count) + char
        
        return result

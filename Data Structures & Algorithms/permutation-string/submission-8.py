import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        combs = []
        ret = False
        if len(s1) > len(s2) or not set(s1).issubset(set(s2)):
            return ret
        else:
            for p in itertools.permutations(s1):
                word = "".join(p)
                if word in s2:
                    ret = True
                    break
            return ret
            
        
        
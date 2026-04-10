class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        if len(ss) != len(tt):
            return False
        state = True
        for i in ss:
            if i not in tt:
                state = False
                return state
            else:
                state = True
                tt.remove(i)
        return state
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        ss = list(s2)
        pali = True

        tt = ss
        ss = ss[::-1]

        for i in range(len(tt)):
            if tt[i] == ss[i]:
                pali = True
            else:
                pali = False
                return pali
        return pali
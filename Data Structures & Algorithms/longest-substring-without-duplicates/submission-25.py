class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        string = 1
        if s == "":
            return 0

        l = [s[0]]
        for i in range(1,len(s)):
            if s[i] not in l:
                l.append(s[i])
                string = len(l) 
            else:
                index = l.index(s[i])
                l = l[index + 1:] + [s[i]]
                string = len(l) 
                longest = max(longest, string)

            longest =  max(longest, string)
        return longest

        
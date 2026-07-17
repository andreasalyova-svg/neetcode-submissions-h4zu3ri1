class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        longest = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            potrebne_zmeny = (right - left +1) - max_freq 
            while potrebne_zmeny > k:
                counts[s[left]] -= 1
                left += 1
                potrebne_zmeny = (right - left +1) - max_freq 
                
            longest = max(longest, right - left +1)
        return longest
